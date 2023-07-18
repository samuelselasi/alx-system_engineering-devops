# [How to] Set up MySQL User
## create the setup file
```
sel@sel-HP-ENVY-x360-m6-Convertible:~/alx/alx-system_engineering-devops/0x14-mysql$ cat setup_mysql_dev.sql 
-- script to create MySQL user on web servers

-- create user if not exist
-- user should should be identified with password projectcorrection280hbtn
CREATE USER IF NOT EXISTS 'holberton_user'@'localhost' IDENTIFIED BY 'projectcorrection280hbtn';

-- grant holberton_user permission to check primary/replica status
GRANT REPLICATION CLIENT ON *.* TO 'holberton_user'@'localhost';
FLUSH PRIVILEGES;
```
## Prepare the bash script to transfer the setup file to the server 
File: [0-transfer_file](./0-transfer_file)
## transfer the setup file to the server
```
./0-transfer_file setup_mysql_dev.sql 3.90.70.66 ubuntu ~/.ssh/school
```

## Execute the setup file on the individual servers as such:
```
cat setup_mysql_dev.sql | sudo mysql
```
