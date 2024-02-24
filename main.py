import sys
from Adafruit_IO import MQTTClient
import time
import random
from simple_ai import *
from uart import *
AIO_FEED_IDs = ["nutnhan1", "nutnhan2"];
AIO_USERNAME = "NamNguyenVan"
AIO_KEY = "aio_rkOi74VhAAn7qlizbWpLTZA217LP"

def connected(client):
    print("Ket noi thanh cong ...")
    for topic in AIO_FEED_IDs:
        client.subscribe(topic)

def subscribe(client , userdata , mid , granted_qos):
    print("Subscribe thanh cong ...")

def disconnected(client):
    print("Ngat ket noi ...")
    sys.exit (1)

def message(client , feed_id , payload):
    print("Nhan du lieu: " + payload + ", feed_id: " + feed_id)

client = MQTTClient(AIO_USERNAME , AIO_KEY)
client.on_connect = connected
client.on_disconnect = disconnected
client.on_message = message
client.on_subscribe = subscribe
client.connect()
client.loop_background()
counter = 10
counter_ai = 5
while True:
    counter = counter - 1
    counter_ai = counter_ai - 1
    if counter_ai <= 0:
        counter_ai = 5
        ai_result = image_detector()
        print("AI Ouput: ", ai_result)
        client.publish("ai",ai_result)
    if counter <= 0:
        print("Random data is publishing")
        temp = random.randint(10,40)
        client.publish("cambien1", temp)
        humi = random.randint(40,80)
        client.publish("cambien2", humi)
        light = random.randint(0,500)
        client.publish("cambien3", light)
    readSerial(client)
    time.sleep(1)   