'''Facilities for logging to files and output streams.'''

import logging
import os
import socket

hostname = socket.gethostname()
pid = str(os.getpid())

filename = '.'.join(['rat', hostname, pid, 'log'])

logging.basicConfig(filename=filename, level=logging.INFO)

