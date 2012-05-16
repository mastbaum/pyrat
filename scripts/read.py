from rat.core.processor import ProcessorBlock
from rat.processors.stats import Count
#from rat.core.file_reader import dsreader

from rat.core import db

db.load_file('./data/count.ratdb')

processors = [
    Count()
]

processor_block = ProcessorBlock(processors)

#for event in dsreader('file.root'):
#    processor_block.event(event)

processor_block.end_run()

