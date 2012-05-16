'''Catch UNIX signal sende to the main application by the operating system.'''

import signal

class SignalHandler:
    '''Handle SIGINT gracefully: the first time sets a flags, giving
    processes time to clean up, while the second time terminates immediately.
    '''
    def __init__(self):
        self.sigint_pending = False
        signal.signal(signal.SIGINT, self.handler)

    def handler(self, signum, frame):
        '''Handler function called by `signal` on the first `SIGINT`.'''
        if signum == signal.SIGINT:
            self.sigint()

    def sigint(self):
        '''Called by `handler`. If this is the first Ctrl-C, set the signal
        pending flag and set future `SIGINT`s to actually terminate the
        program.
        '''
        if not self.sigint_pending:
            self.sigint_pending = True
        signal.signal(signal.SIGINT, signal.SIG_DFL)

    def is_term_requested(self):
        '''Returns true if termination has been requested by a `SIGINT` signal.
        '''
        return self.sigint_pending

