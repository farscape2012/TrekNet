#!/usr/bin/env python
import yaml
import os
import netifaces


DIR = os.path.dirname(__file__)
#HOME_CASSANDRA = "/home/eijmmmp/TrekNet/"
HOME_CASSANDRA = "/opt/tools/cassandra-2.2.7"
CASSANDRA_TEMPLATE = os.path.join(DIR, '../conf/cassandra-template.yaml')
CASSANDRA_PARAMETER = os.path.join(DIR, '../conf/cassandra.yaml')
CASSANDRA_CONFIG = os.path.join(HOME_CASSANDRA, 'conf/cassandra.yaml')

HOME_TITAN = "/opt/tools/titan-1.0.0-hadoop1/"
#HOME_TITAN = "/home/eijmmmp/TrekNet/"
TITAN_TEMPLATE = os.path.join(DIR, '../conf/titan-template.properties')
TITAN_PARAMETER = os.path.join(DIR, '../conf/titan.properties')
TITAN_CONFIG = os.path.join(HOME_TITAN, 'conf/titan.yaml')


class Cassandra(object):
    def __init__(self, template=CASSANDRA_TEMPLATE, parameter=CASSANDRA_PARAMETER, config=CASSANDRA_CONFIG, interface='eth0'):
        self.file_config = config
        self.config = self.read_yaml(template)
        self.parameter = self.read_yaml(parameter)
        self.ip = self.get_host_ip(interface)
        #def _lazy_setting(self):
        self.config = self.set_yaml(self.config, self.parameter)
        self.config = self.set_yaml(self.config, {'listen_address': self.ip})
        self.config = self.set_yaml(self.config, {'rpc_address': self.ip})
        self.set_seeds_ip(self.ip)
        self.enable_trouble_connection(file=os.path.join(HOME_CASSANDRA, 'conf/cassandra-env.sh'))
        self.write_yaml()
    def set_seeds_ip(self, ip):
        self.config['seed_provider'][0]['parameters'][0]['seeds'] = ip
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
    def write_yaml(self):
        with open(self.file_config, 'w') as f:
            yaml.dump(self.config, f, allow_unicode=True,default_flow_style=False)
    def get_host_ip(self, interface='eth0'):
        try:
            return netifaces.ifaddresses(interface)[2][0]['addr']
        except ValueError:
            print "Could not find interface {0}".format(interface)
            return None
    def enable_trouble_connection(self, file):
        lines = []
        with open(file) as infile:
            for line in infile:
                if "JVM_OPTS=\"$JVM_OPTS -Djava.rmi.server.hostname=" in line:
                    line = ("JVM_OPTS=\"$JVM_OPTS -Djava.rmi.server.hostname=" + self.ip + "\"" + "\n")
                lines.append(line)
        with open(file, 'w') as outfile:
            for line in lines:
                outfile.write(line)
class Titan(object):
    def __init__(self):


if __name__ == "__main__":
    cassandra = Cassandra(config="./conf/new.yaml", interface='eth1')


















