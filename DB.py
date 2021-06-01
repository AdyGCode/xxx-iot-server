# --------------------------------------------------------------
# File:     /DB.py
# Project:  xxx-iot-server
# Author:   STUDENT NAME <STUDENT@EMAIL-ADDRESS>
# Created:  5/05/2021
# Purpose:  ...
#
# --------------------------------------------------------------

import urllib.parse

from sqlalchemy import BigInteger, Column, DateTime, func, \
    String, Text
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
    topic = Column(String(255))
    client = Column(String(255))
    data = Column(Text)
    recorded_at = Column(DateTime)
    created_at = Column(DateTime, server_default=func.now())

    def __init__(self):
        self.topic = ""
        self.client = ""
        self.data = ""
        self.recorded_at = "1000-01-01 00:00:00"

    def __str__(self):
        return_string = f"{self.id:>6x} {self.topic}" \
                        f"{self.client} {self.data}"
        return return_string


class Sensor(Base):
    __tablename__ = "iot_sensors"
    id = Column(BigInteger, primary_key=True, autoincrement=True)
    topic = Column(String(255))
    client = Column(String(255))
    data = Column(Text)
    recorded_at = Column(DateTime)
    created_at = Column(DateTime, server_default=func.now())

    def __init__(self):
        self.topic = ""
        self.client = ""
        self.data = ""
        self.recorded_at = "1000-01-01 00:00:00"

    def __str__(self):
        return_string = f"{self.id:>6x} {self.topic}" \
                        f"{self.client} {self.data}"
        return return_string
