import threading
import time 

start = time.perf_counter()
def do_something():
    print("Sleeping")
    time.sleep(1.0)
    print("Done sleeping")

# synchronus (normal)
do_something()
do_something()    
time_end = time.perf_counter()
print(f"Total time (no threads): {time_end - start} ")

start = time.perf_counter()
def do_something(thread_name, time_s = 1.0):
    print("Sleeping")
    time.sleep(time_s)
    print(f"Done sleeping for {time_s}")
    print(f"Thread name: {thread_name}")

# traditional threading. (under the hood)
t1 = threading.Thread(target=do_something, args=[1, 1.5])
t2 = threading.Thread(target=do_something, args = [2, 1.0])
t1.start()
t2.start()
t1.join()
t2.join()
time_end = time.perf_counter()
print(f"Total time (threading): {time_end - start} ")

start = time.perf_counter()
def do_something(time_s):
    print("Sleeping")
    time.sleep(time_s)
    print("Done sleeping")
    return time_s

#
# Above method gets out of control pretty fast. Instead use the global pool cuncurrecy module

import concurrent.futures

with concurrent.futures.ThreadPoolExecutor() as executor:
    f1 = executor.submit(do_something, 1)
    # print(f1.result()) - similar to join above

# or using lists
with concurrent.futures.ThreadPoolExecutor() as executor:
    times = [1, 2, 3, 4]
    results = executor.map(do_something, times)
    
    for result in results:
        print(result)


