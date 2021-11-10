#!/usr/bin/python3
import paho.mqtt.client as mqtt

def on_connect(mqttc, obj, flags, rc):
    print("on_connect: rc="+rc)

def on_message(mqttc, obj, msg):
    print("on_message:  " + msg.topic+": "+str(msg.payload))

def on_publish(mqttc, obj, mid):
    print("on_publish:  mid: "+str(mid))

def on_subscribe(mqttc, obj, mid, granted_qos):
    print("on_subscribe:  Subscribed: "+str(mid)+" "+str(granted_qos))

def on_log(mqttc, obj, level, string):
    print("on_log: " + string)

# If you want to use a specific client id, use
# mqttc = mqtt.Client("client-id")
# but note that the client id must be unique on the broker. Leaving the client
# id parameter empty will generate a random id for you.
mqttc = mqtt.Client("ws-pub-001", transport="websockets")
mqttc.on_message = on_message
#mqttc.on_connect = on_connect
mqttc.on_publish = on_publish
mqttc.on_subscribe = on_subscribe
# Uncomment to enable debug messages
#mqttc.on_log = on_log
mqttc.connect("mqtt.e-motion.ai", 3033, 60)
mqttc.publish("helloyou", "go for it" )
