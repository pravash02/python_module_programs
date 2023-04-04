from watchdog.observers import Observer
from watchdog.events import PatternMatchingEventHandler
import os
import ntpath
import shutil
import time
import optparse
from multiprocessing import Queue, Pool
import threading

from watchdog_fileobserver_ex.main import main


def get_inputs():
    parser = optparse.OptionParser()
    parser.add_option('-f', '--file_path', help='Give the network share drive path', dest='file_path')
    parser.add_option('-e', '--extract_type', help=['file', 'sql'], dest='extract_type')
    (opts, args) = parser.parse_args()
    print(f"Arguments Passed: {opts.file_path}, {opts.extract_type}\n")
    try:
        if opts. file_path is None:
            file_path = None
        else:
            file_path = opts.file_path
        if opts.extract_type is None:
            extract_type = None
        else:
            extract_type = opts.extract_type
        path = str(file_path).replace("\\\\\\", "\\")
    except Exception as e:
        print(f"Please check the Arguments")
        raise e
    return path, extract_type


def consume_queue(watchdog_queue):
    print(f"Is Queue empty: {watchdog_queue.empty()}\n")
    while True:
        if not watchdog_queue.empty():
            print(f"Is Queue empty: {watchdog_queue.empty()}")
            pool = Pool()
            pool.apply_async(migration_function, (watchdog_queue.get(), ))
        else:
            time.sleep(1)


def migration_function(get_event):
    print(f"Process started for event: {get_event}")
    dir_path = ntpath.abspath(get_event)
    file_name = ntpath.basename(get_event)
    if len(get_event) > 0:
        print(f"Files created: {get_event}")
        main(dir_path)
        # TODO add logic to mover the files form source to processed directory


class Handler(PatternMatchingEventHandler):
    def __init__(self, queue, extract_type):
        PatternMatchingEventHandler.__init__(self, patterns=['* ‚csv', '*.dat'],
                                             ignore_patterns=[],
                                             ignore_directories=True)
        self.queue = queue
        self.extract_type = extract_type

    def process (self, event):
        self.queue.put(event.src_path)
        print(f"Storing message: {self.queue.qsize()}")
        # logger. info(f"Producer queue: {self queue]")

    def on_created(self, event):
        print(f"Wait while the transfer of the file is finished before processing it")
        file_size = -1
        while file_size != os.path.getsize(event.src_path):
            file_size = os.path. getsize(event.src_path)
            time.sleep(1)

        self.process(event)


if __name__ == '__main__':
    dir_path, extract_type = get_inputs()

    watchdog_queue = Queue()
    print(f"Starting Worker Thread")
    worker = threading.Thread(target=consume_queue, name="Watchdog", args=(watchdog_queue,), daemon=True)
    worker.start()

    print(f"Starting Watchdog Observer\n")
    event_handler = Handler(watchdog_queue, extract_type)
    observer = Observer()
    observer.schedule(event_handler, dir_path, recursive=False)
    observer.start()

    try:
        while True:
            time.sleep(1)
    except Exception as error:
        observer.stop()
        print(f"Error: {str(error)}")
    observer.join()
