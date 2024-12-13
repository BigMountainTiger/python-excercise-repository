import datetime
import base64
import uuid


class S3ObjectKeyTimeBasedGenerator:
    def __init__(self, prefix, extention):
        self.prefix = prefix
        self.extention = extention

    def generate(self):
        now = datetime.datetime.now(datetime.timezone.utc)

        y = now.strftime('%Y')
        m = now.strftime('%m')
        d = now.strftime('%d')
        h = now.strftime('%H')
        min = now.strftime('%M')
        s = now.strftime('%S')

        uid = base64.urlsafe_b64encode(
            uuid.uuid4().bytes).decode('utf-8').rstrip('=')

        return f'{self.prefix}/year={y}/month={m}/day={d}/hour={h}/{min}{s}-{uid}.{self.extention}'


if __name__ == '__main__':

    generator = S3ObjectKeyTimeBasedGenerator('prefix-1/prefix-2', 'json')
    key = generator.generate()

    print(f'key = {key}')
