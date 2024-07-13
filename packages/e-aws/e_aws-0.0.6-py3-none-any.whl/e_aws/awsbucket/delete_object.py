class AWSBucketDeletedObject:

    @property
    def key(self) -> str:
        """
        Get the key
        """
        return self.__key

    @property
    def version_id(self) -> str:
        """
        Get the version id
        """
        return self.__version_id

    @property
    def deleted(self) -> bool:
        """
        Get the deleted status
        """
        return self.__deleted

    def __init__(self, key: str, version_id: str = None, deleted: bool = False):
        self.__key = key
        self.__version_id = version_id
        self.__deleted = deleted

    def __str__(self) -> str:
        return f"key: {self.key} version_id: {self.version_id} deleted: {self.deleted}"
