--TASK 1
--Show:

--1. all users
SELECT first_name || ' ' || middle_name || ' ' || last_name as user_full_name
FROM USERS;

--2. all products
SELECT product_title  FROM products;

--3. all orders statuses
SELECT status_name FROM order_statuses;

--TASK 2
--Display orders that have been successfully delivered and paid for
SELECT order_id, status_name, shipping_total, total, created_at, updated_at
    FROM orders, order_statuses
    WHERE orders.order_status_id = order_statuses.order_status_id and
          status_name ILIKE 'finished';

--TASK 3
--Show:

--1. Products whose price is greater than 80.00 and less than or equal to 150.00
SELECT product_title, price
    FROM products
    WHERE price > 80.00 and price <= 150.00;

SELECT product_title, price
    FROM products
    WHERE price BETWEEN 80.00 and 150.00;

--2. Orders made after 01.10.2020 (created_at field)
SELECT * FROM orders
    WHERE created_at >= '2020-10-01'::date;

--3. Orders received in the first half of 2020 year
SELECT * FROM orders
    WHERE created_at BETWEEN '2020-01-01' AND '2020-06-30';

--4. Products of next categories: Category 7, Category 11, Category 18
SELECT product_title, category_title FROM products, categories
    WHERE products.category_id = categories.category_id AND
        category_title IN ('Category 7', 'Category 11', 'Category 18');

--5. Unfinished orders as of 31.12.2020
SELECT order_id, status_name, shipping_total, total, created_at, updated_at
    FROM orders, order_statuses
    WHERE orders.order_status_id = order_statuses.order_status_id AND
          status_name NOT IN ('Finished', 'Canceled') AND
          created_at <= '2020-12-31';

--6.Display all carts that have been created but the order has not yet been placed.
SELECT * FROM carts
    WHERE NOT EXISTS (SELECT * FROM orders WHERE orders.cart_id = carts.cart_id);

--TASK 4
--Show:
--1. The average amount of all completed transactions
SELECT avg(total) FROM orders, order_statuses
    WHERE orders.order_status_id = order_statuses.order_status_id AND
          status_name = 'Finished';

--2. Withdraw the maximum transaction amount for the 3rd quarter of 2020
SELECT max(total) FROM orders, order_statuses
    WHERE orders.order_status_id = order_statuses.order_status_id AND
          status_name = 'Finished' AND
          created_at between '2020-07-01' AND '2020-09-30';


