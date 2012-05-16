'''Core functionality of RAT.'''

# singletons shared throughout RAT

# primary database
import ratdb
db = ratdb.DB()

# ROOT with RAT event dictionary (for now!)
#from rootimport import ROOT

# logging to file
import log
debug = log.logging.debug
info = log.logging.info
warn= log.logging.warn
error = log.logging.error
critical = log.logging.critical

# signal handling
import signal_handler
handler = signal_handler.SignalHandler()

