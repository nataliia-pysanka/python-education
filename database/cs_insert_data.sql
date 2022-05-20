CREATE TEMPORARY TABLE streets (id int, name varchar);
COPY streets FROM '/usr/src/street.csv' DELIMITER ',';

-- fills the table Car_model
DO
$$
DECLARE
    car_model_max_id int;
    car_model_min_id int;
    car_price numeric;
    car_year int;
BEGIN
    raise notice 'fill the table Car_model';
    SELECT max(id_car_model) FROM car_model INTO car_model_max_id;
    SELECT min(id_car_model) FROM car_model INTO car_model_min_id;

    FOR i IN car_model_min_id..car_model_max_id LOOP
        car_price := (floor(random() * 150 + 20) - 0.01)::numeric(24, 2);
        UPDATE car_model
            SET price = car_price
            WHERE id_car_model = i;
    END LOOP;
END
$$ language plpgsql;



-- fills the table Customer
DO
$$
DECLARE
    len int;
    street_max_id int;
    street_min_id int;
    zip_max_id int;
    zip_min_id int;
    random_street int;
    random_zip int;
    street_name varchar;
    random_phone varchar;
    random_date date;
BEGIN
    raise notice 'fill the table Customer';
    SELECT max(id_customer) FROM customer INTO len;
    SELECT max(id) FROM streets INTO street_max_id;
    SELECT min(id) FROM streets INTO street_min_id;
    SELECT max(id_zip) FROM zip INTO zip_max_id;
    SELECT min(id_zip) FROM zip INTO zip_min_id;
    FOR i IN 1..len LOOP
        random_street := random_between(street_min_id, street_max_id);
        random_zip := random_between(zip_min_id, zip_max_id);
        SELECT name FROM streets WHERE id = random_street INTO street_name;
        random_phone := get_phone_number();
        random_date := get_date();
        UPDATE customer
            SET birth = random_date,
                phone = random_phone,
                street = street_name,
                id_zip = random_zip
            WHERE id_customer = i;
    END LOOP;
END;
$$ language plpgsql;


-- fills the table Branch
DO
$$
DECLARE
    len int := 1000;
    street_max_id int;
    street_min_id int;
    zip_max_id int;
    zip_min_id int;
    random_street int;
    random_zip int;
    street_name varchar;
    random_phone varchar;
BEGIN
    raise notice 'fill the table Branch';
    SELECT max(id) FROM streets INTO street_max_id;
    SELECT min(id) FROM streets INTO street_min_id;
    SELECT max(id_zip) FROM zip INTO zip_max_id;
    SELECT min(id_zip) FROM zip INTO zip_min_id;
    FOR i IN 1..len LOOP
        random_street := random_between(street_min_id, street_max_id);
        random_zip := random_between(zip_min_id, zip_max_id);
        random_phone := get_phone_number();

        SELECT name FROM streets WHERE id = random_street INTO street_name;
        INSERT INTO branch (phone, street, id_zip)
            VALUES
                (random_phone,
                street_name,
                random_zip);
    END LOOP;
END;
$$ language plpgsql;

DROP TABLE streets;


-- fills the table Car
DO
$$
DECLARE
    len int := 10000;
    car_model_max_id int;
    car_model_min_id int;
    branch_max_id int;
    branch_min_id int;
    random_branch_id int;
    random_car_model_id int;
    random_number varchar;
    random_year int;
    check_number varchar;
    state_id int;
    car_price numeric;
BEGIN
    raise notice 'fill the table Car';
    SELECT max(id_car_model) FROM car_model INTO car_model_max_id;
    SELECT min(id_car_model) FROM car_model INTO car_model_min_id;
    SELECT max(id_branch) FROM branch INTO branch_max_id;
    SELECT min(id_branch) FROM branch INTO branch_min_id;
    FOR i IN 1..len LOOP
        random_car_model_id := random_between(car_model_min_id, car_model_max_id);
        random_branch_id := random_between(branch_min_id, branch_max_id);
        SELECT id_state FROM branch
            INNER JOIN zip USING(id_zip)
            INNER JOIN city USING(id_city)
            INNER JOIN state USING (id_state)
            WHERE id_branch = random_branch_id INTO state_id;

        SELECT price FROM car_model WHERE id_car_model = random_car_model_id INTO car_price;
        CASE
            WHEN car_price < 50 THEN
                random_year = random_between(2000, 2007);
            WHEN car_price BETWEEN 50 AND 100 THEN
                random_year = random_between(2008, 2015);
            ELSE
                random_year = random_between(2016, 2020);
        END CASE;
        WHILE FOUND loop
            random_number := get_car_number(state_id, random_year);
            SELECT car_number FROM car WHERE car_number = random_number into check_number;
        end loop;
        INSERT INTO car (id_car_model, car_number, year, id_branch)
            VALUES
                (random_car_model_id,
                random_number,
                random_year,
                random_branch_id);
    END LOOP;
END
$$ language plpgsql;


-- fills the table Renting

DO
$$
DECLARE
    len int := 200000;
    car_max_id int;
    car_min_id int;
    customer_max_id int;
    customer_min_id int;
    random_car_id int;
    random_customer_id int;
    random_date date;
    state_id int;
    car_year int;
    total_price numeric;
    check_customer int;
    rent_period int;
BEGIN
    raise notice 'fill the table Renting';
    SELECT max(id_car) FROM car INTO car_max_id;
    SELECT min(id_car) FROM car INTO car_min_id;
    SELECT max(id_customer) FROM customer INTO customer_max_id;
    SELECT min(id_customer) FROM customer INTO customer_min_id;
    FOR i IN 1..len LOOP
        random_date := get_date(2020, 2021);
        random_car_id := random_between(car_min_id, car_max_id);
        random_customer_id := random_between(customer_min_id, customer_max_id);
        rent_period := random_between(1, 7);
        SELECT price FROM car_model
            INNER JOIN car USING(id_car_model)
            WHERE id_car = random_car_id INTO total_price;
        total_price := total_price * rent_period;
        INSERT INTO renting (date_renting, period, id_customer, price, id_car)
            VALUES
                (random_date,
                rent_period,
                random_customer_id,
                total_price,
                random_car_id);
    END LOOP;
END
$$ language plpgsql;

