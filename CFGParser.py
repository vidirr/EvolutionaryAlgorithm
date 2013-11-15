__author__ = 'GSUS'

import configparser

config = configparser.ConfigParser()
config.read('config.ini')
config.sections()

for key in config['CHC']: print(key)
for key in config['TSP']: print(key)