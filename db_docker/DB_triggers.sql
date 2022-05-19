-- 1. Сравнить цену каждого продукта n с средней ценой продуктов в категории
-- продукта n. Использовать window function. Таблица результата должна
-- содержать такие колонки: category_title, product_title, price, avg.

SELECT
	category_title,
	product_title,
	price,
	AVG (price) OVER (
	   PARTITION BY category_title
	)
FROM
	products
	INNER JOIN
		categories USING (category_id);

SELECT *
FROM information_schema. columns
WHERE table_schema = 'public'
AND table_name = 'cart_product';


-- 2. Добавить 2 любых триггера и обработчика к ним, обязательно использовать
-- транзакции. Снабдить комментариями - что делают триггеры и обработчики.

-- 1.
-- Check if quantity of product more then 0 and return NEW or raise exception
CREATE OR REPLACE FUNCTION check_new_cart_product()
    RETURNS TRIGGER
    AS
$$
BEGIN
    IF NEW.product_id IN (SELECT product_id FROM products WHERE in_stock > 0) THEN
        RETURN NEW;
    ELSE
        raise exception 'Not enougth quantity of product';
        RETURN NULL;
    end if;
end;
$$ language plpgsql;

-- Works for updating or inserting into the table cart_product
CREATE TRIGGER new_cart_product
    BEFORE INSERT OR UPDATE
    ON cart_product
    FOR EACH ROW
    EXECUTE PROCEDURE check_new_cart_product();

INSERT INTO cart_product (cart_id, product_id) VALUES (1, 3138);
--[P0001] ERROR: Not enougth quantity of product

SELECT * FROM cart_product WHERE product_id=972;
INSERT INTO cart_product (cart_id, product_id) VALUES (1, 972);
SELECT * FROM cart_product WHERE product_id=972;

-- 2.
-- After adding new record for product table checks the product_title.
-- Makes new record to the doubled_products table if the same title already exists

-- Create a table for products with the same titles
CREATE TABLE doubled_products (product_id int, product_title varchar);

-- Create function for trigger check_product
CREATE OR REPLACE FUNCTION check_product()
    RETURNS TRIGGER
    AS
$$
DECLARE
    rec record;
    cur_products CURSOR(new_product_title varchar) FOR
		 SELECT product_id, product_title FROM products
                    WHERE product_title = new_product_title;
BEGIN
--  open the cursor
    OPEN cur_products(NEW.product_title);
    LOOP
      fetch cur_products into rec;
      exit when not found;

        IF rec.product_id IN (SELECT product_id FROM doubled_products) THEN
            continue;
        ELSE
--          adds to the doubled_products table
            INSERT INTO doubled_products VALUES(rec.product_id, NEW.product_title);
        END IF;
    end loop;
    CLOSE cur_products;
    RETURN NEW;
end;
$$ language plpgsql;

-- Create trigger for inserted records into table products
CREATE TRIGGER new_product
    AFTER INSERT
    ON products
    FOR EACH ROW
    EXECUTE PROCEDURE check_product();

-- create sequence for table products
CREATE SEQUENCE products_id_seq;
ALTER SEQUENCE products_id_seq RESTART WITH 5000;

INSERT INTO products (product_title, product_description, in_stock, price)
    VALUES ('Pineapple juice', 'Fresh juice', 1, 49.99);

INSERT INTO products (product_title, product_description, in_stock, price)
    VALUES ('Banana juice', 'Fresh juice', 1, 39.99);

DELETE FROM products WHERE product_title = 'Pineapple juice';

SELECT product_title, count(product_id) FROM doubled_products
GROUP BY product_title;


-- clear all
-- Delete table for doubled products
DROP TABLE IF EXISTS doubled_products;

-- Drop function check_product
DROP FUNCTION IF EXISTS check_product();
-- delete trigger new_product
DROP TRIGGER IF EXISTS new_product ON products;
-- delete sequence products_id_seq
DROP SEQUENCE products_id_seq;

-- USING FOR
-- Insert on products  (cost=0.00..0.01 rows=0 width=0) (actual time=0.448..0.476 rows=0 loops=1)
--   ->  Result  (cost=0.00..0.01 rows=1 width=676) (actual time=0.155..0.175 rows=1 loops=1)
-- Planning Time: 0.124 ms
-- Trigger for constraint fk_product_category: time=0.139 calls=1
-- Trigger new_product: time=6.816 calls=1
-- Execution Time: 7.553 ms

-- USING CURSOR
-- Insert on products  (cost=0.00..0.01 rows=0 width=0) (actual time=0.108..0.137 rows=0 loops=1)
--   ->  Result  (cost=0.00..0.01 rows=1 width=676) (actual time=0.026..0.047 rows=1 loops=1)
-- Planning Time: 0.067 ms
-- Trigger for constraint fk_product_category: time=0.020 calls=1
-- Trigger new_product: time=1.667 calls=1
-- Execution Time: 2.006 ms