from setuptools import setup

setup(
    name = 'rat',
    version = '0.1',
    description = 'RAT is an Analysis Tool',
    author = 'Andy Mastbaum',
    author_email = 'mastbaum@hep.upenn.com',
    url = 'http://github.com/mastbaum/pyrat',
    packages = ['rat', 'rat.core', 'rat.generators', 'rat.processors'],
)

