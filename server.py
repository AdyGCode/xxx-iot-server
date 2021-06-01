# Project:    xxx-iot-server
# Filename:   server.py
# Location:   ./
# Author:     STUDENT NAME <STUDENT TAFE EMAIL ADDRESS>
# Created:    05/05/21
# Purpose:
#   This file provides the following features, methods and associated
#   supporting code:
#
#   TODO: STUDENT TO DESCRIBE THE PURPOSE OF THIS FILE
#
# Requirements:
#   An MQTT Server to act as a 'broker' to accept messages and pass onto
#   subscribers to the message topic(s).
#   Python 3.6 or later
#
# Required Packages:
#   This project requires the following Python Packages to be installed:
#       paho-mqtt
#       piview (to retrieve Pi information)
#       SQLAlchemy
#       MySQL Connector Python

import paho.mqtt.client as mqtt
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from piview.Host import Host

from DB import Base, db_connect


engine = create_engine(db_connect)
Base.metadata.drop_all(engine)
Base.metadata.create_all(engine)

mqtt_server = "127.0.0.1"
mqtt_port = 1883
mqtt_time_alive = 60

session = sessionmaker(bind=engine)()


def on_connect(client, userdata, flags, rc):
    if rc == 0:
        print("connected OK Returned code=", rc)
    else:
        print("Bad connection Returned code=", rc)


def on_message(client, userdata, message):
    data = dict(
        topic=message.topic,
        payload=message.payload.decode("UTF-8"),
    )
    print(f"{userdata} | {data}")


if __name__ == '__main__':
    #  Get the Pi name, model, revision, serial number and MAC
    sensor_name = Host.name()
    sensor_serial = Host.serial()
    topic = "NMTAFE/IoT"
    client_id = f"{sensor_name}-{sensor_serial}-server"

    client = mqtt.Client(client_id=client_id)
    client.on_connect = on_connect
    client.on_message = on_message

    client.connect(mqtt_server, mqtt_port, mqtt_time_alive)

    client.subscribe(topic)
    client.loop_forever()
