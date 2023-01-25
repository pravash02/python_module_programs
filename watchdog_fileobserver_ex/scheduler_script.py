from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler, PatternMatchingEventHandler
import shutil
import time
import os
from datetime import datetime
import multiprocessing as mp
from multiprocessing import Queue
import threading
from multiprocessing import Pool
from watchdog_fileobserver_ex.main import main


PROCESSES = mp.cpu_count() - 1
NUMBER_OF_TASKS = 1

def create_directory(file_path=None):
    # Get the current date in the format of 'year-month-day'
    current_date = datetime.now().strftime('%Y-%m-%d')

    # Create a folder with the current date
    folder_path = f'{file_path}/{current_date}'
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)
        return folder_path
    else:
        return folder_path


class MyHandler(PatternMatchingEventHandler):
    def on_created(self, event):
        file_size = -1
        while file_size != os.path.getsize(event.src_path):
            file_size = os.path.getsize(event.src_path)
            print(file_size)
            time.sleep(1)

        dir_path = event.src_path.split('/input_files')
        processed_files = f'{dir_path[0]}/processed_files'

        child_processed_dir = create_directory(file_path=processed_files)

        if event:
            print("file created:{}".format(event.src_path))
            # call function here
            main(file_name=event.src_path)

            file_name = event.src_path.split('/')[-1]
            destination_path = f'{child_processed_dir}/{file_name}'

            shutil.move(event.src_path, destination_path)
            print("file moved:{} to {}".format(event.src_path, destination_path))


def print_func(event):
    time.sleep(5)
    now = datetime.utcnow()
    print("{0} -- Pulling {1} off the queue ...".format(now.strftime("%Y/%m/%d %H:%M:%S"), event.src_path))


def process_load_queue(q):
    """
    This is the worker thread function. It is run as a daemon threads
    that only exit when the main thread ends.
    Args
    ==========
    q:  Queue() object
    """
    while True:
        if not q.empty():
            event = q.get()
            pool = Pool(processes=1)
            pool.apply_async(print_func, (event,))
        else:
            time.sleep(1)


if __name__ == "__main__":
    watchdog_queue = Queue()
    # handling patterns
    event_handler = MyHandler(patterns=["*.csv", "*.pdf"],
                              ignore_patterns=[],
                              ignore_directories=True
                              )

    observer = Observer()
    observer.schedule(event_handler, path='./input_files', recursive=True)
    observer.start()

    worker = threading.Thread(target=process_load_queue, args=(watchdog_queue,))
    worker.setDaemon(True)
    worker.start()

    try:
        while True:
            time.sleep(300)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()
