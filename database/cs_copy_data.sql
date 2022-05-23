-- create temporary table temp_state to fill it from csv and then
-- inserts values to the state
CREATE TEMPORARY TABLE temp_state(
    id_state int,
    name CHAR(30));

COPY temp_state FROM '/usr/src/state.csv' DELIMITER ',';

INSERT INTO state (name)
    SELECT name
    FROM temp_state;

DROP TABLE temp_state;



-- create temporary table temp_city to fill it from csv and then
-- inserts values to the city
CREATE TEMPORARY TABLE temp_city (
    id_city int,
    name CHAR(30),
    id_state INT);

COPY temp_city FROM '/usr/src/city.csv' DELIMITER ',';

INSERT INTO city (name, id_state)
    SELECT name, id_state
    FROM temp_city;

DROP TABLE temp_city;



-- create temporary table temp_zip to fill it from csv and then
-- inserts values to the zip
CREATE TEMPORARY TABLE temp_zip (
    id_zip int,
    zip_value CHAR(20),
    id_city INT);

COPY temp_zip FROM '/usr/src/zip.csv' DELIMITER ',';

INSERT INTO zip (zip_value, id_city)
    SELECT zip_value, id_city
    FROM temp_zip;

DROP TABLE temp_zip;



-- create temporary table temp_customer to fill it from csv and then
-- inserts values to the customer
CREATE TEMPORARY TABLE temp_customer (
    id_customer int,
    first_name CHAR(25),
    last_name CHAR(25));

COPY temp_customer FROM '/usr/src/customer.csv' DELIMITER ',';

INSERT INTO customer (first_name, last_name)
    SELECT first_name, last_name
    FROM temp_customer;

DROP TABLE temp_customer;



-- create temporary table temp_car_model to fill it from csv and then
-- inserts values to the car_model
CREATE TEMPORARY TABLE temp_car_model (
    id_car_model int,
    manufacturer VARCHAR,
    model VARCHAR);

COPY temp_car_model FROM '/usr/src/car_model.csv' DELIMITER ',';

INSERT INTO car_model (manufacturer, model)
    SELECT manufacturer, model
    FROM temp_car_model;

DROP TABLE temp_car_model;
