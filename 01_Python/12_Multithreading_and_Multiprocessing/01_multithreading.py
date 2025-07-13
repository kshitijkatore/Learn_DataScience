## Multithreading

import threading
import time


def print_numbers():
    for i in range(5):
        time.sleep(2)
        print(f"Number :{i}")

def print_letters():
    for letter in 'abcde':
        time.sleep(2)
        print(f"Letter : {letter}")


# Create 2 threads
t1 =threading.Thread(target=print_numbers)
t2 = threading.Thread(target=print_letters)

t = time.time()
## start the thread
t1.start()
t2.start()

## Wait for the thread to complete
t1.join()
t2.join()
finished_time = time.time()-t
print(finished_time)