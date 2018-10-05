import paho.mqtt.client as mqtt  # import the client
import time

# Server configuration
broker_address = "localhost"  # Use local Mosquitto/RabbitMQ broker
# broker_address="test.mosquitto.org" # Use external Mosquitto broker
# broker_address="broker.hivemq.com" # Use external HiveMQ broker
broker_port = 1883
client_name = "client1"

# Message configuration
topic = "sensors/#"
publish_topic = "sensors/sensor2/door"
message = "Open"


def on_message(client, userdata, message):
    print("message received ", str(message.payload.decode("utf-8")))
    print("message topic=", message.topic)
    print("message qos=", message.qos)
    print("message retain flag=", message.retain)


def on_log(client, userdata, level, buf):
    print("log: ", buf)


print("creating new instance")
client = mqtt.Client(client_name)  # create new instance
client.on_message = on_message  # attach function to callback
# client.on_log=on_log

print("connecting to broker")
client.connect(broker_address, port=broker_port)  # connect to broker
client.loop_start()  # start the loop

print("Subscribing to topic", topic)
client.subscribe(topic)  # qos=2

time.sleep(100)  # wait
client.loop_stop()  # stop the loop

# -----------------  Test result  -----------------
# Local RabbitMQ: pub/sub with wildcards (FALSE) Note: PUB: yes SUB: false (Unstable)
# Local Mosquitto: pub/sub with wildcards (FALSE) Note: PUB: yes SUB: false (Unstable)
# Remote Mosquitto: pub/sub with wildcards (FALSE) Note: PUB: yes SUB: false (Unstable)
# Remote HiveMQ: pub/sub with wildcards (FALSE) Note: PUB: yes SUB: false (Unstable)
