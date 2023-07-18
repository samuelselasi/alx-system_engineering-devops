# 0x14. MySQL
### `DevOps` `SysAdmin` `MySQL`

![KkrkDHT](https://github.com/samuelselasi/alx-system_engineering-devops/assets/85158665/3d4948a4-322c-4ec8-a829-bff37b2eb4e1)

## Resources
**Read or watch**:

* [What is a primary-replica cluster](https://www.digitalocean.com/community/tutorials/how-to-choose-a-redundancy-plan-to-ensure-high-availability#sql-replication)
* [MySQL primary replica setup](https://www.digitalocean.com/community/tutorials/how-to-set-up-replication-in-mysql)
* [Build a robust database backup strategy](https://www.databasejournal.com/ms-sql/developing-a-sql-server-backup-strategy/)

**man or help**:

* `mysqldump`

### General
* What is the main role of a database
* What is a database replica
* What is the purpose of a database replica
* Why database backups need to be stored in different physical locations
* What operation should you regularly perform to make sure that your database backup strategy actually works

## Requirements
### General
* Allowed editors: `vi`, `vim`, `emacs`
* All your files will be interpreted on Ubuntu `16.04` LTS
* All your files should end with a new line
* A `README.md` file, at the root of the folder of the project, is mandatory
* All your Bash script files must be executable
* Your Bash script must pass `Shellcheck` (version `0.3.7-5~ubuntu16.04.1` via `apt-get`) without any error
* The first line of all your Bash scripts should be exactly `#!/usr/bin/env bash`
* The second line of all your Bash scripts should be a comment explaining what is the script doing

## Tasks

[0. Install MySQL](./0-installation-steps.md)

First things first, let’s get MySQL installed on **both** your `web-01` and `web-02` servers.

* MySQL distribution must be `5.7.x`
* Make sure that [task #3](../0x0B-ssh/) of your SSH project is completed for `web-01` and `web-02`. The checker will connect to your servers to check MySQL status
* Please make sure you have your `README.md` pushed to GitHub.

**Example**:
```
ubuntu@229-web-01:~$ mysql --version
mysql  Ver 14.14 Distrib 5.7.25, for Linux (x86_64) using  EditLine wrapper
ubuntu@229-web-01:~$
```

[1. Let us in!](1-mysql-setup.md)

In order for us to verify that your servers are properly configured, we need you to create a `user` and `password` for **both** MySQL databases which will allow the checker access to them.

* Create a MySQL user named `holberton_user` on both `web-01` and `web-02` with the **host name** set to `localhost` and the **password** `projectcorrection280hbtn`. This will allow us to access the replication status on both servers.
* Make sure that `holberton_user` has permission to check the *primary/replica* status of your databases.
* In addition to that, make sure that [task #3](../0x0B-ssh/) of your SSH project is completed for `web-01` and `web-02`. 
**You will likely need to add the public key to `web-02` as you only added it to `web-01` for this project. The checker will connect to your servers to check MySQL status**

**Example**:
```
ubuntu@229-web-01:~$ mysql -uholberton_user -p -e "SHOW GRANTS FOR 'holberton_user'@'localhost'"
Enter password:
+-----------------------------------------------------------------+
| Grants for holberton_user@localhost                             |
+-----------------------------------------------------------------+
| GRANT REPLICATION CLIENT ON *.* TO 'holberton_user'@'localhost' |
+-----------------------------------------------------------------+
ubuntu@229-web-01:~$
```

[2. If only you could see what I've seen with your eyes](./2-create-table.md)

In order for you to set up replication, you’ll need to have a database with at least one table and one row in your primary MySQL server (`web-01`) to replicate from.

* Create a database named `tyrell_corp`.
* Within the `tyrell_corp` database create a table named `nexus6` and add at least one entry to it.
* Make sure that `holberton_user` has `SELECT` permissions on your table so that we can check that the table exists and is not empty.
```
ubuntu@229-web-01:~$ mysql -uholberton_user -p -e "use tyrell_corp; select * from nexus6"
Enter password:
+----+-------+
| id | name  |
+----+-------+
|  1 | Leon  |
+----+-------+
ubuntu@229-web-01:~$
```

[3. Quite an experience to live in fear, isn't it?](./create-replica_user.sql)

Before you get started with your `primary-replica` synchronization, you need one more thing in place. On your `primary` MySQL server (`web-01`), create a new user for the replica server.
* The name of the new user should be `replica_user`, with the host name set to `%`, and can have whatever password you’d like.
* `replica_user` must have the appropriate permissions to replicate your `primary` MySQL server.
* `holberton_user` will need `SELECT` privileges on the `mysql.user` table in order to check that `replica_user` was created with the correct permissions.
```
ubuntu@229-web-01:~$ mysql -uholberton_user -p -e 'SELECT user, Repl_slave_priv FROM mysql.user'
+------------------+-----------------+
| user             | Repl_slave_priv |
+------------------+-----------------+
| root             | Y               |
| mysql.session    | N               |
| mysql.sys        | N               |
| debian-sys-maint | Y               |
| holberton_user   | N               |
| replica_user     | Y               |
+------------------+-----------------+
ubuntu@229-web-01:~$
```

[4. Setup a Primary-Replica infrastructure using MySQL](./4-mysql_configuration_primary) [4. Setup a Primary-Replica infrastructure using MySQL](./4-mysql_configuration_replica)



Having a replica member on for your MySQL database has `2` advantages:

* Redundancy: If you lose one of the database servers, you will still have another working one and a copy of your data
* Load distribution: You can split the read operations between the 2 servers, reducing the load on the primary member and improving query response speed

## Requirements
* MySQL primary must be hosted on `web-01` - do not use the `bind-address`, just comment out this parameter
* MySQL replica must be hosted on `web-02`
* Setup replication for the MySQL database named `tyrell_corp`
* Provide your MySQL primary configuration as answer file(`my.cnf` or `mysqld.cnf`) with the name `4-mysql_configuration_primary`
* Provide your MySQL replica configuration as an answer file with the name `4-mysql_configuration_replica`

## Tips:
* Once MySQL replication is setup, add a new record in your table via MySQL on `web-01` and check if the record has been replicated in MySQL `web-02`. If you see it, it means your replication is working!
* **Make sure that `UFW` is allowing connections on port `3306` (default MySQL port) otherwise replication will not work.**

**Example**:
# `web-01`
```
ubuntu@web-01:~$ mysql -uholberton_user -p
Enter password: 
Welcome to the MySQL monitor.  Commands end with ; or \g.
Your MySQL connection id is 1467
Server version: 5.5.49-0ubuntu0.14.04.1-log (Ubuntu)

Copyright (c) 2000, 2016, Oracle and/or its affiliates. All rights reserved.

Oracle is a registered trademark of Oracle Corporation and/or its
affiliates. Other names may be trademarks of their respective
owners.

Type 'help;' or '\h' for help. Type '\c' to clear the current input statement.

mysql> show master status;
+------------------+----------+--------------------+------------------+
| File             | Position | Binlog_Do_DB       | Binlog_Ignore_DB |
+------------------+----------+--------------------+------------------+
| mysql-bin.000009 |      107 | tyrell_corp          |                  |
+------------------+----------+--------------------+------------------+
1 row in set (0.00 sec)

mysql>
```
# 'web-02'
```
root@web-02:/home/ubuntu# mysql -uholberton_user -p
Enter password: 
Welcome to the MySQL monitor.  Commands end with ; or \g.
Your MySQL connection id is 53
Server version: 5.5.49-0ubuntu0.14.04.1-log (Ubuntu)

Copyright (c) 2000, 2016, Oracle and/or its affiliates. All rights reserved.

Oracle is a registered trademark of Oracle Corporation and/or its
affiliates. Other names may be trademarks of their respective
owners.

Type 'help;' or '\h' for help. Type '\c' to clear the current input statement.

mysql> show slave status\G
*************************** 1. row ***************************
               Slave_IO_State: Waiting for master to send event
                  Master_Host: 158.69.68.78
                  Master_User: replica_user
                  Master_Port: 3306
                Connect_Retry: 60
              Master_Log_File: mysql-bin.000009
          Read_Master_Log_Pos: 107
               Relay_Log_File: mysql-relay-bin.000022
                Relay_Log_Pos: 253
        Relay_Master_Log_File: mysql-bin.000009
             Slave_IO_Running: Yes
            Slave_SQL_Running: Yes
              Replicate_Do_DB: 
          Replicate_Ignore_DB: 
           Replicate_Do_Table: 
       Replicate_Ignore_Table: 
      Replicate_Wild_Do_Table: 
  Replicate_Wild_Ignore_Table: 
                   Last_Errno: 0
                   Last_Error: 
                 Skip_Counter: 0
          Exec_Master_Log_Pos: 107
              Relay_Log_Space: 452
              Until_Condition: None
               Until_Log_File: 
                Until_Log_Pos: 0
           Master_SSL_Allowed: No
           Master_SSL_CA_File: 
           Master_SSL_CA_Path: 
              Master_SSL_Cert: 
            Master_SSL_Cipher: 
               Master_SSL_Key: 
        Seconds_Behind_Master: 0
Master_SSL_Verify_Server_Cert: No
                Last_IO_Errno: 0
                Last_IO_Error: 
               Last_SQL_Errno: 0
               Last_SQL_Error: 
  Replicate_Ignore_Server_Ids: 
             Master_Server_Id: 1
1 row in set (0.00 sec)

mysql>
```

