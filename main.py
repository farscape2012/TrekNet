#!/usr/bin/env python
import os
import sys
import argparse

DIR = os.path.dirname(__file__)
LIB_DIR = os.path.join(DIR, 'lib')
sys.path.append(LIB_DIR)

from config import Cassandra, Titan

#class ConfigTitan(argparse.Action):
#    def __init__(self):
#        print "class A execution"
#class B:
#    def __init__(self, a=1, b=3):
#        print "class B execution: " + str(a+b)


if __name__ == "__main__":
    print sys.argv
    parser = argparse.ArgumentParser(prog='server-config')

    subparser = parser.add_subparsers(help="subcommand", dest='config')
    subparserparam = subparser.add_parser('config', help="config --titan/cassandra/gremlin-server")
    subparserparam.add_argument('-t', '--titan', nargs='?', type=str,
                                                dest='Ctitan',
                                                const='conf/titan-parameter.properties', 
                                                #default='conf/titan-parameter.properties', 
                                                help='config titan with the file in conf/titan-parameter.properties')
    subparserparam.add_argument('-c', '--cassandra', nargs='?', type=str,
                                                dest='Ccassandra',
                                                const='conf/cassandra-parameter.yaml', 
                                                #default='conf/cassandra-parameter.yaml', 
                                                help='config cassandra with the file in conf/cassandra-parameter.yaml')
    subparserparam.add_argument('-g', '--gremlin',  nargs='?', type=str,
                                                dest='Cgremlin',
                                                const='conf/gremlin-server-parameter.yaml', 
                                                #default='conf/gremlin-server-parameter.yaml', 
                                                help='config gremlin server with the file in conf/gremlin-server-parameter.yaml')
    subparserparam = subparser.add_parser('print', help="print --titan/cassandra/gremlin-server")
    subparserparam.add_argument('-t', '--titan',  nargs='?', type=str,
                                                default='conf/titan-parameter.properties', 
                                                help='config titan with the file in conf/titan-parameter.properties')
    args = parser.parse_args()
    print args
    if args.Ctitan:
        print "Titan"
    elif args.Ccassandra:
        print "Cassandra"
    elif args.Cgremlin:
        print "Gremlin"

#### it will take either the first string (like a, m) or string with double -- as dest attribute

#    print "main is executing"
#    cassandra = Cassandra()
#    cassandra.set_seeds_ip("192.168.122.101")
#    cassandra.write_yaml()
#    titan = Titan()
