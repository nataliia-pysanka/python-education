EXPLAIN ANALYZE
    SELECT manufacturer || ' ' || model as model, year, car_number, price
        FROM car
        INNER JOIN car_model USING (id_car_model)
        WHERE car_number ilike '1%'
        ORDER BY year DESC, price DESC;

-- Sort  (cost=219.60..220.36 rows=303 width=52) (actual time=45.604..48.594 rows=295 loops=1)
-- Planning Time: 0.330 ms
-- Execution Time: 51.162 ms

CREATE INDEX idx_car_car_number ON car USING hash (car_number);
CREATE INDEX idx_car_car_number ON car USING btree (car_number);
DROP INDEX idx_car_car_number;
-- Adding index for car_number (hash or btree) made worst time result
-- Planning Time: 5.928 ms
-- Execution Time: 120.357 ms

CREATE INDEX idx_car_model_model ON car_model USING btree (model);
-- Adding index for car model (btree) made worst time result (but better then previous indexes)
-- Planning Time: 2.831 ms
-- Execution Time: 77.350 ms

CREATE INDEX idx_car_model_model ON car_model USING hash (model);
-- This index didnt make any time changes
-- Planning Time: 3.899 ms
-- Execution Time: 58.574 ms

DROP INDEX idx_car_model_model;

CREATE INDEX idx_car_model_manufacturer_model ON car_model USING btree (manufacturer, model);
-- Planning Time: 11.505 ms
-- Execution Time: 72.177 ms
DROP INDEX idx_car_model_manufacturer_model;


CREATE INDEX idx_car_model_price ON car_model USING btree (price);
-- Planning Time: 0.914 ms
-- Execution Time: 74.366 ms
-- Execution Time: 72.177 ms
DROP INDEX idx_car_model_price;

CREATE INDEX idx_car_year ON car USING btree (year);
-- Planning Time: 1.664 ms
-- Execution Time: 74.950 ms

DROP INDEX idx_car_year;

-- The database was well designed, have good structure and don't need more indexes
