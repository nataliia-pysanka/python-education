-- Procedure checks if the new zip_value alredy exist and make rollback if it is
-- or adds new zip

CREATE OR REPLACE PROCEDURE add_zip(
   new_zip_value char(20), input_city char(30), input_state char(30)
) AS
$$
declare
    current_zip char(20);
    current_city integer;
BEGIN
    SELECT id_city FROM city
                   INNER JOIN state USING (id_state)
                   WHERE city.name = input_city AND state.name = input_state
                   INTO current_city;
    IF NOT FOUND THEN
        RAISE NOTICE 'No city "%" in the state "%"', input_city, input_state;
        ROLLBACK;
    ELSE

        SELECT zip_value FROM zip WHERE zip_value = new_zip_value INTO current_zip;

        IF FOUND THEN
            RAISE NOTICE 'Zip code "%" is already exist', new_zip_value;
            ROLLBACK;
        ELSE
            INSERT INTO zip(zip_value, id_city)
                VALUES (new_zip_value, current_city);
            COMMIT;
        END IF;
    END IF;
END;
$$ language plpgsql;


SELECT zip_value, city.name as city_name FROM zip
         INNER JOIN city USING (id_city) WHERE zip_value = '000000';

call add_zip('000000', 'BREMEN', 'ALABAMA');

SELECT zip_value, city.name as city_name FROM zip
         INNER JOIN city USING (id_city) WHERE zip_value = '000000';

call add_zip('000000', 'BREMEN', 'ALABAMA');
-- Zip code "000000" is already exist




-- set price by using discount. If new price < 0 then make rollback
CREATE OR REPLACE PROCEDURE set_price(input_car_number varchar, discount numeric) AS
$$
DECLARE
    current_price numeric;
    current_model record;
BEGIN
    SELECT * FROM car_model
        INNER JOIN car USING (id_car_model)
        WHERE car.car_number = input_car_number INTO current_model;
    IF NOT FOUND THEN
        RAISE NOTICE 'Car number % doesnt exist', current_model.car_number;
        ROLLBACK;
    end if;
    current_price := current_model.price - current_model.price * discount;

    IF current_price < 0 THEN
        RAISE NOTICE 'Discount too big!';
        ROLLBACK;
    ELSE
        UPDATE car_model
            SET price = current_price
            WHERE id_car_model = current_model.id_car_model;
        COMMIT;
    end if;
END;
$$ language plpgsql;



-- Demonstaration for price changing
DO
$$
DECLARE
    car_max_id int;
    car_min_id int;
    current_car_number varchar;
    current_car record;
BEGIN

    SELECT max(id_car) FROM car INTO car_max_id;
    SELECT min(id_car) FROM car INTO car_min_id;

    SELECT car_number FROM car WHERE id_car = random_between(car_min_id, car_max_id)
        INTO current_car_number;

    SELECT manufacturer, model, price FROM car_model
        INNER JOIN car USING (id_car_model)
        WHERE car.car_number = current_car_number
        INTO current_car;
    IF FOUND THEN
        raise notice 'Manufacturer: %', current_car.manufacturer;
        raise notice 'Model: %', current_car.model;
        raise notice 'Price: %', current_car.price;

        call set_price(current_car_number, 2);

        SELECT manufacturer, model, price FROM car_model
            INNER JOIN car USING (id_car_model)
            WHERE car.car_number = current_car_number
            INTO current_car;

        raise notice 'New price: %', current_car.price;
    end if;
end;
$$ language plpgsql;
