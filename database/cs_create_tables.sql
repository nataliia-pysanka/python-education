DROP TABLE renting CASCADE;
DROP TABLE car CASCADE;
DROP TABLE car_model CASCADE;
DROP TABLE customer CASCADE;
DROP TABLE branch CASCADE;
DROP TABLE zip CASCADE;
DROP TABLE city CASCADE;
DROP TABLE state CASCADE;


CREATE TABLE IF NOT EXISTS state (
    id_state SERIAL unique NOT NULL,
    name CHAR(30) unique NOT NULL,

    PRIMARY KEY (id_state)
);


CREATE TABLE IF NOT EXISTS city (
    id_city SERIAL unique NOT NULL,
    name CHAR(30) NOT NULL,
    id_state INT,

    PRIMARY KEY (id_city),
    CONSTRAINT FK_city_state FOREIGN KEY (id_state) REFERENCES state(id_state)
);



CREATE TABLE IF NOT EXISTS zip (
    id_zip SERIAL unique NOT NULL,
    zip_value CHAR(20) unique NOT NULL,
    id_city INT,

    PRIMARY KEY (id_zip),
    CONSTRAINT FK_zip_city FOREIGN KEY (id_city) REFERENCES city(id_city)
);



CREATE TABLE IF NOT EXISTS customer (
    id_customer SERIAL unique NOT NULL,
    first_name CHAR(25) NOT NULL,
    last_name CHAR(25) NOT NULL,
    birth date,
    phone CHAR(15),
    street CHAR(50),
    id_zip INT,

    PRIMARY KEY (id_customer),
    CONSTRAINT FK_customer_zip FOREIGN KEY (id_zip)
        REFERENCES zip(id_zip)
);


CREATE TABLE IF NOT EXISTS car_model (
    id_car_model SERIAL unique NOT NULL,
    manufacturer VARCHAR NOT NULL,
    model VARCHAR unique NOT NULL,
    price money,

    PRIMARY KEY (id_car_model)
);


CREATE TABLE IF NOT EXISTS branch (
    id_branch SERIAL unique NOT NULL,
    phone CHAR(15),
    street CHAR(50),
    id_zip INT,

    PRIMARY KEY (id_branch),
    CONSTRAINT FK_branch_zip FOREIGN KEY (id_zip)
        REFERENCES zip(id_zip)
);

CREATE TABLE IF NOT EXISTS car (
    id_car SERIAL unique NOT NULL,
    id_car_model INT,
    car_number VARCHAR unique,
    year INT,
    id_branch INT,

    PRIMARY KEY (id_car),
    CONSTRAINT FK_car_car_model FOREIGN KEY (id_car_model)
        REFERENCES car_model(id_car_model),
    CONSTRAINT FK_car_branch FOREIGN KEY (id_branch)
        REFERENCES branch(id_branch)
);


CREATE TABLE IF NOT EXISTS renting (
    id_renting SERIAL unique NOT NULL,
    date_renting date,
    period SMALLINT DEFAULT 1,
    id_customer INT NOT NULL,
    price money,
    id_car INT,

    PRIMARY KEY (id_renting),
    CONSTRAINT FK_renting_customer FOREIGN KEY (id_customer)
        REFERENCES customer(id_customer),
    CONSTRAINT FK_renting_car FOREIGN KEY (id_car)
        REFERENCES car(id_car)
);

