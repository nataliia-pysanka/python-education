-- views for table products
CREATE OR REPLACE VIEW view_products AS
SELECT product_title, product_description, in_stock, price
FROM products
ORDER BY product_id DESC;

CREATE OR REPLACE VIEW view_products_in_stock AS
SELECT product_title, product_description, in_stock, price
FROM products
WHERE in_stock > 0
ORDER BY in_stock DESC, price DESC;

CREATE OR REPLACE VIEW view_products_top_price AS
SELECT product_title, product_description, in_stock, price
FROM products
ORDER BY price DESC, product_title ASC
LIMIT 20;

-- --------------------
-- views for table order_statuses and orders
CREATE OR REPLACE VIEW view_order_paid_or_finished AS
SELECT o.order_id, os.status_name, o.total, o.created_at, o.updated_at
    FROM order_statuses os
    INNER JOIN orders o USING (order_status_id)
    WHERE os.status_name in ('Finished', 'Paid');

DROP VIEW view_order;

CREATE OR REPLACE VIEW view_order_canceled AS
SELECT o.order_id, os.status_name, o.total, o.created_at, o.updated_at
    FROM order_statuses os
    INNER JOIN orders o USING (order_status_id)
    WHERE os.status_name in ('Canceled');

CREATE OR REPLACE VIEW view_order AS
SELECT o.order_id, os.status_name, o.total, o.created_at, o.updated_at
    FROM order_statuses os
    INNER JOIN orders o USING (order_status_id)
ORDER BY os.order_status_id DESC, total DESC;

-- --------------------
-- views for table products and categories
CREATE OR REPLACE VIEW view_categories AS
SELECT c.category_title, count(p.product_title)
    FROM products p
    LEFT JOIN categories c USING (category_id)
GROUP BY c.category_title
ORDER BY count(p.product_title) DESC;

-- rename view
ALTER VIEW view_categories RENAME TO view_products_count_by_categories;
-- drop view
DROP VIEW view_products_count_by_categories;

CREATE OR REPLACE VIEW view_products_by_categories AS
SELECT c.category_title, p.product_title
    FROM products p
    INNER JOIN categories c USING (category_id)
ORDER BY category_title, product_title;

DROP VIEW view_products_by_categories;

CREATE OR REPLACE VIEW view_categories_in_stock AS
SELECT c.category_title, count(p.in_stock)
    FROM products p
    INNER JOIN categories c USING (category_id)
    WHERE in_stock > 0
GROUP BY c.category_title
ORDER BY count(p.in_stock) DESC;

DROP VIEW view_categories_in_stock;

-- --------------------
-- create materialized view
CREATE MATERIALIZED VIEW users_by_orders
AS
SELECT users.first_name, count(orders.order_id)
        FROM users
        JOIN carts USING (user_id)
            JOIN orders USING (cart_id)
        GROUP BY users.first_name
        ORDER BY users.first_name
WITH NO DATA;

SELECT * FROM users_by_orders;
-- ERROR: materialized view "users_by_orders" has not been populated

REFRESH MATERIALIZED VIEW users_by_orders;

SELECT * FROM users_by_orders;

-- --------------------
-- Create sequence and restart with max number of product_id
CREATE SEQUENCE products_id_seq;
SELECT max(product_id)+1 FROM products;
ALTER SEQUENCE products_id_seq RESTART WITH 4002;

-- Change default value of product_id to sequence
ALTER TABLE products
    ALTER COLUMN product_id SET DEFAULT nextval('products_id_seq');

-- insert new record to the table products via view
INSERT INTO view_products (product_title, product_description, in_stock, price)
    VALUES ('Orange juice', 'Fresh juice', 21, 29.99);

-- show records from table via view
SELECT * FROM view_products;

-- insert new record with 0 value to the table products via view
INSERT INTO view_products_in_stock (product_title, product_description, in_stock, price)
    VALUES ('Pineapple juice', 'Fresh juice', 0, 29.99);

-- create new view with strict condition
CREATE VIEW view_products_in_stock_existed AS
    SELECT * FROM view_products_in_stock
    WITH CASCADED CHECK OPTION;

-- insert new record with 0 value to the table products via view
INSERT INTO view_products_in_stock_existed (product_title, product_description, in_stock, price)
    VALUES ('Lemon juice', 'Fresh juice', 0, 29.99);
-- ERROR: new row violates check option for view "view_products_in_stock"
-- Detail: Failing row contains (4005, Lemon juice, Fresh juice, 0, 29.99, null, null).