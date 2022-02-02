-- A script that creates the table unique_id on your MySQL server.
-- If the table unique_id already exists, your script should not fail.
-- Author: Waython Yesse

CREATE TABLE IF NOT EXISTS unique_id (
       id INT DEFAULT 1 UNIQUE,
       name VARCHAR(256)
);
