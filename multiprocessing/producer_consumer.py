from threading import Thread, Condition
import time
import random

MAX_NUM=10
queue=[]
condition=Condition()


class ProducerThread(Thread):
    def run(self):
        nums = range(5)
        global queue
        while True:
            condition.acquire()
            if len(queue) == MAX_NUM:
                print("Queue is full, producer is waiting")
                condition.wait()
                print("Space in queue, Consumer notified the producer")
            num=random.choice(nums)
            queue.append(num)
            print("Produced ",num)
            condition.notify()
            condition.release()
            time.sleep(random.random())


class ConsumerThread(Thread):
    def run(self):
        global queue
        while True:
            condition.acquire()
            if not queue:
                print("Queue is empty, consumer is waiting")
                condition.wait()
                print("Items in queue, Producer notified the consumer")
            num=queue.pop(0)
            print("Consumed",num)
            condition.notify()
            condition.release()
            time.sleep(random.random())

ProducerThread().start()
ConsumerThread().start()

