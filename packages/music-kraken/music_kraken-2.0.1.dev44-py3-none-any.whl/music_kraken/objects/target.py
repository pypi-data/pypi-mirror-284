from __future__ import annotations

import logging
import random
from pathlib import Path
from typing import List, Optional, TextIO, Tuple, Union

import requests
from tqdm import tqdm

from ..utils.config import logging_settings, main_settings
from ..utils.shared import HIGHEST_ID
from ..utils.string_processing import fit_to_file_system
from .parents import OuterProxy

LOGGER = logging.getLogger("target")


class Target(OuterProxy):
    """
    create somehow like that
    ```python
    # I know path is pointless, and I will change that (don't worry about backwards compatibility there)
    Target(file="song.mp3", path="~/Music/genre/artist/album")
    ```
    """

    file_path: Path

    _default_factories = {
    }

    @classmethod
    def temp(cls, name: str = None, file_extension: Optional[str] = None) -> P:
        name = name or str(random.randint(0, HIGHEST_ID))
        if file_extension is not None:
            name = f"{name}.{file_extension}"

        return cls(main_settings["temp_directory"] / name)

    # This is automatically generated
    def __init__(self, file_path: Union[Path, str], relative_to_music_dir: bool = False, **kwargs) -> None:
        if not isinstance(file_path, Path):
            file_path = Path(file_path)

        if relative_to_music_dir:
            file_path = Path(main_settings["music_directory"], file_path)

        super().__init__(file_path=fit_to_file_system(file_path), **kwargs)

        self.is_relative_to_music_dir: bool = relative_to_music_dir

    def __repr__(self) -> str:
        return str(self.file_path)

    @property
    def indexing_values(self) -> List[Tuple[str, object]]:
        return [('filepath', self.file_path)]

    @property
    def exists(self) -> bool:
        return self.file_path.is_file()
    
    @property
    def size(self) -> int:
        """
        returns the size the downloaded audio takes up in bytes
        returns 0 if the file doesn't exist
        """
        if not self.exists:
            return 0
        
        return self.file_path.stat().st_size

    def create_path(self):
        self.file_path.parent.mkdir(parents=True, exist_ok=True)

    def copy_content(self, copy_to: Target):
        if not self.exists:
            LOGGER.warning(f"No file exists at: {self.file_path}")
            return

        with open(self.file_path, "rb") as read_from:
            copy_to.create_path()
            with open(copy_to.file_path, "wb") as write_to:
                write_to.write(read_from.read())

    def stream_into(self, r: requests.Response, desc: str = None) -> bool:
        if r is None:
            return False

        self.create_path()

        total_size = int(r.headers.get('content-length'))

        with open(self.file_path, 'wb') as f:
            try:
                """
                https://en.wikipedia.org/wiki/Kilobyte
                > The internationally recommended unit symbol for the kilobyte is kB.
                """
                with tqdm(total=total_size, unit='B', unit_scale=True, unit_divisor=1024, desc=desc) as t:

                    for chunk in r.iter_content(chunk_size=main_settings["chunk_size"]):
                        size = f.write(chunk)
                        t.update(size)
                return True

            except requests.exceptions.Timeout:
                logging_settings["download_logger"].error("Stream timed out.")
                return False

    def open(self, file_mode: str, **kwargs) -> TextIO:
        return self.file_path.open(file_mode, **kwargs)
            
    def delete(self):
        self.file_path.unlink(missing_ok=True)

    def read_bytes(self) -> bytes:
        return self.file_path.read_bytes()

    @property
    def raw_content(self) -> bytes:
        return self.file_path.read_bytes()

    @raw_content.setter
    def raw_content(self, content: bytes):
        self.file_path.write_bytes(content)
