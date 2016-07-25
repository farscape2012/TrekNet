#!/usr/bin/env python
import yaml
import os

HOME_CASSANDRA = "/opt/tools/casandra-2.2.7"
DIR = os.path.dirname(__file__)
CASSANDRA_TEMPLATE = os.path.join(DIR, '../conf/template.yaml')
CASSANDRA_PARAMETER = os.path.join(DIR, '../conf/cassandra.yaml')
CASSANDRA_CONFIG = os.path.join(HOME_CASSANDRA, 'conf/cassandra.yaml')

class Cassandra(object):
    def read_yaml(self, file):
        with open(file) as f:
            try:
                data = yaml.load(f)
            except:
                raise
        return data

    def set_yaml(self, template, parameter):
        templ_kesy = template.keys()
        param_keys = parameter.keys()
        for key in param_keys:
            template[key] = parameter[key]
        return template

    def write_yaml(self, file, data):
        with open(file, 'w') as f:
            yaml.dump(data, f, allow_unicode=True,default_flow_style=False)
if __name__ == "__main__":
    cassandra = Cassandra()
    template = cassandra.read_yaml(CASSANDRA_TEMPLATE)
    parameter = cassandra.read_yaml(CASSANDRA_PARAMETER)
    config = cassandra.set_yaml(template, parameter)
    cassandra.write_yaml(CASSANDRA_CONFIG, config)
#listen_address: 192.168.122.238
#rpc_address: 192.168.122.238
