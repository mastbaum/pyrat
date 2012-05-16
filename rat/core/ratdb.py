'''Utilties for accessing the database.'''

from rat.core import *
import json

class DBTable(dict):
    '''Holds the contents of a RATDB table in memory.
    
    :param table: `(optional)` Dictionary from which to constuct the table
    '''
    def __init__(self, table={}):
        dict.__init__(self, table)
        self.name = self['name'] if 'name' in self else ''
        self.index = self['index'] if 'index' in self else ''
        self.run_begin = self['run_begin'] if 'run_begin' in self else 0
        self.run_end = self['run_end'] if 'run_end' in self else 0

        self.callbacks = {}

    def is_valid_run(self, run):
        '''Returns true if this table is valid for the specified run.
        
        :param run: Run number to check
        '''
        return run >= self.run_begin and run <= self.run_end

    def set_user(self):
        '''Set this as a user-override table.'''
        self.run_begin = -1
        self.run_end = -1

    def is_user(self):
        '''Returns true if validity range flags this as a user-plane table.'''
        return self.run_begin == -1 and self.run_end == -1

    def set_default(self):
        '''Set this as a default table.'''
        self.run_begin = 0
        self.run_end = 0

    def is_default(self):
        '''Returns true if validity range flags this as a default-plane table.
        '''
        return self.run_begin == 0 and self.run_end == 0

    def register(self, key, callback):
        '''Add a callback function, which will be called when the value of the
        specified key is modified. This may be used to reload database values
        in a processor, for example.

        :param key: Key to watch for changes
        :param callback: Function to call when a change occurs
        '''
        self.callbacks.setdefault(key, []).append(callback)

    def __setitem__(self, key, value):
        '''Set the item and fire any callbacks.'''
        super(DBTable, self).__setitem__(key, value)

        if key in callbacks:
            for callback in callbacks[key]:
                callback(value)

    def save(self, filename):
        '''Save this table to a file.
        
        :param filename: Name of file to write table to
        '''
        with open(filename, 'w') as f:
            f.write(json.dumps(self))

class DB(dict):
    '''RATDB is the database of constants used by RAT for all adjustable
    parameters, including physical properties of materials, detector geometry,
    calibration constants, lookup tables, and control parameters that specify
    how processing should be done.
    '''
    def add_table(self, table, key=None):
        '''Add a `DBTable` to this database.
        
        :param table: The table
        :param key: `(optional)` Key of table. Computed automatically if not provided
        '''
        if key is None:
            key = (table.name, table.index, table.run_begin, table.run_end,)
        if key in self:
            warn('Replacing table', key, 'in database.')
        self[key] = table

    def load_file(self, filename):
        '''Read a table from a file and add it to this DB.

        :param filename: Name of file to read table from
        '''
        with open(filename) as f:
            data = json.loads(f.read())

        if isinstance(data, list):
            for item in data:
                self.add_table(DBTable(item))
        else:
            self.add_table(DBTable(data))

