import time
import concurrent
from concurrent.futures import ThreadPoolExecutor


def wait_on_b():
    time.sleep(5)
    return 5

def wait_on_a():
    time.sleep(5)
    return 6

def wait_on_c():
    time.sleep(1)
    print('Exception is ignored in the thread executor')

def run():

    start_time = time.time()
    with ThreadPoolExecutor(max_workers=3) as e:
        a = e.submit(wait_on_a)
        b = e.submit(wait_on_b)
        c = e.submit(wait_on_c)
        print('Submitting is not blocking')

    print('The context manager blocks until all tasks complete')
    print(f'{a.result()} - {b.result()} - {c.result()}')
    print(f'Total run time {(time.time() - start_time)} seconds')


    print()
    print('Another test')
    start_time = time.time()
    with ThreadPoolExecutor(max_workers=3) as e:
        futures = []

        futures.append(e.submit(wait_on_a))
        futures.append(e.submit(wait_on_b))
        futures.append(e.submit(wait_on_c))

        for future in concurrent.futures.as_completed(futures):
            print(future.result())
        
    print(f'Total run time {(time.time() - start_time)} seconds')

if __name__ == '__main__':    
    run()

