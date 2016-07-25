#!/usr/bin/env python
import yaml


HOME_CASSANDRA = "/opt/tools/casandra-2.2.7"
DIR = os.path.dirname(__file__)
CASSANDRA_TEMPLATE = os.path.join(DIR, '../config/template.yaml')
CASSANDRA_PARAMETER = os.path.join(DIR, '../config/cassandra.yaml')
CASSANDRA_CONFIG = os.path.join(HOME_CASSANDRA, 'config/cassandra.yaml')

class Cassandra(object):
    def read_yaml(file):
        with open(file) as f:
            try:
                data = yaml.load(f)
            except:
                raise
        return data

    def set_yaml(template, parameter):
        templ_kesy = template.keys()
        param_keys = parameter.keys()
        for key in param_keys:
            template[key] = parameter[key]
        return template

    def write_yaml(file, data):
        with open(file, 'w') as f:
            yaml.dump(data, f, allow_unicode=True,default_flow_style=False)
if __name__ == __main__:
    template = read_yaml(CASSANDRA_TEMPLATE)
    parameter = read_yaml(CASSANDRA_PARAMETER)
    config = set_yaml(template, parameter)
    write_yaml(CASSANDRA_CONFIG, config)

