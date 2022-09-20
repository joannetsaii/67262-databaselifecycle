\connect postgres

drop database if exists Database_Model_for_DoorDash;
create database Database_Model_for_DoorDash;

\connect Database_Model_for_DoorDash;

\i Database_Model_for_DoorDash_create.sql

-- \i Database_Model_for_DoorDash_load.sql
