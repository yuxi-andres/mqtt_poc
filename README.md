
# MQTT PoC

This repo contains a set of PoCs of how to use MQTT clients in Ruby, Node.js and Python.

In each PoC the MQTT client library is tested with:
- 2 local brokers (RabbitMQ and Mosquitto) using topics with wildcards (# +).
- 2 remote brokers (HiveMQ and Mosquitto) using topics with wildcards (# +).

## MQTT Theory
[MQTT.md](/MQTT.md)

## Local broker installation

 - [Mosquitto](https://mosquitto.org/download/)
 - [RabbitMQ](https://www.rabbitmq.com/getstarted.html)

## Node-Red
This Repo includes an example flow, after install [node-red](https://nodered.org/docs/getting-started/installation), just run it as:

    node-red flow.json

![enter image description here](https://res.cloudinary.com/dmddlrfmw/image/upload/v1539035931/Screen_Shot_2018-10-08_at_4.57.38_PM_j3ldbb.png)

### Description
- There are 2 input nodes who simulate a door sensor (open/close).
- There is 1 MQTT output who publish messages using the topic injected by the inputs.
- There is 1 MQTT input who is subscribed to sensors/# topic.
- There is 1 debug node used to show the messages received by the MQTT input.

### Node-Red MQTT Configuration

The flow included in this repo is able to connect with:
- Flespi io: mqtt.flespi.io:1883 (you must create an account and copy your access token).
- HiveMQ: broker.hivemq.com:1883
- Mosquitto: test.mosquitto.org:1883
- Any local MQTT broker running on port 1883 (RabbitMQ and Mosquitto were tested in this repo).

![enter image description here](https://res.cloudinary.com/dmddlrfmw/image/upload/v1539036251/Screen_Shot_2018-10-08_at_5.03.38_PM_qoydrr.png)

### Node-Red MQTT Video
[Demo](https://res.cloudinary.com/dmddlrfmw/video/upload/v1539102246/mqtt_demo_kqyacq.mov)

## Ruby (https://github.com/njh/ruby-mqtt)

### Configuration
![enter image description here](https://res.cloudinary.com/dmddlrfmw/image/upload/v1539037348/Screen_Shot_2018-10-08_at_5.20.36_PM_wplgny.png)

### Run
    gem install mqtt
    ruby broker.rb

### Notes

TLS/SSL is not enabled by default, to enabled it, pass :ssl => true in MQTT::Client.connect method.

### Test result

- **Local RabbitMQ:** pub/sub with wildcards (TRUE).
- **Local Mosquitto:** pub/sub with wildcards (TRUE).
- **Remote Mosquitto:** pub/sub with wildcards (TRUE).
- **Remote HiveMQ:** pub/sub with wildcards (TRUE).

### Limitations

- [QoS](https://www.hivemq.com/blog/mqtt-essentials-part-6-mqtt-quality-of-service-levels) 2 is not currently supported by client.
- Automatic re-connects to the server are not supported.
- No local persistence for packets.

## Node.js (https://github.com/mqttjs/MQTT.js)

### Configuration
![enter image description here](https://res.cloudinary.com/dmddlrfmw/image/upload/v1539037448/Screen_Shot_2018-10-08_at_5.21.01_PM_wmz7ie.png)

### Run

    npm install mqtt --save
    node broker.js

### Notes

MQTT v5 support is experimental as it has not been implemented by brokers yet.

### Test result

- **Local RabbitMQ:** pub/sub with wildcards (TRUE).
- **Local Mosquitto:** pub/sub with wildcards (TRUE).
- **Remote Mosquitto:** pub/sub with wildcards (TRUE).
- **Remote HiveMQ:** pub/sub with wildcards (TRUE).

## Python Paho (http://www.eclipse.org/paho/clients/python/, https://pypi.org/project/paho-mqtt/)

### Configuration
![enter image description here](https://res.cloudinary.com/dmddlrfmw/image/upload/v1539037563/Screen_Shot_2018-10-08_at_5.25.30_PM_pn2hgt.png)

![enter image description here](https://res.cloudinary.com/dmddlrfmw/image/upload/v1539037563/Screen_Shot_2018-10-08_at_5.25.42_PM_hydrhu.png)

### Run

    pip install paho-mqtt
    python3 broker_paho_receive.py
    python3 broker_paho_send.py

### Test result

- **Local RabbitMQ:** pub/sub with wildcards (FALSE) Note: PUB: yes SUB: false (Unstable, sometimes the subscription doesn't receive messages).
- **Local Mosquitto:** pub/sub with wildcards (FALSE) Note: PUB: yes SUB: false (Unstable, sometimes the subscription doesn't receive messages).
- **Remote Mosquitto:** pub/sub with wildcards (FALSE) Note: PUB: yes SUB: false (Unstable, sometimes the subscription doesn't receive messages).
- **Remote HiveMQ:** pub/sub with wildcards (FALSE) Note: PUB: yes SUB: false (Unstable, sometimes the subscription doesn't receive messages).

## Python Pika (https://www.rabbitmq.com/tutorials/tutorial-one-python.html)

### Configuration
It only need a local instance of RabbitMQ running as default.

### Run

    pip install pika
    python3 broker_pika_receive.py
    python3 broker_pika_send.py

### Test result

This client only works with AMQP protocol and the only server that supports it is RabbitMQ, so, There isn't way to compare.