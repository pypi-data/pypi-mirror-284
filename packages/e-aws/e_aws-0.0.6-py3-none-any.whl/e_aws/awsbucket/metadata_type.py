class AWSBucketMetaDataType:

    @property
    def content_type(self) -> str:
        """
        Get the content type
        """
        return self._content_type

    @property
    def content_length(self) -> int:
        """
        Get the content length
        """
        return self._content_length

    @property
    def last_modified(self) -> str:
        """
        Get the last modified date
        """
        return self._last_modified

    def __init__(self, content_type: str, content_length: int, last_modified: str):
        self._content_type = content_type
        self._content_length = content_length
        self._last_modified = last_modified

    def __str__(self) -> str:
        return f"content_type: {self.content_type}, content_length: {self.content_length}, last_modified: {self.last_modified}"
