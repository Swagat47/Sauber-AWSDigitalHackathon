#!/usr/bin/env python
from AWSIoTPythonSDK.MQTTLib import AWSIoTMQTTClient
from sense import sensor_data
import json, os, logging, time
from uuid import uuid4

logger = logging.getLogger("AWSIoTPythonSDK.core")
logger.setLevel(logging.DEBUG)
streamHandler = logging.StreamHandler()
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
streamHandler.setFormatter(formatter)
logger.addHandler(streamHandler)

endpoint = os.environ['ENDPOINT']
rootCAPath = os.environ['ROOTCA']
certificatePath = os.environ['CERT']
privateKeyPath = os.environ['KEY']
port = 8883
useWebsocket = False
clientId = "test-" + str(uuid4())
proxy_options = None
signing_region = 'us-east-1'
count = 0
topic = "test/topic"
message = True

myMQTTClient = AWSIoTMQTTClient(clientId) #random key, if another connection using the same key is opened the previous one is auto closed by AWS IOT
myMQTTClient.configureEndpoint(endpoint, port)

myMQTTClient.configureCredentials(rootCAPath, privateKeyPath, certificatePath)

myMQTTClient.configureOfflinePublishQueueing(-1) # Infinite offline Publish queueing
myMQTTClient.configureDrainingFrequency(2) # Draining: 2 Hz
myMQTTClient.configureConnectDisconnectTimeout(10) # 10 sec
myMQTTClient.configureMQTTOperationTimeout(5) # 5 sec
print ('Initiating Realtime Data Transfer From Raspberry Pi...')
myMQTTClient.connect()


while True:
    c, f, h = sensor_data()
    message = c
    message_json = json.dumps(message)
    mqtt_connection.publish(
        topic=topic,
        payload=message_json,
        qos=1)
    time.sleep(2)