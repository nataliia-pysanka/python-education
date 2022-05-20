-- Materialized view that shows how many times car was rented in each state
CREATE OR REPLACE MATERIALIZED VIEW car_model_by_state
AS
SELECT state.name, car_model.model, car.car_number, count(car.car_number)
        FROM car
        INNER JOIN car_model USING (id_car_model)
        INNER JOIN renting USING (id_car)
        INNER JOIN branch USING (id_branch)
        INNER JOIN zip USING (id_zip)
        INNER JOIN city USING (id_city)
        INNER JOIN state USING (id_state)
        GROUP BY state.name, car_model.model, car.car_number
        ORDER BY state.name, car_model.model, count(car.car_number) DESC
WITH NO DATA;

SELECT * FROM car_model_by_state;
-- ERROR: materialized view "car_model_by_state" has not been populated

REFRESH MATERIALIZED VIEW car_model_by_state;



-- view that shows cities without branch and quantity of customers in them
CREATE OR REPLACE VIEW cities_without_branch
AS
SELECT city.name, count(id_customer) from zip
    LEFT OUTER JOIN branch USING(id_zip)
    INNER JOIN city USING (id_city)
    LEFT JOIN customer USING (id_zip)
    WHERE branch.id_zip IS NULL
    GROUP BY city.name
    ORDER BY count(id_customer) DESC;

SELECT * FROM cities_without_branch;



-- view that shows how many cars after 2018 year
CREATE OR REPLACE VIEW cars_after_2018
AS
SELECT car_model.manufacturer, car_model.model,
       count(car.id_car) from car
    INNER JOIN branch USING (id_branch)
    INNER JOIN zip USING (id_zip)
    INNER JOIN city USING (id_city)
    INNER JOIN car_model USING (id_car_model)
    WHERE car.year >= 2018
    GROUP BY car_model.manufacturer, car_model.model
    ORDER BY car_model.manufacturer;

SELECT * FROM cars_after_2018;
