#!/usr/bin/env bash
# author : Chengyu Liu

# Exit immediately if a command exits with a non-zero status.
set -euo pipefail

usage() {
    echo "usage: $0 [--python python2|python3] [OPTIONS] [DIR] [ -- COMMAND [ARGS..] ]"
    echo
    echo "valid options:"
    echo "      -h, --help              Show this message"
    echo "      -c, --clean             clean every setting"
    echo "      -s, --setup             setup environment"
    echo
}
setup() {
    sudo add-apt-repository ppa:webupd8team/java && sudo apt-get update && sudo apt-get install oracle-java8-installer python-dev python-pip unzip build-essential
    sudo pip install --upgrade virtualenv 
    
    sudo mkdir /opt/tools/
    sudo chown -R eric:eric /opt/tools/
    sudo chmod -R 755 /opt/tools/
    cd /opt/tools/
    echo "inside /opt/tools"
    
    # cassandra
    wget http://mirror.netinch.com/pub/apache/cassandra/2.2.7/apache-cassandra-2.2.7-bin.tar.gz 
    tar -xvf *cassandra* 
    mv apache-cassandra-2.2.7 cassandra-2.2.7
    sudo mkdir -p /var/lib/cassandra/data
    sudo mkdir -p /var/lib/cassandra/commitlog
    sudo mkdir -p /var/lib/cassandra/saved_caches
    sudo mkdir -p /var/log/cassandra/
    sudo chown -R eric:eric /var/lib/cassandra/data
    sudo chown -R eric:eric /var/lib/cassandra/commitlog
    sudo chown -R eric:eric /var/lib/cassandra/saved_caches
    sudo chown -R eric:eric /var/log/cassandra/
    sudo chmod -R 755 /var/lib/cassandra/data
    sudo chmod -R 755 /var/lib/cassandra/commitlog
    sudo chmod -R 755 /var/lib/cassandra/saved_caches
    sudo chmod -R 755 /var/log/cassandra/
    
    
    # elasticsearch
    wget https://download.elastic.co/elasticsearch/release/org/elasticsearch/distribution/zip/elasticsearch/2.3.4/elasticsearch-2.3.4.zip
    unzip elasticsearch-2.3.4.zip
    
    # Gremlin server
    wget https://archive.apache.org/dist/incubator/tinkerpop/3.2.0-incubating/apache-gremlin-server-3.2.0-incubating-bin.zip
    unzip apache-gremlin-server-3.2.0-incubating-bin.zip
    mv apache-gremlin-server-3.2.0-incubating gremlin-server-3.2.0
    # Gremlin console
    wget https://archive.apache.org/dist/incubator/tinkerpop/3.2.0-incubating/apache-gremlin-console-3.2.0-incubating-bin.zip
    unzip apache-gremlin-console-3.2.0-incubating-bin.zip
    mv apache-gremlin-console-3.2.0-incubating gremlin-console-3.2.0
    
    # Titan
    wget http://s3.thinkaurelius.com/downloads/titan/titan-1.0.0-hadoop1.zip
    unzip titan-1.0.0-hadoop1.zip
    
    rm *.gz *.zip
    
    # !!!!!!!!!!!!! Open all ports !!!!!!!!!!!!!! 
    # Dangerous!
    sudo iptables -A INPUT -m conntrack --ctstate ESTABLISHED,RELATED -j ACCEPT
    sudo iptables -A OUTPUT -m conntrack --ctstate ESTABLISHED,RELATED -j ACCEPT
    
    sudo sh -c "iptables-save > /etc/iptables.conf"
    echo -e "# Load iptables rules from this file\niptables-restore < /etc/iptables.conf" | sudo tee /etc/rc.local > /dev/null
}
clean() {
    sudo rm -rf /var/lib/cassandra/data/* /var/lib/cassandra/commitlog/* /var/lib/cassandra/saved_caches/* /var/log/cassandra/* 
}
while true; do
    case "$1" in
        -h|--help)
            usage
            exit 0
            ;;
        -c|--clean)
            clean
            exit 0
            ;;
        -s|--setup)
            setup
            exit 0
            ;;
        *)
            usage
            exit 1
            ;;
    esac
done
