# What is MQTT?

MQTT is a machine-to-machine (M2M)/"Internet of Things" connectivity protocol. It was designed as an extremely lightweight publish/subscribe messaging transport. It is useful for connections with remote locations where a small code footprint is required and/or network bandwidth is at a premium.

### Publish/Subscribe

The MQTT protocol is based on the principle of publishing messages and subscribing to topics, or "pub/sub". Multiple clients connect to a broker and subscribe to topics that they are interested in. Clients also connect to the broker and publish messages to topics. The broker and MQTT act as a simple, common interface for everything to connect to. There is no need to configure a topic, publishing on it is enough.

Topics are treated as a hierarchy, using a slash (/) as a separator. This allows a sensible arrangement of common themes to be created, much in the same way as a filesystem.

Clients can receive messages by creating subscriptions. A subscription may be to an explicit topic, in which case only messages to that topic will be received, or it may include wildcards. Two wildcards are available, + or #.

- (+) can be used as a wildcard for a single level of hierarchy.
- (#) can be used as a wildcard for all remaining levels of hierarchy. This means that it must be the final character in a subscription.

### Quality of Service

MQTT defines three levels of Quality of Service (QoS). The QoS defines how hard the broker/client will try to ensure that a message is received. Messages may be sent at any QoS level, and clients may attempt to subscribe to topics at any QoS level.

Higher levels of QoS are more reliable, but involve higher latency and have higher bandwidth requirements.

-   0: The broker/client will deliver the message once, with no confirmation.
-   1: The broker/client will deliver the message at least once, with confirmation required.
-   2: The broker/client will deliver the message exactly once by using a four-step handshake.

### Retained Messages

All messages may be set to be retained. This means that the broker will keep the message even after sending it to all current subscribers. If a new subscription is made that matches the topic of the retained message, then the message will be sent to the client. This is useful as a "last known good" mechanism. If a topic is only updated infrequently, then without a retained message, a newly subscribed client may have to wait a long time to receive an update. With a retained message, the client will receive an instant update.

### Clean session / Durable connections

On connection, a client sets the "clean session" flag, which is sometimes also known as the "clean start" flag. If clean session is set to false, then the connection is treated as durable. This means that when the client disconnects, any subscriptions it has will remain and any subsequent QoS 1 or 2 messages will be stored until it connects again in the future. If clean session is true, then all subscriptions will be removed for the client when it disconnects.

### Wills

When a client connects to a broker, it may inform the broker that it has a will. This is a message that it wishes the broker to send when the client disconnects unexpectedly. The will message has a topic, QoS and retain status just the same as any other message.

## Servers/Brokers

-   [**Flespi**](https://flespi.com/mqtt-broker)**:** is a public and free cloud-based MQTT broker service with declared 3.1, 3.1.1, 5.0 protocols compliance. High-volume targeted architecture, isolated MQTT namespace, WebSockets/SSL support, configurable ACL, commercial and free SLA, managed by HTTP REST API.
-   [**HiveMQ**](http://www.hivemq.com/)**:**  is an MQTT broker which was built from the ground up with maximum scalability and enterprise-ready security in mind. It comes with native web socket support and an open source plugin SDK to extend its functionality or integrate it with other components.
-   [**Mosca**](http://www.mosca.io/)**:** is Node.js based and so requires node.js to be installed. It can also be installed as a node in node-red. It is not very feature rich when compared to mosquitto.
-   [**Mosquitto**](https://mosquitto.org/)**:**  is an Open Source and Lightweight broker written in C. Probably the most popular MQTT broker.
-   [**RabbitMQ**](http://rabbitmq.com/)**:**  is an AMQP message broker.

![enter image description here](https://res.cloudinary.com/dmddlrfmw/image/upload/v1539103209/Screen_Shot_2018-10-01_at_4.37.06_PM_nk2oqh.png)

### Remote Servers Tested

![enter image description here](https://res.cloudinary.com/dmddlrfmw/image/upload/v1539103263/Screen_Shot_2018-10-01_at_5.14.36_PM_t3eau3.png)

## See more

### Dashboards

- [https://github.com/fabaff/mqtt-panel](https://github.com/fabaff/mqtt-panel)
- [https://github.com/jpmens/mqtt-svg-dash](https://github.com/jpmens/mqtt-svg-dash)

### Great Links:

- [https://blog.autsoft.hu/choosing-an-mqtt-broker-for-your-iot-project/](https://blog.autsoft.hu/choosing-an-mqtt-broker-for-your-iot-project/)
- [https://mobilebit.wordpress.com/2013/05/03/rest-is-for-sleeping-mqtt-is-for-mobile/](https://mobilebit.wordpress.com/2013/05/03/rest-is-for-sleeping-mqtt-is-for-mobile/)
- [http://stephendnicholas.com/posts/power-profiling-mqtt-vs-https](http://stephendnicholas.com/posts/power-profiling-mqtt-vs-https)

### More Useful Links:

- [https://github.com/mqtt/mqtt.github.io/wiki](https://github.com/mqtt/mqtt.github.io/wiki)
- [http://docs.oasis-open.org/mqtt/mqtt/v3.1.1/errata01/os/mqtt-v3.1.1-errata01-os-complete.html#_Toc442180919](http://docs.oasis-open.org/mqtt/mqtt/v3.1.1/errata01/os/mqtt-v3.1.1-errata01-os-complete.html#_Toc442180919)
- [http://www.steves-internet-guide.com/mqtt-hosting-brokers-and-servers/](http://www.steves-internet-guide.com/mqtt-hosting-brokers-and-servers/)
- [http://www.steves-internet-guide.com/install-mosca-mqtt-broker-node-red/](http://www.steves-internet-guide.com/install-mosca-mqtt-broker-node-red/)
- [https://github.com/mqtt/mqtt.github.io/wiki/libraries](https://github.com/mqtt/mqtt.github.io/wiki/libraries)
- [https://github.com/njh/ruby-mqtt](https://github.com/njh/ruby-mqtt)
- [https://github.com/mqttjs/MQTT.js](https://github.com/mqttjs/MQTT.js)