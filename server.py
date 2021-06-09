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
#       piview http://piview.readthedocs.io
#       SQLAlchemy
#       MySQL Connector Python

# TODO: ENSURE changed completed in DB.py BEFORE working on this file

# TODO: Import the paho mqtt client as mqtt
from piview.Host import Host
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# TODO: Modify this line to also import the Sensehat_TPH class
from DB import Base, db_connect, Sensor

engine = create_engine(db_connect)

Base.metadata.drop_all(engine, checkfirst=True)
Base.metadata.create_all(engine, checkfirst=True)

mqtt_server = "127.0.0.1"
mqtt_port = 1883
mqtt_time_alive = 60

session = sessionmaker(bind=engine)()

# TODO: Before you go any further you will need to modify the xxx-iot-sensor
#       project's sensor-system.py file by locating the lines:
#       data = json.dumps({
#             'sensor': mqtt_sensor_name,
#       Add the following line before the 'sensor' line:
#         'system': {
#       Locate the lines:
#              'time': str(datetime.datetime.now()),
#           })
#       Between these lines add a } on a line fo its own.
#       Hint -- check the GitHub repository code to see where the lines are

# TODO: The next alteration is to the xxx-iot-sensor project's sensor-tph.py
#       file by pressing enter at the end of the json.dumps line
#           data = json.dumps({
#       and adding a new line with:
#               'sensehat': {
#       before the 'sensor' line.
#       Then locate the 'time' line, go to the end of the line, press ENTER
#       to create a new line and add a }
#       Hint -- check the GitHub repository code to see where the lines are

# TODO: modify the method definition to have details (a named parameter, with a 'default' value)
#       have a value of None
def store_system_data(details):
    # TODO: DO NOT change the IF statement or the assignment statements below
    if details is not None:
        sensor = Sensor()
        sensor.sensor_name = details["sensor"]["sensor"]
        sensor.sensor_model = details["sensor"]['model']
        sensor.sensor_ip = details["sensor"]['ip']
        sensor.sensor_mac = details["sensor"]['mac']
        sensor.boot_time = details["sensor"]['boot-time']
        sensor.ram_free = details["sensor"]['sensor-free-ram']
        sensor.ram_total = details["sensor"]['sensor-total-ram']
        sensor.storage_free = details["sensor"]['sensor-free-storage']
        sensor.storage_total = details["sensor"]['sensor-total-storage']
        sensor.hw_i2c = details["sensor"]['hw-i2c']
        sensor.hw_bt = details["sensor"]['hw-bt']
        sensor.hw_camera = details["sensor"]['hw-camera']
        sensor.hw_spi = details["sensor"]['hw-spi']
        sensor.recorded_at = details["sensor"]['time']
        # Add and commit the sensor data to the database TODO: remove this line
        session.add(sensor)
        session.commit()


def store_sensehat_tph(details=None):
    if details is not None:
        # TODO: Modify the None below to create a new Sensehat_TPH object
        #       See the `sensor = Sensor()` example above
        sensehat_tph = None
        # TODO: set the sensehat_tph.sensor_name to be the value from
        #       details['sensehat']['sensor']
        sensehat_tph.sensor = None
        # TODO: set the sensehat_tph.pressure to the correct value
        # TODO: set the sensehat_tph.humidity to the correct value
        # TODO: set the sensehat_tph.temperature to the correct value
        # TODO: set the sensehat_tph.accelerometer to the correct value
        # TODO: set the sensehat_tph.compass to the correct value
        sensehat_tph.recorded_at = details["sensor"]['time']
        # TODO: add and commit the sensehat_tph data to the database
        # TODO: delete this line and the PASS line below
        pass


def on_connect(client, userdata, flags, rc):
    if rc == 0:
        print("connected OK Returned code=", rc)
    else:
        # TODO: Add error code detail display (error codes 1-5)
        print("Bad connection Returned code=", rc)


def on_message(client, userdata, message):
    data = dict(
        topic=message.topic,
        payload=message.payload.decode("UTF-8"),
    )
    # TODO: Unpack the data into variables
    details = data['payload']
    # TODO: Insert data variables into a new record
    if details != "" and details["sensor"] != "":
        store_system_data()
    # TODO: Add a decision that checks to see if the details are not blank
    #       and the sensor "sensehat" is not blank (similar to the previous lines)
    # TODO:     call the store_sensehat_data method


if __name__ == '__main__':
    #  Get the Pi name, model, revision, serial number and MAC
    server_name = Host.name()
    server_serial = Host.serial()
    
    topic = "NMTAFE/IoT"
    client_id = f"{server_name}-{server_serial}-server"

    client = mqtt.Client(client_id=client_id)
    client.on_connect = on_connect
    client.on_message = on_message

    client.connect(mqtt_server, mqtt_port, mqtt_time_alive)

    client.subscribe(topic)
    client.loop_forever()
