from time import time
import logging
import os
from ..awsresource import AWSResource
from .. import worker
from . import (
    AWSBucketMetaDataType,
    AWSBucketDeletedObject,
    AWSBucketDataList,
    AWSBucketDataFile,
    AWSBucketTempFile,
    AWSBucketFolderUpload
)


class AWSBucket(AWSResource):

    def __init__(self, bucket_name: str, prefix: str = None, access_key_id: str = None, secret_access_key: str = None, region: str = None):
        super().__init__('s3', access_key_id, secret_access_key, region)
        self.bucket_name = bucket_name
        self.prefix = prefix or ''

    def list_objects(self, prefix: str = '', limit: int = 100, start_after_key: str = '') -> any:
        """
        List the objects in the bucket

        Parameters:
            prefix (str): Prefix to filter the objects
            limit (int): Maximum number of items to return, default 100 max 1000
            start_after_key (str): Start after the specified key

        Returns:
            iter[AWSBucketDataList]: List of objects
        """
        new_prefix = os.path.join(self.prefix, prefix or '')
        resp = self.resource.list_objects_v2(
            Bucket=self.bucket_name,
            Prefix=new_prefix,
            MaxKeys=min(0, limit, 1000),
            StartAfter=start_after_key
        )
        if resp['ResponseMetadata']['HTTPStatusCode'] != 200:
            raise FileNotFoundError(
                f"Error listing objects in bucket {self.bucket_name}, prefix {new_prefix}")
        for obj in resp['Contents']:
            if obj['Key'] == new_prefix:
                continue
            yield AWSBucketDataList(obj['Key'], obj['Size'], obj['LastModified'])

    def get_object_metadata(self, key: str) -> AWSBucketMetaDataType:
        """
        Get the metadata of a file

        Parameters:
            key (str): Bucked file path

        Returns:
            AWSBucketMetaDataType: Metadata

        Raises:s
            FileNotFoundError: If the file does not exist
        """
        resp = self.resource.head_object(
            Bucket=self.bucket_name, Key=os.path.join(self.prefix, key))
        if resp['ResponseMetadata']['HTTPStatusCode'] == 200:
            return AWSBucketMetaDataType(resp['ContentType'], resp['ContentLength'], resp['LastModified'])
        raise FileNotFoundError(
            f"File '{key}' does not exist in bucket '{self.bucket_name}'")

    def get_object(self, key: str) -> AWSBucketDataFile:
        """
        Get the files in bytes

        Parameters:
            key (str): Bucked file path

        Raises:
            FileNotFoundError: If the file does not exist
        """
        key = os.path.join(self.prefix, key)
        resp = self.resource.get_object(Bucket=self.bucket_name, Key=key)
        if resp['ResponseMetadata']['HTTPStatusCode'] == 200:
            return AWSBucketDataFile(resp['Body'].read(), resp['ContentType'], resp['ContentLength'], resp['LastModified'])
        raise FileNotFoundError(
            f"Error getting object from bucket {self.bucket_name} with key {key}")

    def get_object_bytes(self, key: str) -> bytes:
        """
        Get the files in bytes

        Parameters:
            key (str): Bucked file path

        Raises:
            FileNotFoundError: If the file does not exist
        """
        return self.get_object(key).data_bytes

    def put_object(self, file_bytes: bytes, key: str) -> None:
        """
        Put a file in bytes

        Parameters:
            file_bytes: bytes
            key (str): Bucked file path
        """
        logging.info(f"Uploading {key} :: {len(file_bytes)} bytes")
        tm = time()
        self.resource.put_object(
            Body=file_bytes, Bucket=self.bucket_name, Key=os.path.join(self.prefix, key))
        logging.info(f"Uploaded {key} ::: {round(time() - tm, 2)} secs")
    
    async def put_objects(self, objects: list[tuple[bytes, str]], max_parallel_uploads = 10) -> None:
        """
        Put multiple file in bytes

        Parameters:
            objects (list | iter[tuple[bytes, str]]): list of files
            max_parallel_uploads (int): The maximum number of parallel uploads

        Returns:
            None
        """
        tm = time()
        await worker.run(objects, self.put_object, max_parallel_uploads)
        logging.info(f"Uploaded {len(objects)} files ::: {round(time() - tm, 2)} secs")

    def open_temp(self, key: str, temp_dir: str = None, file_name: str = None) -> AWSBucketTempFile:
        """
        Save the file locally and delete it when closed

        Parameters:
            key (str): Bucked file path
            temp_dir (str): Local temp  folder path
            file_name (str): Local file name
        """
        data_arr = self.get_object_bytes(key)
        return AWSBucketTempFile(data_arr, temp_dir=temp_dir, file_name=file_name)

    def download(self, key: str, output_file_path: str) -> None:
        """
        Download a file

        Parameters:
            key (str): Bucked file path
            output_file_path (str): Local file path
        """
        key = os.path.join(self.prefix, key)
        logging.info(f"Downloading {key} to {output_file_path}")
        with open(output_file_path, 'wb') as fl:
            self.resource.download_fileobj(self.bucket_name, key, fl)
        logging.info(f"Downloaded {key} to {output_file_path}")

    async def download_files(self, dst_folder: str, keys: list[str], max_parallel_downloads: int = 10) -> None:
        """
        Download multiple files

        Parameters:
            dst_folder (str): Local folder path
            files (list[str]): list of files
            max_parallel_downloads (int): The maximum number of parallel downloads
        """

        def __generate_job():
            for key in keys:
                yield key, os.path.join(dst_folder, os.path.basename(key))

        await worker.run(
            __generate_job(), self.download, max_parallel_downloads
        )

    def upload(self, file_path: str, key: str) -> None:
        """
        Upload a file

        Parameters:
            file_path (str): Local file path
            key (str): Bucked file path

        Returns:
            None
        """
        tm = time()
        logging.info(f"Uploading {file_path}")
        self.resource.upload_file(file_path, self.bucket_name, os.path.join(self.prefix, key))
        logging.info(f"Uploaded {file_path} ::: {round(time() - tm, 2)} secs")

    def exists(self, key: str) -> bool:
        """
        If a file exists

        Returns:
            bool: True if exists
        """
        try:
            self.get_object_metadata(key)
            return True
        except Exception:
            return False

    async def upload_files(self, paths: list[tuple[str, str]], re_write: bool = False, max_parallel_uploads: int = 10) -> AWSBucketFolderUpload:
        """
        Upload multiple files

        Parameters:
            paths (list[tuple[str, str]]): list of files
            re_write (bool): If True, overwrite existing files
            max_parallel_uploads (int): The maximum number of parallel uploads

        Returns:
            AWSBucketFolderUpload: The result of the upload
        """
        result = AWSBucketFolderUpload()

        def __generate_job():
            for npath, dst_filepath in paths:
                if re_write or not self.exists(dst_filepath):
                    logging.warning(f"Uploading {npath} :: {dst_filepath}")
                    yield npath, dst_filepath
                else:
                    logging.warning(f"{npath} already exists in AWS :: {dst_filepath}")

        def __upload_file(npath, dst_filepath):
            try:
                self.upload(npath, dst_filepath)
            except Exception:
                result.error.append(dst_filepath)
            else:
                result.success.append(dst_filepath)

        await worker.run(
            __generate_job(), __upload_file, max_parallel_uploads
        )
        return result

    async def upload_folder(self, local_path_folder: str, dst_prefix: str, re_write: bool = False, max_parallel_uploads: int = 10) -> AWSBucketFolderUpload:
        """
        Upload all file from a folder

        Parameters:
            local_path_folder (str): Local folder path
            dst_prefix (str): Bucket folder path
            re_write (bool): If True, overwrite existing files

        Returns:
            AWSBucketFolderUpload: The result of the upload
        """

        def __generate_job(root_folder: str, cloud_folder: str):
            logging.info(f"Exploring {root_folder}")
            for name in os.listdir(root_folder):
                npath = os.path.join(root_folder, name)
                if os.path.isfile(npath):
                    dst_filepath = os.path.join(cloud_folder, name)
                    yield npath, dst_filepath
                else:
                    yield from __generate_job(npath, os.path.join(cloud_folder, name))

        return await self.upload_files(
            __generate_job(local_path_folder, dst_prefix), re_write, max_parallel_uploads
        )

    def delete_objects(self, keys: list[str]) -> list[AWSBucketDeletedObject]:
        """
        Delete multiple files

        Parameters:
            keys (list[str]): list of files

        Returns:
            None
        """
        resp = self.resource.delete_objects(
            Bucket=self.bucket_name,
            Delete={
                'Objects': [
                    {'Key': os.path.join(self.prefix, key)}
                    for key in keys
                ]
            }
        )
        return [
            AWSBucketDeletedObject(
                key=obj['Key'],
                version_id=obj.get('VersionId'),
                deleted=obj.get('DeleteMarker', False)
            )
            for obj in resp['Deleted']
        ]


if __name__ == '__main__':
    logging.getLogger().setLevel(logging.INFO)
    AWSBucket('test').exists('test.txt')
