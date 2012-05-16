from rat.core.processor import Processor
from rat.core import *
from rat.core import db

class Count(Processor):
    def __init__(self, interval=None):
        Processor.__init__(self, 'count')
        self.interval = interval
        if self.interval is None:
            try:
                self.interval = db[('count','',0,0)]['interval']
            except AttributeError:
                self.interval = 10
        self.count = 0
    def event(self, ev):
        self.count += 1
        if self.count % self.interval == 0:
            warn('count: ', self.count)

