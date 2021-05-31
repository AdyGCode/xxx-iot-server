# XXX IoT Server

A core project template for the analysis of current technologies and 
their application to industry - specifically within Internet of Things.

This code base is not complete, but **no** contributions are required.

## General Information

* Free software: Open Software License ("OSL") v. 3.0
* Documentation: To be added


## Features

* Listens to an MQTT topic and Receives data
* Store received sensor (environment) data to a MySQL database (table)
* Store received sensor hardware data to a MySQL database (table)

## Requirements

This code presumes certain hardware is being used.

### Hardware:
* Raspberry Pi 3B or later

### Package Requirements

This project requires the following package(s):

| Package | Purpose | Recommended Version |
|------------------|-----------------------------------|----------------|
| `paho-mqtt`  | Python MQTT package  | v1.5.1 or later |
| `SQLAlchemy`  | Python ORM for SQL databases  | v1.4.17 or later |
| `mysql-connector-python`  | MySQL Connector for Python | v8.0.25 or later |
 

Remaining packages are Python 'built-ins'.

### Package Installation

The requirements above may be installed using:

```shell
pip3 install PACKAGE_NAME
```
or using the PyCharm Project Preferences


## Required Software Installation and Configuration

Install MySQL 8 on Raspberry Pi

```shell
sudo apt-get install mysql
```

When installed successfully, run the MySQL/MariaDB shell:

```shell
mysql -u root
```

you should see:
```text

```

Now you create the user and database with required access rights, replacing the xxx with 
your initials in this code, and throughout the Python and other source code.

```SQL
DROP DATABASE IF EXISTS xxx_iot;
DROP USER IF EXISTS 'xxx_iot'@'localhost';
FLUSH PRIVILEGES;

CREATE DATABASE IF NOT EXISTS xxx_traffic_cop;
CREATE USER 'xxx_iot'@'localhost' IDENTIFIED BY 'Password1';
CREATE DATABASE IF NOT EXISTS xxx_iot;
FLUSH PRIVILEGES;

GRANT USAGE ON *.* TO 'xxx_iot'@'localhost' 
    REQUIRE NONE WITH MAX_QUERIES_PER_HOUR 0 
    MAX_CONNECTIONS_PER_HOUR 0 MAX_UPDATES_PER_HOUR 0 MAX_USER_CONNECTIONS 0;

GRANT ALL PRIVILEGES ON `xxx_iot`.* TO 'xxx_iot'@'localhost';

FLUSH PRIVILEGES;
```


## Credits


## Copyright

Copyright Adrian Gould, 2021 onwards. 
Licensed under the Open Software License version 3.0

Please credit the author whenever this code is used in any capacity.
