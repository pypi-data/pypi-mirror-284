from .metadata_type import AWSBucketMetaDataType


class AWSBucketDataFile(AWSBucketMetaDataType):

    @property
    def data_bytes(self) -> bytes:
        """
        Get the data in bytes
        """
        return self.__data_bytes

    def __init__(self, data: bytes, content_type: str, content_length: int, last_modified: str):
        super().__init__(content_type, content_length, last_modified)
        self.__data_bytes = data
