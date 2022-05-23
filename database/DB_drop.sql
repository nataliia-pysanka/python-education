DROP TABLE renting CASCADE;
DROP TABLE car CASCADE;
DROP TABLE car_model CASCADE;
DROP TABLE customer CASCADE;
DROP TABLE branch CASCADE;
DROP TABLE zip CASCADE;
DROP TABLE city CASCADE;
DROP TABLE state CASCADE;

DROP FUNCTION cs.public.check_customer_birth;
DROP FUNCTION cs.public.check_renting_number_of_adding;
DROP FUNCTION cs.public.get_car_number;
DROP FUNCTION cs.public.get_cars_used_in_interval;
DROP FUNCTION cs.public.get_date;
DROP FUNCTION cs.public.get_phone_number;
DROP FUNCTION cs.public.random_between;
DROP FUNCTION cs.public.random_letters;
DROP FUNCTION cs.public.random_numbers;
DROP FUNCTION cs.public.random_symbols;
DROP FUNCTION cs.public.get_customers;

DROP PROCEDURE cs.public.set_price;
DROP PROCEDURE cs.public.add_zip;

DROP VIEW cars_after_2018;
DROP VIEW cities_without_branch;
DROP MATERIALIZED VIEW car_model_by_state;


DROP TRIGGER new_renting_number;
DROP TRIGGER new_customer;

