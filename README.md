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

#### Hardware:
* Raspberry Pi 3B or later

#### Package Requirements

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

Install MariaDB on Raspberry Pi

```shell
sudo apt-get install mariadb-server
```
The process with start with the following text (or similar)...
```text
pi@per-pi-000:~ $ sudo apt-get install mariadb-server
Reading package lists... Done
Building dependency tree       
Reading state information... Done

The following NEW packages will be installed:
  mariadb-server
0 upgraded, 1 newly installed, 0 to remove and 8 not upgraded.
```

When it asks if you wish to install press Y then Enter.

When installed successfully, run the MySQL/MariaDB shell:

```shell
sudo mysql -uroot
```

You should see a welcome similar to the following:
```text
Welcome to the MariaDB monitor.  Commands end with ; or \g.
Your MariaDB connection id is 39
Server version: 10.3.27-MariaDB-0+deb10u1 Raspbian 10

Copyright (c) 2000, 2018, Oracle, MariaDB Corporation Ab and others.

Type 'help;' or '\h' for help. Type '\c' to clear the current input statement.

MariaDB [(none)]> 
```
The `MariaDB [(none)]>` indicates that you are now in the MySQL/MariaDB command line interface.

Now you create the user and database with required access rights, replacing the `xxx` with 
your **initials** in this code, and throughout the Python and other source code.

The easiest way to do this is to edit the sample code below first.
Then copy it to the clipboard and return to the terminal. 
In the terminal press `CTRL`+`SHIFT`+`V` to paste all the code in.

```mysql
DROP DATABASE IF EXISTS xxx_iot;
DROP USER IF EXISTS 'xxx_iot'@'localhost';
FLUSH PRIVILEGES;

CREATE DATABASE IF NOT EXISTS xxx_iot;

CREATE USER 'xxx_iot'@'localhost' IDENTIFIED BY 'Password1';

GRANT USAGE ON *.* TO 'xxx_iot'@'localhost' 
    REQUIRE NONE WITH MAX_QUERIES_PER_HOUR 0 
    MAX_CONNECTIONS_PER_HOUR 0 MAX_UPDATES_PER_HOUR 0 MAX_USER_CONNECTIONS 0;

GRANT ALL PRIVILEGES ON `xxx_iot`.* TO 'xxx_iot'@'localhost';

FLUSH PRIVILEGES;
```

If you edited it all correctly then the commands will be executed, creating a new user, new 
password and new database ready for the rest of the server (and dashboard).

Here is an example of the output from the commands after successfully running (note we used 
`xxx` for our initials:
```text
MariaDB [(none)]> DROP DATABASE IF EXISTS xxx_iot;
Query OK, 0 rows affected (0.002 sec)

MariaDB [(none)]> DROP USER IF EXISTS 'xxx_iot'@'localhost';
Query OK, 0 rows affected (0.002 sec)

MariaDB [(none)]> FLUSH PRIVILEGES;
Query OK, 0 rows affected (0.001 sec)

MariaDB [(none)]> 
MariaDB [(none)]> CREATE DATABASE IF NOT EXISTS xxx_iot;
Query OK, 1 row affected (0.001 sec)

MariaDB [(none)]> 
MariaDB [(none)]> CREATE USER 'xxx_iot'@'localhost' IDENTIFIED BY 'Password1';
Query OK, 0 rows affected (0.002 sec)

MariaDB [(none)]> 
MariaDB [(none)]> GRANT USAGE ON *.* TO 'xxx_iot'@'localhost' 
    ->     REQUIRE NONE WITH MAX_QUERIES_PER_HOUR 0 
    ->     MAX_CONNECTIONS_PER_HOUR 0 MAX_UPDATES_PER_HOUR 0 MAX_USER_CONNECTIONS 0;
Query OK, 0 rows affected (0.001 sec)

MariaDB [(none)]> 
MariaDB [(none)]> GRANT ALL PRIVILEGES ON `xxx_iot`.* TO 'xxx_iot'@'localhost';
Query OK, 0 rows affected (0.001 sec)

MariaDB [(none)]> 
MariaDB [(none)]> FLUSH PRIVILEGES;
Query OK, 0 rows affected (0.003 sec)
```
Check to see if you got any errors. If you did then the problem is most likely a typo... 
Simply correct the error, copy the whole script again and paste into the CLI.

Use the command:
```mysql
SHOW DATABASES;
```
This should show a table similar to this to indicate the database was created:
```text
+--------------------+
| Database           |
+--------------------+
| information_schema |
| mysql              |
| performance_schema |
| xxx_iot            |
+--------------------+
4 rows in set (0.024 sec)
```

When the final line is executed successfully use `\q` followed by `ENTER` to quit the MySQL CLI.

You are ready to develop the server code.

## Credits


## Copyright

Copyright Adrian Gould, 2021 onwards. 
Licensed under the Open Software License version 3.0

Please credit the author whenever this code is used in any capacity.
