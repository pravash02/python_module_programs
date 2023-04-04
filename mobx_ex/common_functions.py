import threading
import time
from mopyx import observable, action, autorun


@observable
class EventsDict:
    def __init__(self):
        self.events = {}

    @action
    def update_events(self, file_path, events):
        self.events[file_path] = events
