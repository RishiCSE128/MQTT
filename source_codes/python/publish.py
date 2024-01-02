from mqtt_publisher import Publisher
from datetime import datetime
import time
from random import uniform
import json

#----------------------------- CONFIG VARS -----------------------------
BROKER_IP = '192.168.1.74'
BROKER_PORT = 1883
PUBLISHER_ID = 'pub1' 
TOPIC='test/test1'    # topic 
PUBLISH_INTERVAL=1    # in sec
#-----------------------------------------------------------------------

def gen_dummy_data(low:float, high:float):
    """generate random data between LOW and HIGH from Uniform distribution

    Args:
        low (float): lower bound
        high (float): upper bound

    Returns:
        _type_: JSON string Format: {t_stamp: timestamp, data: random_value}
    """
    data = {
        't_stamp': str(datetime.now()),
        'data': uniform(low,high)
    }
    return json.dumps(data)

def publish_loop(interval:int):
    """Loops forever publishing in a given INTERVAL

    Args:
        interval (int): publish interval
    """
    publisher = Publisher(broker_ip=BROKER_IP,
                          broker_port=BROKER_PORT,
                          publisher_id=PUBLISHER_ID,
                          keepalive=60
                          )
    
    if publisher.connect():  # publisher establishes comm to broker 
        while True:          # loop forever
            try:
                '''
                add your code here for custom payload
                '''
                payload = gen_dummy_data(low=10.0, high=20.0)  # generate random paylaod
                

                '''
                end of code 
                '''
                publisher.publish(topic=TOPIC,
                                payload=payload)
                
                print(f'[{datetime.now()}] \t payload sent : {payload}]') # print status 

                time.sleep(interval)  # sleep      
            except KeyboardInterrupt:   
                print('Publisher stopped by user !')
                break
    else:
        print('Connection Error !')
        return 0
    
if __name__ == '__main__':
    publish_loop(interval=PUBLISH_INTERVAL)