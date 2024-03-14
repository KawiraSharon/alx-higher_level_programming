-- creates database table states on MySQL server
-- create dtb
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
-- use dtb
USE hbtn_0d_usa;
-- create table
CREATE TABLE IF NOT EXISTS states (id INT UNIQUE NOT NULL AUTO_INCREMENT, name VARCHAR(256) NOT NULL, PRIMARY KEY(id));
