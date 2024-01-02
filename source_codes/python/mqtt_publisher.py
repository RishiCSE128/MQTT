import paho.mqtt.client as mqtt
from random import randrange, uniform
import time
from datetime import datetime

class Publisher:
    def __init__(self, broker_ip:str, broker_port:int, publisher_id:str, keepalive:int=60, ) -> None:
        """Constructs a PAHO MQTT publisher object 

        Args:
            broker_ip (str): IP address or hostname of the broker   
            broker_port (int): port number of the broker 
            publisher_id (str): publisher's id (any)
            keepalive (int, optional): keepalive timer. Defaults to 60.
        """
        # assign object attributes
        self.broker_ip = broker_ip
        self.broker_port = broker_port
        self.publisher_id = publisher_id
        self.keepalive=keepalive

        # create client instance 
        self.client = mqtt.Client(client_id=publisher_id)


    def connect(self) -> bool:
        """
        established connection to the broker 
        """
        try:
            self.client.connect(host=self.broker_ip,
                           port=self.broker_port,
                           keepalive=self.keepalive
                        )
            return True
        except Exception as e:
            print(f'Error: {e}')
            return False

    def publish(self, topic:str, payload:str):
        """Publishes a string type payload with a topic to the broker 

        Args:
            topic (str): topic (format 'topic/sub-topic/sub-sub-topic/')
            payload (str): string/json type 
        """
        self.client.publish(topic=topic, payload=payload)