from threading import Lock, Thread
lock = Lock()
a = 1

def multiply_one():
   
   global a
   lock.acquire()
   a *= 4
   lock.release()

def multiply_two():
   global a
   lock.acquire()
   a *= 6
   lock.release()

threads = []
for func in [multiply_one, multiply_two]:
   threads.append(Thread(target=func))
   threads[-1].start()

for thread in threads:
 
   thread.join()

print(a)