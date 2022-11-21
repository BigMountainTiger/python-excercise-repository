import boto3

class Bucket(object):

    def __init__(self, name:str):
        self._name         = name
        self._s3           = boto3.resource('s3')
        self._bucket       = self._s3.Bucket(name)

    @property
    def name(self):
        return self._name

    @property
    def bucket(self):
        return self._bucket

    def copy_object(self, src_key:str=None, dst_key:str=None) -> str:
        self._bucket.copy({'Bucket': self._name, 'Key': src_key}, dst_key)
        return dst_key

    def move_object(self, src_key:str = None, dst_key:str = None) -> str:
        src_object = self._s3.Object(self._name, src_key)
        dst_object = self._s3.Object(self._name, dst_key)
        dst_object.copy({'Bucket': self._name, 'Key': src_key})
        src_object.delete()

        return dst_key

    def copy(self, src_bucket:str=None, src_key:str=None, dst_key: str = None):
        dst_object = self._s3.Object(self._name, dst_key)
        dst_object.copy({'Bucket': src_bucket, 'Key': src_key})
        return dst_key

    def wait_until_exists(self, key, **kwargs):
        self._s3.Object(self._name, key).wait_until_exists(**kwargs)

    def download_file(self, key:str = None, filename:str=None):
        self._bucket.download_file(key, filename)

    def upload_file(self, filename: str=None, key:str=None):
        self._bucket.upload_file(filename, key)
        return key

    def is_exist(self, key:str=None) -> bool:
        exists = False
        obj_list = list(self._bucket.objects.filter(Prefix=key))

        if any([f.key == key for f in obj_list]):
            exists = True

        return exists