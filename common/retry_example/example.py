import time


def dangerous_function(i):
    success_when_and_after = 4

    if i < success_when_and_after:
        raise Exception(f'Failed at attempt No. {i}')

    return f'Success at attempt No. {i}'


def run():

    max_no_of_attempts, wait_time_base_in_second = 4, 2
    attempt_count = 0
    while True:
        attempt_count += 1

        try:
            result = dangerous_function(attempt_count)
            break
        except Exception:
            if attempt_count < max_no_of_attempts:
                delay = wait_time_base_in_second ** attempt_count
                print(
                    f'Attempt No. {attempt_count} failed, will retry after {delay} seconds')
                time.sleep(delay)
                continue

            raise

    print(result)


if __name__ == '__main__':
    run()
