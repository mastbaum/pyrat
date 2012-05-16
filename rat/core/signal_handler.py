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
        if signum == signal.SIGINT:
            self.sigint()

    def sigint(self):
        if not self.sigint_pending:
            self.sigint_pending = True
        signal.signal(signal.SIGINT, signal.SIG_DFL)

    def is_term_requested(self):
        return self.sigint_pending

