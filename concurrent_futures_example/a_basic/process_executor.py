import time
from concurrent.futures import ProcessPoolExecutor


def wait_on_b():
    time.sleep(5)
    return 5


def wait_on_a():
    time.sleep(6)
    return 6


def run():

    with ProcessPoolExecutor(max_workers=2) as e:
        a = e.submit(wait_on_a)
        b = e.submit(wait_on_b)
        print('Submitting is not blocking')

    print('The context manager blocks until all tasks complete')
    print(f'{a.result()} - {b.result()}')


if __name__ == '__main__':

    start_time = time.time()
    run()
    print(f'Total run time {(time.time() - start_time)} seconds')
    
