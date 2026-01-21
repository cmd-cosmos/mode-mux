#pylint: skip-file

import time
import argparse

parser = argparse.ArgumentParser()

parser.add_argument("-f", "--fun",   action="store_true", help="run fun mode")
parser.add_argument("-s", "--study", action="store_true", help="run study mode")
parser.add_argument("-w", "--work",  action="store_true", help="run work mode")

args = parser.parse_args()
