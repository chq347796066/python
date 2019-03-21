import _thread
import time


def print_time(threadName, delay):
    print(delay)
    count = 0
    while count < 5:
        time.sleep(delay)
        count += 1
        print("%s: %s" % (threadName, time.ctime(time.time())))



# 创建两个线程
try:
    print("create")
    _thread.start_new_thread(print_time, ("Thread-1", 2))
    _thread.start_new_thread(print_time, ("Thread-2", 4))
except :
    print("error")

while 1:
    pass