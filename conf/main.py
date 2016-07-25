#!/usr/bin/env python

import netifaces

CASS_HOME = "/opt/tools/cassandra-2.2.7"

ip = netifaces.ifaddresses('eth0')[2][0]['addr']
