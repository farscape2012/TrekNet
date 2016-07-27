#!/usr/bin/env python
import os
import sys
DIR = os.path.dirname(__file__)
LIB_DIR = os.path.join(DIR, 'lib')
sys.path.append(LIB_DIR)

from config import Cassandra, Titan

if __name__ == "__main__":
    print "main is executing"
    cassandra = Cassandra()
    cassandra.set_seeds_ip("192.168.122.101")
    cassandra.write_yaml()
    titan = Titan()
