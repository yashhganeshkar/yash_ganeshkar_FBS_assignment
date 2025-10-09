
import threading
import time
import random

buffer = []
buffer_size = 5
condition = threading.Condition()

def producer(name):
    global buffer
    while True:
        item = random.randint(1, 100)
        with condition:
            while len(buffer) == buffer_size:
                condition.wait() 
            buffer.append(item)
            print(f"Producer {name} produced: {item}")
            condition.notifyAll() 
        time.sleep(random.uniform(0.5, 1.5))

def consumer(name):
    global buffer
    while True:
        with condition:
            while len(buffer) == 0:
                condition.wait()  
            item = buffer.pop(0)
            print(f"Consumer {name} consumed: {item}")
            condition.notifyAll()  
        time.sleep(random.uniform(0.5, 2))


producers = [threading.Thread(target=producer, args=(i,)) for i in range(2)]
consumers = [threading.Thread(target=consumer, args=(i,)) for i in range(2)]

for p in producers:
    p.daemon = True
    p.start()
for c in consumers:
    c.daemon = True
    c.start()

time.sleep(10)
print("Finished execution")
