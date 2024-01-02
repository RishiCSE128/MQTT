import paho.mqtt.client as mqtt
import time

BROKER_IP = '192.168.1.74'
BROKER_PORT = 1883
SUBSCRIBER_ID = 'sub1'
TOPIC='test/matlab'    # topic to subscribe 
SUB_INTERVAL = 1

DATA_BANK='databank.dat'

def on_message(client, userdata, message):
    data=str(message.payload.decode("utf-8"))
    print(f'Received: {data}')

    # Data banking 
    with open(DATA_BANK,'a') as fp:
        fp.write(data+'\n')

try:
    subscriber = mqtt.Client(client_id=SUBSCRIBER_ID)
    subscriber.connect(host=BROKER_IP, port=BROKER_PORT)
    
    print('------------ Subscriber Ready --------------')
    
    subscriber.subscribe(topic=TOPIC)
    subscriber.on_message=on_message  #points to on_message() function
    time.sleep(SUB_INTERVAL) 
    subscriber.loop_forever()

except KeyboardInterrupt:
    print('Subscription terminated by user')

except Exception as e:
    print(str(e))


