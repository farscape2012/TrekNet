#!/usr/bin/env python
import os
import sys
DIR = os.path.dirname(__file__)
LIB_DIR = os.path.join(DIR, 'lib')
sys.path.append(LIB_DIR)

from config import Cassandra

if __name__ == "__main__":
    print "main is executing"
    cassandra = Cassandra()
