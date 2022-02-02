-- This is script that creates a table called first_table in the current database in MySQL server.
-- If the table first_table already exists, this script should not fail.
-- Author: Waython Yesse

CREATE TABLE IF NOT EXISTS first_table (id INT, name VARCHAR(256));
