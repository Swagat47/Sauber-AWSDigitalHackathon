from AWSIoTPythonSDK.MQTTLib import AWSIoTMQTTClient
import logging
import time
import os
from sense import sensor_data

host = os.environ['ENDPOINT']
rootCAPath = os.environ['ROOTCA']
certificatePath = os.environ['CERT']
privateKeyPath = os.environ['KEY']
port = False
useWebsocket = True
clientId = 'sensor'


# Port defaults
if useWebsocket and not port:  # When no port override for WebSocket, default to 443
    port = 443
if not useWebsocket and not port:  # When no port override for non-WebSocket, default to 8883
    port = 8883

# Configure logging
logger = logging.getLogger("AWSIoTPythonSDK.core")
logger.setLevel(logging.DEBUG)
streamHandler = logging.StreamHandler()
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
streamHandler.setFormatter(formatter)
logger.addHandler(streamHandler)

# Init AWSIoTMQTTClient
myAWSIoTMQTTClient = None
if useWebsocket:
    myAWSIoTMQTTClient = AWSIoTMQTTClient(clientId, useWebsocket=True)
    myAWSIoTMQTTClient.configureEndpoint(host, port)
    myAWSIoTMQTTClient.configureCredentials(rootCAPath)
else:
    myAWSIoTMQTTClient = AWSIoTMQTTClient(clientId)
    myAWSIoTMQTTClient.configureEndpoint(host, port)
    myAWSIoTMQTTClient.configureCredentials(rootCAPath, privateKeyPath, certificatePath)

# AWSIoTMQTTClient connection configuration
myAWSIoTMQTTClient.configureAutoReconnectBackoffTime(1, 32, 20)
myAWSIoTMQTTClient.configureOfflinePublishQueueing(-1)  # Infinite offline Publish queueing
myAWSIoTMQTTClient.configureDrainingFrequency(2)  # Draining: 2 Hz
myAWSIoTMQTTClient.configureConnectDisconnectTimeout(10)  # 10 sec
myAWSIoTMQTTClient.configureMQTTOperationTimeout(5)  # 5 sec


# Publish to the same topic in a loop forever
while True:
    c, f, humi = sensor_data()
    res = []
    res.append(myAWSIoTMQTTClient.publish("/get", c, 1))
    res.append(myAWSIoTMQTTClient.publish("/get", f, 1))
    res.append(myAWSIoTMQTTClient.publish("/get", humi, 1))
    if False in res:
        print('Failed')
    if False not in res:
        print(f'Temp in C and F is {c}, {f}.\n Humidity is {humi}%')
    time.sleep(2)