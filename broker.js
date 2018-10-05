// https://github.com/mqttjs/MQTT.js

var mqtt = require('mqtt');

// Server configuration
// var server_url = 'mqtt://test.mosquitto.org'; // Use external Mosquitto broker
var server_url = 'mqtt://localhost:1883'; // Use local Mosquitto/RabbitMQ broker
// var server_url = 'mqtt://broker.hivemq.com'; // Use external HiveMQ broker

// Message configuration
var topic = 'sensors/#';
var publish_topic = "sensors/sensor2/door";
var message = "Open";

var client = mqtt.connect(server_url);

client.on('connect', function () {
  console.log("Connected to: " + server_url);

  client.subscribe(topic, function (err) {
    if (!err) {
      // Publish example
      client.publish(publish_topic, message);
    }
  })
});

client.on('message', function (_topic, _message) {
  console.log("Topic: " + _topic + " - message: " + _message.toString());
  //client.end();
});

// -----------------  Test result  -----------------
// Local RabbitMQ: pub/sub with wildcards (TRUE)
// Local Mosquitto: pub/sub with wildcards (TRUE)
// Remote Mosquitto: pub/sub with wildcards (TRUE)
// Remote HiveMQ: pub/sub with wildcards (TRUE)