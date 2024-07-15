from __future__ import annotations

from copy import copy
from dataclasses import dataclass, field
from functools import cached_property
from typing import Dict, List, Optional, Set, Tuple, Type, TypedDict, Union

from ..connection import Connection
from ..utils import create_dataclass_instance, custom_hash
from ..utils.config import main_settings
from ..utils.enums import PictureType
from ..utils.string_processing import hash_url, unify
from .collection import Collection
from .metadata import ID3Timestamp
from .metadata import Mapping as id3Mapping
from .metadata import Metadata
from .parents import OuterProxy as Base
from .target import Target
from PIL import Image

import imagehash

artwork_connection: Connection = Connection(module="artwork")


@dataclass
class ArtworkVariant:
    url: str
    width: Optional[int] = None
    heigth: Optional[int] = None
    image_format: Optional[str] = None

    def __hash__(self) -> int:
        return custom_hash(self.url)

    def __eq__(self, other: ArtworkVariant) -> bool:
        return hash(self) == hash(other)

    def __contains__(self, other: str) -> bool:
        return custom_hash(other) == hash(self.url)

    def __merge__(self, other: ArtworkVariant) -> None:
        for key, value in other.__dict__.items():
            if value is None:
                continue

            if getattr(self, key) is None:
                setattr(self, key, value)

    @cached_property
    def target(self) -> Target:
        return Target.temp()

    def fetch(self) -> None:
        global artwork_connection

        r = artwork_connection.get(self.url, name=hash_url(self.url))
        if r is None:
            return

        self.target.raw_content = r.content

@dataclass
class Artwork:
    variants: List[ArtworkVariant] = field(default_factory=list)

    artwork_type: PictureType = PictureType.OTHER

    def search_variant(self, url: str) -> Optional[ArtworkVariant]:
        if url is None: 
            return None

        for variant in self.variants:
            if url in variant:
                return variant

        return None

    def __contains__(self, other: str) -> bool:
        return self.search_variant(other) is not None

    def add_data(self, **kwargs) -> None:
        variant = self.search_variant(kwargs.get("url"))

        if variant is None:
            variant, kwargs = create_dataclass_instance(ArtworkVariant, kwargs)
            self.variants.append(variant)

        variant.__dict__.update(kwargs)

    @property
    def url(self) -> Optional[str]:
        if len(self.variants) <= 0:
            return None
        return self.variants[0].url

    def fetch(self) -> None:
        for variant in self.variants:
            variant.fetch()


class ArtworkCollection:
    """
    Stores all the images/artworks for one data object.
    
    There could be duplicates before calling ArtworkCollection.compile()  
    _this is called before one object is downloaded automatically._
    """

    artwork_type: PictureType = PictureType.OTHER

    def __init__(
        self, 
        *data: List[Artwork], 
        parent_artworks: Set[ArtworkCollection] = None, 
        crop_images: bool = True,
    ) -> None:
        # this is used for the song artwork, to fall back to the song artwork
        self.parent_artworks: Set[ArtworkCollection] = parent_artworks or set()
        self.crop_images: bool = crop_images
        
        self._data = []
        self.extend(data)

    def search_artwork(self, url: str) -> Optional[ArtworkVariant]:
        for artwork in self._data:
            if url in artwork:
                return artwork

        return None
    
    def __contains__(self, other: str) -> bool:
        return self.search_artwork(other) is not None

    def _create_new_artwork(self, **kwargs) -> Tuple[Artwork, dict]:
        kwargs["artwork_type"] = kwargs.get("artwork_type", self.artwork_type)

        return create_dataclass_instance(Artwork, dict(**kwargs))

    def add_data(self, url: str, **kwargs) -> Artwork:
        kwargs["url"] = url

        artwork = self.search_artwork(url)

        if artwork is None:
            artwork, kwargs = self._create_new_artwork(**kwargs)
            self._data.append(artwork)

        artwork.add_data(**kwargs)
        return artwork

    def append(self, value: Union[Artwork, ArtworkVariant, dict], **kwargs):
        """
        You can append the types Artwork, ArtworkVariant or dict 
        the best option would be to use Artwork and avoid the other options.
        """
        if isinstance(value, dict):
            kwargs.update(value)
            value, kwargs = create_dataclass_instance(ArtworkVariant, kwargs)
        
        if isinstance(value, ArtworkVariant):
            kwargs["variants"] = [value]
            value, kwargs = create_dataclass_instance(Artwork, kwargs)

        if isinstance(value, Artwork):
            self._data.append(value)
            return
    
    def extend(self, values: List[Union[Artwork, ArtworkVariant, dict]], **kwargs):
        for value in values:
            self.append(value, **kwargs)

    def compile(self, **kwargs) -> None:
        """
        This will make the artworks ready for download and delete duplicates.
        """
        artwork_hashes: list = list()
        artwork_urls: list = list()
        for artwork in self._data:
            index = 0
            for artwork_variant in artwork.variants:
                r = artwork_connection.get(
                    url=artwork_variant.url,
                    name=artwork_variant.url,
                )

                if artwork_variant.url in artwork_urls:
                    artwork.variants.pop(index)
                    continue
                artwork_urls.append(artwork_variant.url)

                target: Target = artwork_variant.target
                with target.open("wb") as f:
                    f.write(r.content)

                with Image.open(target.file_path) as img:
                    # https://stackoverflow.com/a/59476938/16804841
                    if img.mode != 'RGB':
                        img = img.convert('RGB')
                    
                    try:
                        image_hash = imagehash.crop_resistant_hash(img)
                    except Exception as e:
                        continue

                    if image_hash in artwork_hashes:
                        artwork.variants.pop(index)
                        target.delete()
                        continue
                    artwork_hashes.append(image_hash)
                    width, height = img.size
                    if width != height:
                        if width > height:
                            img = img.crop((width // 2 - height // 2, 0, width // 2 + height // 2, height))
                        else:
                            img = img.crop((0, height // 2 - width // 2, width, height // 2 + width // 2))

                        # resize the image to the preferred resolution
                        img.thumbnail((main_settings["preferred_artwork_resolution"], main_settings["preferred_artwork_resolution"]))
                        index =+ 1
                    
                    

    def __merge__(self, other: ArtworkCollection, **kwargs) -> None:
        self.parent_artworks.update(other.parent_artworks)
        for other_artwork in other._data:
            for other_variant in other_artwork.variants:
                if self.__contains__(other_variant.url):
                    continue
                self.append(ArtworkVariant(other_variant.url))


    def __hash__(self) -> int:
        return id(self)

    def __iter__(self) -> Generator[Artwork, None, None]:
        yield from self._data

    def get_urls(self) -> Generator[str, None, None]:
        yield from (artwork.url for artwork in self._data if artwork.url is not None)

    
    