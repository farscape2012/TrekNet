#!/usr/bin/env ruby
#
# Released under the same terms as Sensu (the MIT license); see LICENSE
# for details.
#
# This is the handler to send sensu metrics to kafka message queue,
# which will be consumed by other applications. 
# So the message format is dependant on applications. For instance in graphite: "key value timestamp"
#
# The configuration is in ../handler/kafka-handler.json.
#   The servers like "server1:port1,server2:port2,....."
#   The topic is the kafka topic which this handler will send the messages to.
#
#


require 'rubygems' if RUBY_VERSION < '1.9.0'
require 'sensu-handler'
require 'timeout'
require 'poseidon'

class SensuToKafka < Sensu::Handler
    def handle
        kafka_servers = settings['kafka']['servers'].split(',').map(&:strip)
        kafka_topic   = settings['kafka']['topic']

        producer = Poseidon::Producer.new(kafka_servers, "sensu_kafka_handler")

        @event['check']['output'].each_line do |metric|
            m = metric.split
            puts 'metric : #{m}'
            begin
                timeout(3) do
                    message = Poseidon::MessageToSend.new(kafka_topic, metric)
                    reponse = producer.send_messages([message])
                    if reponse == true
                      puts "kafka-metrics-graphite post ok. message : #{metric}"
                    end
                end
            rescue Timeout::Error
                puts 'kafka-metrics -- timed out while sending metrics'
            rescue => error
                puts "kafka-metrics -- failed to send metrics: #{error}"
            end
        end
    end
end
