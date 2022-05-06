DROP TABLE users;
DROP TABLE carts;
DROP TABLE categories;
DROP TABLE order_statuses;

-- TASK 1
CREATE TABLE IF NOT EXISTS users (
    user_id INT NOT NULL,
    email VARCHAR(255),
    password VARCHAR(255),
    first_name VARCHAR(255),
    last_name VARCHAR(255),
    middle_name VARCHAR(255),
    is_staff SMALLINT,
    country VARCHAR(255),
    city VARCHAR(255),
    address TEXT,

    PRIMARY KEY (user_id)
);

CREATE TABLE IF NOT EXISTS carts
(
    cart_id INT NOT NULL,
    user_id INT NOT NULL,
    subtotal DECIMAL,
    total DECIMAL,
    time_stamp TIMESTAMP(2),

    PRIMARY KEY (cart_id),
    CONSTRAINT FK_cart_user FOREIGN KEY (user_id)
    REFERENCES users(user_id)
);

CREATE TABLE IF NOT EXISTS categories (
    category_id serial PRIMARY KEY,
    category_title VARCHAR(255),
    category_description TEXT
);

CREATE TABLE IF NOT EXISTS order_statuses (
    order_status_id serial PRIMARY KEY,
    status_name VARCHAR(255)
);

CREATE TABLE IF NOT EXISTS orders
(
    order_id INT NOT NULL,
    cart_id INT NOT NULL,
    order_status_id INT NOT NULL,
    shipping_total DECIMAL,
    total DECIMAL,
    created_at TIMESTAMP(2),
    updated_at TIMESTAMP(2),

    PRIMARY KEY (order_id),
    CONSTRAINT FK_order_cart FOREIGN KEY (cart_id)
    REFERENCES carts(cart_id),
    CONSTRAINT FK_order_order_status FOREIGN KEY (order_status_id)
    REFERENCES order_statuses(order_status_id)
);

CREATE TABLE IF NOT EXISTS products
(
    product_id INT NOT NULL,
    product_title VARCHAR(255),
    product_description TEXT,
    in_stock INT,
    price FLOAT,
    slug VARCHAR(45),
    category_id INT NOT NULL,

    PRIMARY KEY (product_id),
    CONSTRAINT FK_product_category FOREIGN KEY (category_id)
    REFERENCES categories(category_id)
);

CREATE TABLE IF NOT EXISTS cart_product
(
    cart_id INT NOT NULL,
    product_id INT NOT NULL,

    CONSTRAINT FK_product_cart FOREIGN KEY (cart_id)
    REFERENCES carts(cart_id),
    CONSTRAINT FK_cart_product FOREIGN KEY (product_id)
    REFERENCES products(product_id)
);

-- TASK 2

SELECT * FROM users;

ALTER TABLE users ADD phone INT;

SELECT first_name, last_name, phone FROM users;

ALTER TABLE users DROP COLUMN phone;

ALTER TABLE users ALTER COLUMN phone TYPE VARCHAR(15);

UPDATE users SET phone = '000-000-000';

-- TASK 3

UPDATE products SET price = price * 2;