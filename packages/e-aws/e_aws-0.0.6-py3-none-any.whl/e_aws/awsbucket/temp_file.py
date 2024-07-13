from tempfile import gettempdir
from io import TextIOWrapper
import uuid
import os


class AWSBucketTempFile:

    @property
    def file_path(self) -> str:
        """
        Get the file path
        """
        return self._file_path

    @property
    def file_name(self) -> str:
        """
        Get the file name
        """
        return self._file_name

    @property
    def temp_dir(self) -> str:
        """
        Get the temporary directory
        """
        return self._temp_dir

    def __init__(self, data: bytes, temp_dir: str, file_name: str = None):
        self._temp_dir = temp_dir or gettempdir()
        self._file_name = file_name or str(uuid.uuid4())
        self._file_path = os.path.join(self.temp_dir, self.file_name)
        with open(self.file_path, 'wb') as fl:
            fl.write(data)
            fl.flush()

    def __enter__(self) -> 'AWSBucketTempFile':
        return self

    def open(self, open_mode: str = None) -> TextIOWrapper:
        """
        Open the file in the specified mode

        Parameters:
            open_mode (str): File open mode
        """
        return open(self.file_path, open_mode or 'rb')

    def __exit__(self, *_):
        os.remove(self.file_path)
