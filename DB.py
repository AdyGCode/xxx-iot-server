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

db_server = "localhost"
db_port = 3306
db_username = "xxx_iot"
db_password = "Password1"
db_database = "xxx_iot"
db_engine = "mysql+mysqlconnector"

db_safe_pw = urllib.parse.quote_plus(db_password)
db_connect = f"{db_engine}://{db_username}:{db_safe_pw}@{db_server}" \
             f"/{db_database}"

Base = declarative_base()


class Environment(Base):
    __tablename__ = "iot_data"
    id = Column(BigInteger, primary_key=True, autoincrement=True)
    # TODO: Add defaults for all the fields (see list above)
    topic = Column(String(255), default="ERROR")
    client = Column(String(255), default="ERROR")
    data = Column(Text, default="ERROR")
    # TODO: Add temperature column (float)
    # TODO: Add pressure column (float)
    # TODO: Add humidity column (float)
    # TODO: Add acceleration columns (X,Y,Z) in Gs
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
    __tablename__ = "iot_sensors"
    id = Column(BigInteger, primary_key=True, autoincrement=True)
    # TODO: Add defaults of the correct type for all the fields
    topic = Column(String(255), default="ERROR")
    client = Column(String(255), default="ERROR")
    data = Column(Text, default="ERROR")
    sensor_name = Column(String(64))
    message = Column(String(32))
    model = Column(String(32))
    ip = Column(String(32))
    mac = Column(String(32))
    boot_time = Column(DateTime)
    ram_total = Column(Integer)
    ram_free = Column(Integer)
    storage_total = Column(BigInteger)
    storage_free = Column(BigInteger)
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
