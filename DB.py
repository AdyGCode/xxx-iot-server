# --------------------------------------------------------------
# File:     /DB.py
# Project:  xxx-iot-server
# Author:   STUDENT NAME <STUDENT@EMAIL-ADDRESS>
# Created:  5/05/2021
# Purpose:  ...
#
# --------------------------------------------------------------

import urllib.parse

from sqlalchemy import BigInteger, Boolean, Column, DateTime, Float, func, \
    Integer, String, Text
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

# TODO: Make sure that you have installed MariaDB Server (See README.MD)

# TODO: Before making any changes to this file, read it all carefully

# Define the database connection details
db_server = "localhost"
db_port = 3306
db_username = "xxx_iot"
db_password = "Password1"
db_database = "xxx_iot"
db_engine = "mysql+mysqlconnector"

# Create a SQL safe password by escaping any special characters
db_safe_pw = urllib.parse.quote_plus(db_password)
# Create the database connection string
db_connect = f"{db_engine}://{db_username}:{db_safe_pw}@{db_server}" \
             f"/{db_database}"


class Sensehat_TPH(Base):
    """
    TODO: Add a description to this class

    TODO: Before working on the Environment class, check and complete the
          sensor class as it has lots of examples.
    """
    __tablename__ = "iot_sensehat_tph"
    id = Column(BigInteger, primary_key=True, autoincrement=True)
    # TODO: Add defaults for all the fields (see list above)
    topic = Column(String(255), default="ERROR")
    client = Column(String(255), default="ERROR")
    data = Column(Text, default="ERROR")
    # TODO: Add temperature column (float)
    # TODO: Add pressure column (float)
    # TODO: Add humidity column (float)
    # TODO: Add acceleration columns (X,Y,Z) in Gs (X given as an example)
    acceleration_x = Column(Float, default=0.0)
    # TODO: Add compass (North) direction in degrees column (Small Integer?)
    recorded_at = Column(DateTime, default="1000-01-01 00:00:00")
    created_at = Column(DateTime, server_default=func.now())

    def __init__(self):
        pass

    def __str__(self):
        return_string = f"{self.id:>6x} {self.topic}" \
                        f"{self.client} {self.data}"
        return return_string


class Sensor(Base):
    """
    Sensor Table Class

    Used to provide the table structure to SQLAlchemy for it to automatically
    create the table on first run of the server.

    This table stores each individual item of data from the sensor.
    """
    __tablename__ = "iot_sensors"
    id = Column(BigInteger, primary_key=True, autoincrement=True)
    # TODO: Add defaults of the correct type for all the fields
    #       Some sample defaults have been added
    topic = Column(String(255), default="ERROR")
    client = Column(String(255), default="ERROR")
    data = Column(Text, default="ERROR")
    # TODO: Add a default of UNKNOWN to the sensor name
    sensor_name = Column(String(64))
    message = Column(Text, default=None)
    # TODO: Add a default of UNKNOWN to the model
    model = Column(String(128))
    # TODO: Add a default of 999.999.999.999 to the ip
    ip = Column(String(32))
    # TODO: Add a default of zz:zz:zz:zz:zz:zz to the mac
    mac = Column(String(32))
    # TODO: Add a default of 1000-01-01 00:00:00 to boot time
    boot_time = Column(DateTime)
    # TODO: Set a default of 0 for the RAM
    ram_total = Column(Integer)
    # TODO: Set a default of 0 for the RAM Free
    ram_free = Column(Integer)
    # TODO: Set a default of 0 for the storage
    storage_total = Column(BigInteger)
    # TODO: Set a default of 0 for the storage total
    storage_free = Column(BigInteger)
    # TODO: Set a default of False for the i2c, bt, camera and spi
    hw_i2c = Column(Boolean)
    hw_bt = Column(Boolean)
    hw_camera_support = Column(Boolean)
    hw_camera_detected = Column(Boolean)
    hw_spi = Column(Boolean)
    recorded_at = Column(DateTime, default="1000-01-01 00:00:00")
    created_at = Column(DateTime, server_default=func.now())

    def __init__(self):
        pass

    def __str__(self):
        return_string = f"{self.id:>6x} {self.topic}" \
                        f"{self.client} {self.data}"
        return return_string
