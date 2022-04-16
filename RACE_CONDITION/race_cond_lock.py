import threading

x = 0 # global variable shared by threads

def increment():
    global x
    x += 1

def thread_task(lock):
    for _ in range(300000): # lock.acquire를 for loop 밖에 선언하고 lock.release를 for loop 밖에 선언해도 가능 하지만 별로 효율적이진 않음
        lock.acquire() # Acquire lock before accessing the shared data
        increment()
        lock.release() # Release lock after finishing the access

def main_task():
    global x
    x = 0

    lock = threading.Lock() # create a lock object

    t1 = threading.Thread(target=thread_task, args=(lock,))
    t2 = threading.Thread(target=thread_task, args=(lock,))

    t1. start()
    t2. start()

    t1.join()
    t2.join()

for i in range(10):
    main_task()
    print('Iteration {0}: x = {1}'.format(i, x))