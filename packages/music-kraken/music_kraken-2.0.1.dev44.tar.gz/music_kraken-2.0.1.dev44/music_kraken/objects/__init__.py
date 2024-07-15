from typing_extensions import TypeVar

from .artwork import ArtworkCollection
from .collection import Collection
from .contact import Contact
from .country import Country
from .formatted_text import FormattedText
from .metadata import ID3Timestamp
from .metadata import Mapping as ID3Mapping
from .metadata import Metadata
from .option import Options
from .parents import OuterProxy
from .song import Album, Artist, Label, Lyrics, Song, Target
from .source import Source, SourceType

DatabaseObject = OuterProxy
