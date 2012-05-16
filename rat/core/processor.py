'''Processor-related classes.'''

class ProcessorAbort(Exception):
    '''When raised by a processor, processing of this event is immediately
    terminated and no further processors are run on this event.
    '''
    def __init__(self, value):
        self.value = value
    def __str__(self):
        return repr(self.value)

class ProcessorFail(Exception):
    '''When raised by a processor, signifies that the processor task failed,
    but later processors are still executed.
    '''
    def __init__(self, value):
        self.value = value
    def __str__(self):
        return repr(self.value)

class Processor:
    '''A processor represents a chunk of analysis code that can be placed in
    the event loop.
    '''
    def __init__(self, name):
        self.name = name
    def event(self, event):
        pass
    def start_run(self):
        pass
    def end_run(self):
        pass

class ProcessorBlock(list):
    '''A processor block is a list of processors which are each called for
    every event.
    '''
    def event(self, ev):
        for processor in self:
            processor.event(ev)
    def start_run(self):
        for processor in self:
            processor.start_run()
    def end_run(self):
        for processor in self:
            processor.end_run()

