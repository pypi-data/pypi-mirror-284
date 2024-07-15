from __future__ import annotations

from dataclasses import dataclass
from enum import Enum
from typing import TYPE_CHECKING, Optional, Type

from mutagen.id3 import PictureType

if TYPE_CHECKING:
    from ...pages.abstract import Page

@dataclass
class SourceType:
    name: str
    homepage: Optional[str] = None
    download_priority: int = 0

    page_type: Type[Page] = None
    page: Page = None

    def register_page(self, page: Page):
        self.page = page

    def __hash__(self):
        return hash(self.name)

    @property
    def has_page(self) -> bool:
        return self.page is not None

    # for backwards compatibility
    @property
    def value(self) -> str:
        return self.name


class ALL_SOURCE_TYPES:
    YOUTUBE = SourceType(name="youtube", homepage="https://music.youtube.com/")
    BANDCAMP = SourceType(name="bandcamp", homepage="https://bandcamp.com/", download_priority=10)
    MUSIFY = SourceType(name="musify", homepage="https://musify.club/", download_priority=7)
    
    GENIUS = SourceType(name="genius", homepage="https://genius.com/")
    MUSICBRAINZ = SourceType(name="musicbrainz", homepage="https://musicbrainz.org/")
    ENCYCLOPAEDIA_METALLUM = SourceType(name="encyclopaedia metallum")
    DEEZER = SourceType(name="deezer", homepage="https://www.deezer.com/")
    SPOTIFY = SourceType(name="spotify", homepage="https://open.spotify.com/")

    # This has nothing to do with audio, but bands can be here
    WIKIPEDIA = SourceType(name="wikipedia", homepage="https://en.wikipedia.org/wiki/Main_Page")
    INSTAGRAM = SourceType(name="instagram", homepage="https://www.instagram.com/")
    FACEBOOK = SourceType(name="facebook", homepage="https://www.facebook.com/")
    TWITTER = SourceType(name="twitter", homepage="https://twitter.com/")
    # Yes somehow this ancient site is linked EVERYWHERE
    MYSPACE = SourceType(name="myspace", homepage="https://myspace.com/")     

    MANUAL = SourceType(name="manual")
    
    PRESET = SourceType(name="preset")


class PictureType(Enum):
    """Enumeration of image types defined by the ID3 standard for the APIC
    frame, but also reused in WMA/FLAC/VorbisComment.

    This is copied from mutagen.id3.PictureType
    """

    OTHER = 0

    FILE_ICON = 1
    """32x32 pixels 'file icon' (PNG only)"""

    OTHER_FILE_ICON = 2
    """Other file icon"""

    COVER_FRONT = 3
    """Cover (front)"""

    COVER_BACK = 4
    """Cover (back)"""

    LEAFLET_PAGE = 5
    """Leaflet page"""

    MEDIA = 6
    """Media (e.g. label side of CD)"""

    LEAD_ARTIST = 7
    """Lead artist/lead performer/soloist"""

    ARTIST = 8
    """Artist/performer"""

    CONDUCTOR = 9
    """Conductor"""

    BAND = 10
    """Band/Orchestra"""

    COMPOSER = 11
    """Composer"""

    LYRICIST = 12
    """Lyricist/text writer"""

    RECORDING_LOCATION = 13
    """Recording Location"""

    DURING_RECORDING = 14
    """During recording"""

    DURING_PERFORMANCE = 15
    """During performance"""

    SCREEN_CAPTURE = 16
    """Movie/video screen capture"""

    FISH = 17
    """A bright colored fish"""

    ILLUSTRATION = 18
    """Illustration"""

    BAND_LOGOTYPE = 19
    """Band/artist logotype"""

    PUBLISHER_LOGOTYPE = 20
    """Publisher/Studio logotype"""
