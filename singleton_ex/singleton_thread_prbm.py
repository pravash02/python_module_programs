import threading
import random


class Singleton():
    def __init__(self):
        self.value = random.randint(1, 10)


def create_singleton_instances():
    s = Singleton()
    print(f"Singleton instance created by thread {threading.current_thread().name}: {s} and value: {s.value}\n")


threads = []
for i in range(5):
    t = threading.Thread(target=create_singleton_instances)
    t.start()
    threads.append(t)

for t in threads:
    t.join()
