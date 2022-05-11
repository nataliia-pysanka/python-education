-- Задание 1
-- Создайте новую таблицу potential customers с полями id, email, name, surname,
-- second_name, city
DROP TABLE potential_customers;
CREATE TABLE IF NOT EXISTS potential_customers (
    id INT NOT NULL,
    email VARCHAR(255),
    name VARCHAR(255),
    surname VARCHAR(255),
    second_name VARCHAR(255),
    city VARCHAR(255),

    PRIMARY KEY (id)
);

-- Заполните данными таблицу.
COPY potential_customers FROM '/usr/src/potential_users.csv' DELIMITER ',';

-- Выведите имена и электронную почту потенциальных и существующих пользователей
-- из города city 17
SELECT first_name || ' ' || middle_name || ' ' || last_name as user_full_name,
       email as email FROM users WHERE city = 'city 17'
    UNION
    SELECT name || ' ' || second_name || ' ' || surname as user_full_name,
       email as email FROM potential_customers WHERE city = 'city 17';

-- Задание 2
-- Вывести имена и электронные адреса всех users отсортированных по городам и по имени (по алфавиту)
SELECT first_name, email FROM users
    ORDER BY city, first_name;

-- Задание 3
-- Вывести наименование группы товаров, общее количество по группе товаров в порядке убывания количества
SELECT COUNT(product_title) FROM products GROUP BY category_id ORDER BY COUNT(product_title) DESC;

-- Задание 4
-- 1. Вывести продукты, которые ни разу не попадали в корзину.
SELECT product_title FROM products LEFT OUTER JOIN cart_product cp
        ON products.product_id = cp.product_id WHERE cp.product_id IS NULL;

-- 2. Вывести все продукты, которые так и не попали ни в 1 заказ. (но в корзину попасть могли).
SELECT products.product_title, CASE
        WHEN orders.order_id IS NULL THEN 0 ELSE orders.order_id END AS is_order
        FROM products JOIN
            cart_product LEFT OUTER JOIN orders ON cart_product.cart_id = orders.cart_id
        ON products.product_id = cart_product.product_id
        WHERE orders.cart_id IS NULL;

-- 3. Вывести топ 10 продуктов, которые добавляли в корзины чаще всего.
SELECT products.product_title, count(cp.product_id)
        FROM cart_product cp JOIN products ON cp.product_id = products.product_id
        GROUP BY products.product_title
        ORDER BY count(cp.product_id) DESC
        LIMIT 10;

-- 4. Вывести топ 10 продуктов, которые не только добавляли в корзины, но и оформляли заказы чаще всего.
SELECT products.product_title, count(cart_product.product_id)
        FROM products JOIN cart_product
            JOIN orders ON cart_product.cart_id = orders.cart_id
        ON products.product_id = cart_product.product_id

        GROUP BY products.product_title
        ORDER BY count(cart_product.product_id) DESC
        LIMIT 10;

-- 5. Вывести топ 5 юзеров, которые потратили больше всего денег (total в заказе).
SELECT users.first_name, orders.total, order_statuses.status_name FROM
            users JOIN carts ON users.user_id = carts.user_id
            JOIN
                orders JOIN order_statuses ON orders.order_status_id = order_statuses.order_status_id
            ON carts.cart_id = orders.cart_id

    WHERE order_statuses.status_name in ('Finished', 'Paid')
    ORDER BY orders.total DESC
    LIMIT 5;

-- 6. Вывести топ 5 юзеров, которые сделали больше всего заказов (кол-во заказов).
SELECT users.first_name, count(orders.order_id)
        FROM users
        JOIN carts ON users.user_id = carts.user_id
            JOIN orders ON carts.cart_id = orders.cart_id
        GROUP BY users.first_name
        ORDER BY users.first_name
        LIMIT 5;

-- 7. Вывести топ 5 юзеров, которые создали корзины, но так и не сделали заказы.
SELECT users.first_name,
        CASE
        WHEN orders.order_id IS NULL THEN 0 ELSE orders.order_id END
        FROM users JOIN carts ON users.user_id = carts.user_id
        LEFT OUTER JOIN orders ON carts.cart_id = orders.cart_id WHERE orders.cart_id IS NULL
        ORDER BY users.first_name
        LIMIT 5;
