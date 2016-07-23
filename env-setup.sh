# TrekNet
#!/bin/bash

sudo add-apt-repository ppa:webupd8team/java && sudo apt-get update && sudo apt-get install oracle-java8-installer python unzip

sudo mkdir /opt/tools/
sudo chown -R ericsson:ericsson /opt/tools/
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

# elasticsearch
wget https://download.elastic.co/elasticsearch/release/org/elasticsearch/distribution/zip/elasticsearch/2.3.4/elasticsearch-2.3.4.zip
unzip elastcisearch-2.3.4.zip

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

rm *.gz*.zip
