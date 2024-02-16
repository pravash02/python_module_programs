import threading
import random


class Singleton:
    _instance = None

    def __init__(self):
        self.value = random.randint(1, 10)

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(Singleton, cls).__new__(cls)
        return cls._instance


def create_singleton(index):
    s = Singleton()
    print(f"Singleton instance created by thread {threading.current_thread().name}: {s} and value: {s.value}\n")


# Problem case: Simulating multiple threads creating singleton instances simultaneously
def problem_case():
    threads = []
    for i in range(5):
        thread = threading.Thread(target=create_singleton, args=(i,))
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()


# Solution using locks to ensure thread safety
class ThreadSafeSingleton:
    __instance = None
    __lock = threading.Lock()

    def __init__(self):
        self.value = random.randint(1, 10)

    @classmethod
    def get_instance(cls):
        if not cls.__instance:
            with cls.__lock:
                if not cls.__instance:
                    cls.__instance = cls()
        return cls.__instance


def create_thread_safe_singleton(index):
    s = ThreadSafeSingleton.get_instance()
    print(f"Singleton instance created by thread {threading.current_thread().name}: {s} and value: {s.value}\n")


# Thread-safe case: Simulating multiple threads creating thread-safe singleton instances
def thread_safe_case():
    threads = []
    for i in range(5):
        thread = threading.Thread(target=create_thread_safe_singleton, args=(i,))
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()


if __name__ == "__main__":
    print("Problem case (without thread safety):")
    problem_case()

    print("\nThread-safe case:")
    thread_safe_case()
