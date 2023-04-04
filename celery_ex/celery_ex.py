from celery import Celery
from watchdog.observers import Observer
from watchdog.events import PatternMatchingEventHandler
import psutil
import time
import subprocess

code_dir_to_monitor = "path/celery/dir"
celery_working_dir = code_dir_to_monitor    # happen to be the same. It may be different on your machine
celery_cmdline = 'celery -A celery_ex worker -l INFO'.split(" ")

app = Celery('celery_ex', broker='redis://localhost:6379/0')


class MyHandler(PatternMatchingEventHandler):
    def on_any_event(self, event):
        print("detected change. event = {}".format(event))

        for proc in psutil.process_iter():
            print('proc - ', proc)
            proc_cmdline = self._get_proc_cmdline(proc)
            if not proc_cmdline or len(proc_cmdline) < len(celery_cmdline):
                continue

            is_celery_worker = 'python' in proc_cmdline[0].lower() \
                               and celery_cmdline[0] == proc_cmdline[1] \
                               and celery_cmdline[1] == proc_cmdline[2]
            if not is_celery_worker:
                continue

            proc.kill()
            print("Just killed {} on working dir {}".format(proc_cmdline, proc.cwd()))

        run_worker()

    def _get_proc_cmdline(self, proc):
        try:
            print('proc.cmdline() - ', proc.cmdline())
            return proc.cmdline()
        except Exception as e:
            return []


def run_worker():
    print("Ready to call {} ".format(celery_cmdline))
    # os.chdir(celery_working_dir)  # if the working directory is different
    subprocess.Popen(celery_cmdline)
    print("Done callling {} ".format(celery_cmdline))


if __name__ == "__main__":
    run_worker()

    observer = Observer()
    event_handler = MyHandler(patterns=["*.csv", "*.pdf"],
                              ignore_patterns=[],
                              ignore_directories=True
                              )
    observer.schedule(event_handler, path='./input_files', recursive=True)
    observer.start()

    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()
