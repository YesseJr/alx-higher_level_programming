-- A script that creates the database hbtn_0d_usa and the table states (in the database hbtn_0d_usa) on MySQL server.
-- If the database hbtn_0d_usa already exists,this script should not fail.
-- If the table states already exists, this script should not fail.
-- Author: Waython Yesse

CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
USE hbtn_0d_usa;
CREATE TABLE IF NOT EXISTS states (
       id INT UNIQUE AUTO_INCREMENT NOT NULL PRIMARY KEY,
       name VARCHAR(256) NOT NULL
);
