"""
:parameter: -f /Users/pravashpanigrahi/PycharmProjects/etl_migration_proj/inbound_files -e file
"""

import requests
import databricks.koalas as ks
from watchdog.observers import Observer
from watchdog.events import PatternMatchingEventHandler
import os
from sys import platform
import ntpath
import shutil
import time
import optparse
import multiprocessing
from multiprocessing import Queue, Pool, Manager
import threading
from datetime import datetime

from mobx_ex.main_proc import main
from mobx_ex.common_functions import EventsDict


lock = threading.RLock()

plfm = ''
if platform == 'linux' or platform == 'linux2':
    plfm = 'linux'
elif platform == 'win32' or platform == 'win64':
    plfm = 'windows'
elif platform == 'darwin':
    plfm = 'darwin'


def get_inputs():
    parser = optparse.OptionParser()
    parser.add_option('-f', '--file_path', help='Give the network share drive path', dest='file_path')
    parser.add_option('-e', '--extract_type', help=['file', 'sql'], dest='extract_type')
    (opts, args) = parser.parse_args()
    logger.info(f"Arguments Passed: {opts.file_path}, {opts.extract_type}\n")
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
        logger.error(f"Please check the Arguments")
        raise e
    return path, extract_type


def consume_queue(watchdog_queue, extract_type):
    logger.info(f"Is Queue empty: {watchdog_queue.empty()}\n")
    while True:
        if not watchdog_queue.empty():
            logger.info(f"Is Queue empty: {watchdog_queue.empty()}")
            pool = multiprocessing.Pool()
            pool.apply_async(migration_function, (watchdog_queue.get(), extract_type))
        else:
            time.sleep(1)


def migration_function(get_event, extract_type, event_dict):
    logger.info(f"Process started for event: {get_event}")
    dir_path = ntpath.abspath(get_event)
    file_name = ntpath.basename(get_event)

    # create spark session and pass it as argument to main function

    if len(get_event) > 0:
        updt_event_dict = update_events_dict(event_dict=event_dict, key=file_name, value=get_event)

        try:
            logger.info(f"Starting process for: {get_event}")
            upd_dict = main(file_path=get_event, file_name=file_name, extract_type=extract_type, load_Type=None,
                            event_dict=updt_event_dict)

        except Exception as e:
            raise Exception(str(e))

        else:
            if 'error' in upd_dict[file_name].keys():
                logger.info(f"List of Events: {upd_dict}")
            else:
                logger.info(f"Finished processing for: {get_event}")
                upd_dict = update_events_dict(event_dict=upd_dict, key='status', value='completed', file_name=file_name)

                logger.info(f"List of Events: {upd_dict}")

                logger.info(f"Moving file")
                dest_path = create_directory(file_path=get_event, file_name=file_name, platform=None)
                current_date = datetime.now().strftime('%Y%m%d')
                dest_path = f"{dest_path}/{file_name}_{current_date}"
                # shutil.move(get_event, dest_path)
                logger.info(f"File Moved")


class Handler(PatternMatchingEventHandler):
    def __init__(self, queue, splunk_service, event_dict):
        PatternMatchingEventHandler.__init__(self, patterns=['*.csv', '*.dat'],
                                             ignore_patterns=[],
                                             ignore_directories=True)
        self.queue = queue
        self.splunk_service = splunk_service
        self.event_dict = event_dict

    def process(self, event):
        self.queue.put(event.src_path)
        # logger.info(f"Storing message: {self.queue.qsize()}")

    def on_created(self, event):
        # logger.info(f"Wait while the transfer of the file is finished before processing it")
        # file_size = -1
        # while file_size != os.path.getsize(event.src_path):
        #     file_size = os.path. getsize(event.src_path)
        #     time.sleep(1)

        file = None
        while file is None:
            try:
                file = open(event.src_path)
            except OSError:
                logger.info('Waiting for file transfer')
                time.sleep(5)
                continue

        self.process(event)
        # splunk_logger.info("Inside on_created event")

    def on_modified(self, event):
        pass


def start_watchdog(watchdog_queue, dir_path, splunk_service, event_dict):
    logger.info(f"Starting Watchdog Observer\n")
    event_handler = Handler(watchdog_queue, splunk_service, event_dict)
    observer = Observer()
    observer.schedule(event_handler, dir_path, recursive=False)
    observer.start()

    try:
        while True:
            time.sleep(1)
            print(event_dict)
    except Exception as error:
        observer.stop()
        logger.error(f"Error: {str(error)}")
    observer.join()


if __name__ == '__main__':
    logger.info(f"Running on Platform: {plfm}")
    dir_path, extract_type = get_inputs()

    watchdog_queue = Queue()

    splunk_obj = SplunkConnection(config=None)
    splunk_service = splunk_obj.get_client_conn()

    mp = Manager()
    event_dict = mp.dict()

    logger.info(f"Starting Worker Thread")
    worker = threading.Thread(target=start_watchdog, name="Watchdog",
                              args=(watchdog_queue, dir_path, splunk_service, event_dict), daemon=True)
    worker.start()

    while True:
        if not watchdog_queue.empty():
            logger.info(f"Is Queue empty: {watchdog_queue.empty()}")
            pool = Pool()
            pool.apply_async(migration_function, (watchdog_queue.get(), extract_type, event_dict))
        else:
            time.sleep(1)
