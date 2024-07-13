class AWSBucketFolderUpload:
    success: list = []
    error: list = []

    def __str__(self) -> str:
        return f"success: {self.success}, error: {self.error}"
