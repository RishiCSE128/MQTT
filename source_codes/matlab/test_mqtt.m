BROKER_IP="192.168.1.74";
BROKER_PORT=1883;
CLIENT_ID="matlab_client";
INTERVAL=1;
TOPIC="test/matlab";

MQTT_PUBLISHER = mqttclient(BROKER_IP, ...
                      'Port', BROKER_PORT, ...
                      'ClientID',CLIENT_ID);
for i = 1:100
    MESSAGE="message"+str(i);
    publish(MQTT_PUBLISHER,TOPIC,MESSAGE)
    pause(INTERVAL)
end