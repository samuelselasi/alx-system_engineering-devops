-- script to create MySQL user on web servers

-- create user if not exist
-- user should should be identified with password projectcorrection280hbtn
CREATE USER IF NOT EXISTS 'holberton_user'@'localhost' IDENTIFIED BY 'projectcorrection280hbtn';

-- grant holberton_user permission to check primary/replica status
GRANT REPLICATION CLIENT ON *.* TO 'holberton_user'@'localhost';
FLUSH PRIVILEGES;

