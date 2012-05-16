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

    :param name: The name of the processor
    '''
    def __init__(self, name):
        self.name = name
    def event(self, event):
        '''Called for every event.
        
        :param ev: The event
        '''
        pass
    def start_run(self):
        '''Called once at the start of a run.'''
        pass
    def end_run(self):
        '''Called once at the end of a run.'''
        pass

class ProcessorBlock(list):
    '''A processor block is a list of processors which are each called for
    every event.
    '''
    def event(self, ev):
        '''Call the `event` methods of all processors in the block. Called
        once per event.

        :param ev: The event
        '''
        for processor in self:
            processor.event(ev)
    def start_run(self):
        '''Call the `start_run` methods for all processors in the block.
        Called at the start of a run.
        '''
        for processor in self:
            processor.start_run()
    def end_run(self):
        '''Call the `end_run` methods for all processors in the block.
        Called at the end of a run.
        '''
        for processor in self:
            processor.end_run()

