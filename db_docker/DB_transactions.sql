-- Задание:
-- Использовать транзакции для insert, update, delete на 3х таблицах.
-- Предоставить разнообразные примеры включая возврат к savepoints.

BEGIN;
INSERT INTO users values(
       3001, 'happy_mail@gmail.com', '88888888', 'Anna', 'Lichtenshtein', 'Maria', 0, 'France', 'Paris', 'Monmartr', '5556686'
                        );
COMMIT;

BEGIN;
    SAVEPOINT point_1;
        UPDATE users
            SET email='new_mail@gmail.com'
            WHERE user_id=3001;
    ROLLBACK TO point_1;
COMMIT;

SELECT * FROM users WHERE user_id=3001;

BEGIN;
    UPDATE users
        SET email='again_new_mail@gmail.com'
        WHERE user_id=3001;
COMMIT;


BEGIN;
SAVEPOINT point_2;
    INSERT INTO categories values(
           22, 'Milk', 'All products from farm'
                                  );
    UPDATE categories
        SET category_title='Fresh milk'
        WHERE category_id=21;
ROLLBACK TO point_2;
COMMIT;

BEGIN;
    INSERT INTO categories values(
           22, 'Milk', 'All products from farm'
                                  );
SAVEPOINT point_3;
    DELETE FROM categories
        WHERE category_id=21;
ROLLBACK TO point_3;
COMMIT;


BEGIN;
SAVEPOINT point_4;
    INSERT INTO products values(4001, 'Oak milk', null, 2, 43, null, 21);
ROLLBACK TO point_4;

SAVEPOINT point_5;
    DELETE FROM products
        WHERE product_title='Oak milk';
ROLLBACK TO point_5;

SAVEPOINT point_6;
    UPDATE products
        SET price=42.99
        WHERE product_title='Oak milk';
ROLLBACK TO point_6;
COMMIT;