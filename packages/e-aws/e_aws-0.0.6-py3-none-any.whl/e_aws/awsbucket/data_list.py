from mimetypes import MimeTypes
from .metadata_type import AWSBucketMetaDataType


class AWSBucketDataList(AWSBucketMetaDataType):

    @property
    def key(self) -> bytes:
        """
        Get the key
        """
        return self.__key

    def __init__(self, key: str, content_length: int, last_modified: str):
        content_type = next(iter(MimeTypes().guess_type(key)), None)
        super().__init__(content_type, content_length, last_modified)
        self.__key = key

    def __str__(self) -> str:
        return f"key: {self.key}, content_type: {self.content_type}, content_length: {self.content_length}, last_modified: {self.last_modified}"
