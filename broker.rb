# https://github.com/njh/ruby-mqtt

require 'rubygems'
require 'mqtt'

# Server configuration
broker_address="localhost" # Use local Mosquitto/RabbitMQ broker
# broker_address="test.mosquitto.org" # Use external Mosquitto broker
# broker_address="broker.hivemq.com" # Use external HiveMQ broker
broker_port=1883

# Message configuration
topic = "sensors/#"
publish_topic = "sensors/sensor2/door"
message = "Open"

# Publish example
MQTT::Client.connect(:host => broker_address, :port => broker_port) do |client|
  puts "Connected to: #{broker_address}:#{broker_port}"
  puts "Publishing on topic: #{publish_topic}"
  client.publish(publish_topic, message)
end

# Subscribe example
MQTT::Client.connect(:host => broker_address, :port => broker_port) do |client|
  puts "Connected to: #{broker_address}:#{broker_port}"
  # If you pass a block to the get method, then it will loop
  client.get(topic) do |topic,message|
    puts "#{topic}: #{message}"
  end
end

# -----------------  Test result  -----------------
# Local RabbitMQ: pub/sub with wildcards (TRUE)
# Local Mosquitto: pub/sub with wildcards (TRUE)
# Remote Mosquitto: pub/sub with wildcards (TRUE)
# Remote HiveMQ: pub/sub with wildcards (TRUE)