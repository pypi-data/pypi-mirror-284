import json
from enum import Enum
from typing import List, Optional, Type
from urllib.parse import urlparse, urlunparse

import pycountry
from bs4 import BeautifulSoup

from ..connection import Connection
from ..objects import (Album, Artist, ArtworkCollection, Contact,
                       DatabaseObject, FormattedText, ID3Timestamp, Label,
                       Lyrics, Song, Source, SourceType, Target)
from ..utils import dump_to_file
from ..utils.config import logging_settings, main_settings
from ..utils.enums import ALL_SOURCE_TYPES, SourceType
from ..utils.shared import DEBUG
from ..utils.string_processing import clean_song_title
from ..utils.support_classes.download_result import DownloadResult
from .abstract import Page

if DEBUG:
    from ..utils import dump_to_file


def _parse_artist_url(url: str) -> str:
    parsed = urlparse(url)
    return urlunparse((parsed.scheme, parsed.netloc, "/music/", "", "", ""))


def _get_host(source: Source) -> str:
    parsed = urlparse(source.url)
    return urlunparse((parsed.scheme, parsed.netloc, "", "", "", ""))


class BandcampTypes(Enum):
    ARTIST = "b"
    ALBUM = "a"
    SONG = "t"


class Bandcamp(Page):
    SOURCE_TYPE = ALL_SOURCE_TYPES.BANDCAMP

    def __init__(self, *args, **kwargs):
        self.connection: Connection = Connection(
            host="https://bandcamp.com/",
            logger=self.LOGGER,
            module="bandcamp",
        )

        super().__init__(*args, **kwargs)

    def get_source_type(self, source: Source) -> Optional[Type[DatabaseObject]]:
        path = source.parsed_url.path.replace("/", "")

        if path == "" or path.startswith("music"):
            return Artist
        if path.startswith("album"):
            return Album
        if path.startswith("track"):
            return Song

        return super().get_source_type(source)

    def _parse_autocomplete_api_result(self, data: dict) -> DatabaseObject:
        try:
            object_type = BandcampTypes(data["type"])
        except ValueError:
            return

        url = data["item_url_root"]
        if "item_url_path" in data:
            url = data["item_url_path"]

        source_list = [Source(self.SOURCE_TYPE, url)]
        name = data["name"]

        if data.get("is_label", False):
            return Label(
                name=name,
                source_list=source_list
            )

        if object_type is BandcampTypes.ARTIST:
            source_list = [Source(self.SOURCE_TYPE, _parse_artist_url(url))]
            return Artist(
                name=name,
                source_list=source_list
            )

        if object_type is BandcampTypes.ALBUM:
            return Album(
                title=name,
                source_list=source_list,
                artist_list=[
                    Artist(
                        name=data["band_name"].strip(),
                        source_list=[
                            Source(self.SOURCE_TYPE, data["item_url_root"])
                        ]
                    )
                ]
            )

        if object_type is BandcampTypes.SONG:
            return Song(
                title=clean_song_title(name, artist_name=data["band_name"]),
                source_list=source_list,
                artist_list=[
                    Artist(
                        name=data["band_name"],
                        source_list=[
                            Source(self.SOURCE_TYPE, data["item_url_root"])
                        ]
                    )
                ]
            )

    def general_search(self, search_query: str, filter_string: str = "") -> List[DatabaseObject]:
        results = []

        r = self.connection.post("https://bandcamp.com/api/bcsearch_public_api/1/autocomplete_elastic", json={
            "fan_id": None,
            "full_page": True,
            "search_filter": filter_string,
            "search_text": search_query,
        }, name=f"search_{filter_string}_{search_query}")
        if r is None:
            return results

        if DEBUG:
            dump_to_file("bandcamp_search_response.json", r.text, is_json=True, exit_after_dump=False)

        data = r.json()

        for element in data.get("auto", {}).get("results", []):
            r = self._parse_autocomplete_api_result(element)
            if r is not None:
                results.append(r)

        return results

    def label_search(self, label: Label) -> List[Label]:
        return self.general_search(label.name, filter_string="b")

    def artist_search(self, artist: Artist) -> List[Artist]:
        return self.general_search(artist.name, filter_string="b")

    def album_search(self, album: Album) -> List[Album]:
        return self.general_search(album.title, filter_string="a")

    def song_search(self, song: Song) -> List[Song]:
        return self.general_search(song.title, filter_string="t")

    def fetch_label(self, source: Source, stop_at_level: int = 1) -> Label:
        return Label()

    def _parse_artist_details(self, soup: BeautifulSoup) -> Artist:
        name: str = None
        source_list: List[Source] = []
        contact_list: List[Contact] = []

        band_name_location: BeautifulSoup = soup.find("p", {"id": "band-name-location"})
        if band_name_location is not None:
            title_span = band_name_location.find("span", {"class": "title"})
            if title_span is not None:
                name = title_span.text.strip()

        link_container: BeautifulSoup = soup.find("ol", {"id": "band-links"})
        if link_container is not None:
            li: BeautifulSoup
            for li in link_container.find_all("a"):
                if li is None and li['href'] is not None:
                    continue

                source_list.append(Source.match_url(_parse_artist_url(li['href']), referrer_page=self.SOURCE_TYPE))

        return Artist(
            name=name,
            source_list=source_list
        )

    def _parse_album(self, soup: BeautifulSoup, initial_source: Source) -> List[Album]:
        title = None
        source_list: List[Source] = []

        a = soup.find("a")
        if a is not None and a["href"] is not None:
            source_list.append(Source(self.SOURCE_TYPE, _get_host(initial_source) + a["href"]))

        title_p = soup.find("p", {"class": "title"})
        if title_p is not None:
            title = title_p.text.strip()

        return Album(title=title, source_list=source_list)

    def _parse_artist_data_blob(self, data_blob: dict, artist_url: str):
        parsed_artist_url = urlparse(artist_url)
        album_list: List[Album] = []

        for album_json in data_blob.get("buyfulldisco", {}).get("tralbums", []):
            album_list.append(Album(
                title=album_json["title"].strip(),
                source_list=[Source(
                    self.SOURCE_TYPE,
                    urlunparse((parsed_artist_url.scheme, parsed_artist_url.netloc, album_json["page_url"], "", "", ""))
                )]
            ))

        return album_list

    def fetch_artist(self, source: Source, stop_at_level: int = 1) -> Artist:
        artist = Artist()

        r = self.connection.get(_parse_artist_url(source.url), name=f"artist_{urlparse(source.url).scheme}_{urlparse(source.url).netloc}")
        if r is None:
            return artist

        soup = self.get_soup_from_response(r)

        if DEBUG:
            dump_to_file("artist_page.html", r.text, exit_after_dump=False)

        artist = self._parse_artist_details(soup=soup.find("div", {"id": "bio-container"}))

        html_music_grid = soup.find("ol", {"id": "music-grid"})
        if html_music_grid is not None:
            for subsoup in html_music_grid.find_all("li"):
                artist.album_collection.append(self._parse_album(soup=subsoup, initial_source=source))

        # artist artwork
        artist_artwork: BeautifulSoup = soup.find("img", {"class":"band-photo"})
        if artist_artwork is not None:
            artist.artwork.add_data(artist_artwork.get("data-src", artist_artwork.get("src")))
        
        for i, data_blob_soup in enumerate(soup.find_all("div", {"id": ["pagedata", "collectors-data"]})):
            data_blob = data_blob_soup["data-blob"]

            if DEBUG:
                dump_to_file(f"bandcamp_artist_data_blob_{i}.json", data_blob, is_json=True, exit_after_dump=False)

            if data_blob is not None:
                artist.album_collection.extend(
                    self._parse_artist_data_blob(json.loads(data_blob), source.url)
                )

        artist.source_collection.append(source)
        return artist

    def _parse_track_element(self, track: dict, artwork: ArtworkCollection) -> Optional[Song]:
        lyrics_list: List[Lyrics] = []

        _lyrics: Optional[str] = track.get("item", {}).get("recordingOf", {}).get("lyrics", {}).get("text")
        if _lyrics is not None:
            lyrics_list.append(Lyrics(text=FormattedText(plain=_lyrics)))

        return Song(
            title=clean_song_title(track["item"]["name"]),
            source_list=[Source(self.SOURCE_TYPE, track["item"]["mainEntityOfPage"])],
            tracksort=int(track["position"]),
            artwork=artwork,
        )

    def fetch_album(self, source: Source, stop_at_level: int = 1) -> Album:
        album = Album()

        r = self.connection.get(source.url, name=f"album_{urlparse(source.url).netloc.split('.')[0]}_{urlparse(source.url).path.replace('/', '').replace('album', '')}")
        if r is None:
            return album

        soup = self.get_soup_from_response(r)

        data_container = soup.find("script", {"type": "application/ld+json"})

        if DEBUG:
            dump_to_file("album_data.json", data_container.text, is_json=True, exit_after_dump=False)

        data = json.loads(data_container.text)
        artist_data = data["byArtist"]

        artist_source_list = []
        if "@id" in artist_data:
            artist_source_list = [Source(self.SOURCE_TYPE, _parse_artist_url(artist_data["@id"]))]


        source_list: List[Source] = [source]
        if "mainEntityOfPage" in data or "@id" in data:
            source_list.append(Source(self.SOURCE_TYPE, data.get("mainEntityOfPage", data["@id"])))

        album = Album(
            title=data["name"].strip(),
            source_list=source_list,
            date=ID3Timestamp.strptime(data["datePublished"], "%d %b %Y %H:%M:%S %Z"),
            artist_list=[Artist(
                name=artist_data["name"].strip(),
                source_list=artist_source_list
            )]
        )

        artwork: ArtworkCollection = ArtworkCollection()

        def _get_artwork_url(_data: dict) -> Optional[str]:
            if "image" in _data:
                return _data["image"]
            for _property in _data.get("additionalProperty", []):
                if _property.get("name") == "art_id":
                    return f"https://f4.bcbits.com/img/a{_property.get('value')}_2.jpg"

        _artwork_url = _get_artwork_url(data)
        if _artwork_url is not None:
            artwork.add_data(url=_artwork_url, width=350, height=350)
        else:
            for album_release in data.get("albumRelease", []):
                _artwork_url = _get_artwork_url(album_release)
                if _artwork_url is not None:
                    artwork.add_data(url=_artwork_url, width=350, height=350)
                    break

        for i, track_json in enumerate(data.get("track", {}).get("itemListElement", [])):
            if DEBUG:
                dump_to_file(f"album_track_{i}.json", json.dumps(track_json), is_json=True, exit_after_dump=False)

            try:
                album.song_collection.append(self._parse_track_element(track_json, artwork=artwork))
            except KeyError:
                continue

        album.source_collection.append(source)
        return album

    def _fetch_lyrics(self, soup: BeautifulSoup) -> List[Lyrics]:
        track_lyrics = soup.find("div", {"class": "lyricsText"})
        if track_lyrics:
            return [Lyrics(text=FormattedText(html=track_lyrics.prettify()))]

        return []

    def fetch_song(self, source: Source, stop_at_level: int = 1) -> Song:
        r = self.connection.get(source.url, name=f"song_{urlparse(source.url).netloc.split('.')[0]}_{urlparse(source.url).path.replace('/', '').replace('track', '')}")
        if r is None:
            return Song()

        soup = self.get_soup_from_response(r)

        data_container = soup.find("script", {"type": "application/ld+json"})
        other_data = {}

        other_data_list = soup.select("script[data-tralbum]")
        if len(other_data_list) > 0:
            other_data = json.loads(other_data_list[0]["data-tralbum"])

        dump_to_file("bandcamp_song_data.json", data_container.text, is_json=True, exit_after_dump=False)
        dump_to_file("bandcamp_song_data_other.json", json.dumps(other_data), is_json=True, exit_after_dump=False)
        dump_to_file("bandcamp_song_page.html", r.text, exit_after_dump=False)

        data = json.loads(data_container.text)
        album_data = data["inAlbum"]
        artist_data = data["byArtist"]

        mp3_url = None
        for key, value in other_data.get("trackinfo", [{}])[0].get("file", {"": None}).items():
            mp3_url = value

        source_list: List[Source] = [source]
        if "mainEntityOfPage" in data or "@id" in data:
            source_list.append(Source(self.SOURCE_TYPE, data.get("mainEntityOfPage", data["@id"]), audio_url=mp3_url))

        source_list_album: List[Source] = [source]
        if "@id" in album_data:
            source_list_album.append(Source(self.SOURCE_TYPE, album_data["@id"]))

        source_list_artist: List[Source] = [source]
        if "@id" in artist_data:
            source_list_artist.append(Source(self.SOURCE_TYPE, _parse_artist_url(artist_data["@id"])))

        song = Song(
            title=clean_song_title(data["name"], artist_name=artist_data["name"]),
            source_list=source_list,
            album_list=[Album(
                title=album_data["name"].strip(),
                date=ID3Timestamp.strptime(data["datePublished"], "%d %b %Y %H:%M:%S %Z"),
                source_list=source_list_album
            )],
            artist_list=[Artist(
                name=artist_data["name"].strip(),
                source_list=source_list_artist
            )],
            lyrics_list=self._fetch_lyrics(soup=soup)
        )

        return song

    def download_song_to_target(self, source: Source, target: Target, desc: str = None) -> DownloadResult:
        if source.audio_url is None:
            return DownloadResult(error_message="Couldn't find download link.")
        return self.connection.stream_into(url=source.audio_url, target=target, description=desc)
