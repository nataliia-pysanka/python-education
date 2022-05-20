-- Checks the age of new customer before insert or update
CREATE OR REPLACE FUNCTION check_customer_birth()
    RETURNS TRIGGER
    AS
$$
BEGIN
    IF NEW.birth BETWEEN '1960-01-01'::date AND (now() - '22 years'::interval) THEN
        RETURN NEW;
    ELSE
        raise exception 'The age of customer is not valid';
    end if;
end;
$$ language plpgsql;

-- Works for updating or inserting into the table customer
CREATE TRIGGER new_customer
    BEFORE INSERT OR UPDATE
    ON customer
    FOR EACH ROW
    EXECUTE PROCEDURE check_customer_birth();


INSERT INTO customer (first_name, last_name, birth, phone, street, id_zip)
    VALUES (
        'SARA','CONNOR', '1950-01-01', '000-000-000-000', 'MAGNOLIA STR.', 1);
-- [P0001] ERROR: The age of customer is not valid

INSERT INTO customer (first_name, last_name, birth, phone, street, id_zip)
    VALUES (
        'SARA','CONNOR', '1970-01-01', '000-000-000-000', 'MAGNOLIA STR.', 1);
SELECT * FROM customer WHERE first_name = 'SARA' AND last_name = 'CONNOR';

UPDATE customer
    SET birth = '1950-01-01',
        phone = '000-000-000-000',
        street = 'MAGNOLIA STR.',
        id_zip = 1
    WHERE id_customer = 1;
-- ERROR: The age of customer is not valid

UPDATE customer
    SET birth = '1980-01-01'
    WHERE id_customer = 1;



-- Checks if the number of renting is tenth for this user. If it is them change
-- price - make a discount of 10%

CREATE OR REPLACE FUNCTION check_renting_number_of_adding()
    RETURNS TRIGGER
    AS
$$
DECLARE
    counter integer;
BEGIN
    SELECT count(id_customer) FROM renting WHERE id_customer = NEW.id_customer INTO counter;
    raise notice 'The number of renting is %', counter;
    IF mod(counter, 10) = 0 THEN
        raise notice 'Customer % have discount', NEW.id_customer;
        raise notice 'Old price was %', NEW.price;
        NEW.price := NEW.price - (NEW.price * 0.1);
        raise notice 'New price is %', NEW.price;
    end if;
    RETURN NEW;
end;
$$ language plpgsql;

-- Works for inserting into the table customer

CREATE TRIGGER new_renting_number
    AFTER INSERT
    ON renting
    FOR EACH ROW
    EXECUTE PROCEDURE check_renting_number_of_adding();

-- insert new rent
DO
$$
DECLARE
    car_max_id int;
    car_min_id int;
    total_price numeric;
    random_car_id int;
    random_customer_id int;
    random_date date;
    customer_max_id int;
    customer_min_id int;
    rent_period int;
    counter int;
    item int;
BEGIN
    SELECT max(id_car) FROM car INTO car_max_id;
    SELECT min(id_car) FROM car INTO car_min_id;
    SELECT max(id_customer) FROM customer INTO customer_max_id;
    SELECT min(id_customer) FROM customer INTO customer_min_id;
    random_customer_id := random_between(customer_min_id, customer_max_id);
    SELECT count(id_customer) FROM renting WHERE id_customer = random_customer_id INTO counter;
--     item := 10 - mod(counter, 10);
    raise notice 'counter = %, items = %', counter, item;
    FOR i IN 1..item LOOP
        random_date := get_date(2022, 2022);
        random_car_id := random_between(car_min_id, car_max_id);

        rent_period := random_between(1, 7);
        SELECT car_model.price FROM car_model
                INNER JOIN car USING(id_car_model)
                WHERE car.id_car = random_car_id INTO total_price;
        total_price := total_price * rent_period;
        INSERT INTO renting (date_renting, period, id_customer, price, id_car)
                VALUES
                    (random_date,
                    rent_period,
                    random_customer_id,
                    total_price,
                    random_car_id);
    end loop;
end;
$$ language plpgsql;
