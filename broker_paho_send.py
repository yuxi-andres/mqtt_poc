import paho.mqtt.client as mqtt  # import the client1

# Server configuration
broker_address = "localhost"  # Use local Mosquitto/RabbitMQ broker
# broker_address="test.mosquitto.org" # Use external Mosquitto broker
# broker_address="broker.hivemq.com" # Use external HiveMQ broker
broker_port = 1883
client_name = "client1"

# Message configuration
publish_topic = "sensors/sensor2/door"
message = "Open"

client = mqtt.Client(client_name)  # create new instance

client.connect(broker_address, port=broker_port)  # connect to broker
client.publish(publish_topic, message)  # publish
