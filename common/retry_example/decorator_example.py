import time
from functools import wraps


def retry(max_no_of_attempts=4, wait_time_base_in_second=2):
    # decorator with parameter

    # The name of this function is not important
    def decorator(func):

        @wraps(func)
        def wrapper(*args, **kwargs):
            attempt_count = 0

            while True:
                attempt_count += 1
                try:
                    result = func(*args, **kwargs)
                    return result
                except Exception:
                    if attempt_count < max_no_of_attempts:
                        delay = wait_time_base_in_second ** attempt_count
                        print(
                            f'Attempt No. {attempt_count} failed, will retry after {delay} seconds')
                        time.sleep(delay)
                        continue

                    raise

        return wrapper

    return decorator


class dangerous_class():
    def __init__(self):
        self.success_when_or_after = 4
        self.invoke_count = 0

    @retry()
    def dangerous_function(self):
        self.invoke_count += 1
        if self.invoke_count < self.success_when_or_after:
            raise Exception(f'Failed at attempt No. {self.invoke_count}')

        return f'Success at attempt No. {self.invoke_count}'

    def reset(self):
        self.invoke_count = 0


def run():

    cls = dangerous_class()

    print(cls.dangerous_function())

    cls.reset()
    print(cls.dangerous_function())


if __name__ == '__main__':
    run()
