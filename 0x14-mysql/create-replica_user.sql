-- script to create MySQL user on web servers

-- create user if not exist
-- user should should be identified with password projectcorrection280hbtn
CREATE USER IF NOT EXISTS 'replica_user'@'%' IDENTIFIED BY 'projectcorrection280hbtn';

-- grant hbnb_dev all previleges on hbnb_dev_db
GRANT REPLICATION SLAVE ON *.* TO 'replica_user'@'%';

-- grant select privileges on mysql.user table
GRANT SELECT ON mysql.user TO 'holberton_user'@'localhost';

FLUSH PRIVILEGES;
