--TASK 1

-- Delete function shipping_total
DROP FUNCTION shipping_total(input_city varchar);

-- Call function shipping_total
SELECT shipping_total('city_1');

-- Create function shipping_total
CREATE OR REPLACE FUNCTION shipping_total(input_city varchar)
    RETURNS float AS
$$
--     Function change shipping_total to 0 for all orders which made by users in the city "input_city"
DECLARE
    output_shipping_total numeric := 0;
    temp_row users%ROWTYPE;
    rec record;
BEGIN
--      Check is there any record for city "input_city"
        SELECT * FROM users WHERE users.city ILIKE input_city LIMIT 1 INTO temp_row ;

--      If not exist any record, message will raised
        if not found then
            raise notice 'There is no city %', input_city;
        else
--      For each record with city="input_city" will ship_total will be changed to 0
--      and value of total column will be added to variable "output_shipping_total"
            FOR rec IN SELECT orders.order_id, orders.total FROM users
                INNER JOIN carts USING (user_id)
                INNER JOIN orders USING (cart_id)
                WHERE users.city ILIKE input_city
            LOOP
                raise notice 'Change ship_total for order_id %', rec.order_id;
                UPDATE orders SET shipping_total=0 WHERE order_id=rec.order_id;
                output_shipping_total = output_shipping_total + rec.total;
            END LOOP;

        end if;
--      Raise message wit information about output_shipping_total
        raise notice 'The total order for city % is %', input_city, output_shipping_total;
        RETURN output_shipping_total;
END;
$$ LANGUAGE plpgsql;

-- $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
--TASK 2.1
-- Delete function get_products_in_stock
DROP FUNCTION get_products_in_stock();
-- Call function get_products_in_stock
SELECT get_products_in_stock();

-- Create function get_products_in_stock
CREATE OR REPLACE function get_products_in_stock() RETURNS table (
		product_title VARCHAR,
		in_stock integer
	) AS
$$
-- Function returns a query with information about products in stock
BEGIN
    RETURN query
        SELECT products.product_title, products.in_stock
            FROM products WHERE products.in_stock > 0;
    IF NOT FOUND THEN
        RAISE EXCEPTION 'No products in stock';
    END IF;
END;
$$ LANGUAGE plpgsql;

-- $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
--TASK 2.2
-- Procedure updates table with new column for next work with function
CREATE OR REPLACE PROCEDURE add_column_cash_back() AS
$$
BEGIN
    ALTER TABLE users ADD COLUMN cash_back NUMERIC(22,3);
    UPDATE users SET cash_back = 0 WHERE cash_back IS NULL;
    ALTER TABLE users ALTER COLUMN cash_back SET DEFAULT 0.0;
    ALTER TABLE users ALTER COLUMN cash_back TYPE numeric(22,3);
    COMMIT;
END;
$$ language plpgsql;

-- Procedure clear column cash_back
CREATE OR REPLACE PROCEDURE clear_column_cash_back() AS
$$
BEGIN
    UPDATE users SET cash_back = 0 WHERE cash_back IS NOT NULL;
    COMMIT;
END;
$$ language plpgsql;

-- Procedure removes previous updates
CREATE OR REPLACE PROCEDURE drop_column_cash_back() AS
$$
BEGIN
    ALTER TABLE users DROP COLUMN cash_back;
    COMMIT;
END;
$$ language plpgsql;

-- Call this procedure to update table
call add_column_cash_back();
-- Call this procedure to restore table
call drop_column_cash_back();
-- Call this procedure to clear cash_back
call clear_column_cash_back();

-- Delete function set_cash_back
DROP FUNCTION set_cash_back(rate float);
-- Call function set_cash_back
SELECT set_cash_back(0.01, '2000-03-05');
SELECT set_cash_back(0.01, now()::date);

-- Calculates the cash back for all finished orders after the specified date
CREATE OR REPLACE FUNCTION set_cash_back(
    rate float,
    date date) RETURNS float AS
$$
DECLARE
    rec record;
    total_cashback numeric(22,3) := 0;
    temp_cashback numeric(22,3);
BEGIN
    total_cashback = 0;
    FOR rec IN
        SELECT users.user_id, users.cash_back, orders.total,
                order_statuses.status_name, orders.updated_at FROM users
                INNER JOIN carts USING (user_id)
                INNER JOIN orders USING (cart_id)
                INNER JOIN order_statuses USING (order_status_id)
    LOOP
        IF rec.status_name ilike ('finished') AND rec.updated_at > date THEN
            temp_cashback := rec.cash_back + rec.total * rate;
            total_cashback := total_cashback + temp_cashback;
            UPDATE users SET cash_back = temp_cashback
                WHERE users.user_id = rec.user_id;
        END IF;
    END LOOP;
    RETURN total_cashback;
END;
$$ language plpgsql;

-- $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
--TASK 2.3

-- Delete function get_orders_sum_by_statuses
DROP FUNCTION get_orders_sum_by_statuses(date date);

-- Call function get_orders_sum_by_statuses
SELECT get_orders_sum_by_statuses();
SELECT get_orders_sum_by_statuses('2021-12-12');
SELECT get_orders_sum_by_statuses('2020-12-12');
SELECT get_orders_sum_by_statuses('2022-05-12');

--Create function get_orders_sum_by_statuses
CREATE OR REPLACE FUNCTION get_orders_sum_by_statuses(
    date date default now()::date
                                ) RETURNS table (
    status_name varchar,
    order_count numeric) AS
$$
-- Returns table with total sum of all orders after the specified date
BEGIN
    RETURN QUERY
        SELECT order_statuses.status_name, sum(orders.total) as order_count
            FROM orders INNER JOIN order_statuses USING (order_status_id)
            WHERE orders.created_at::date > date
            GROUP BY order_statuses.status_name;
    IF NOT FOUND THEN
        RAISE EXCEPTION 'No orders after date %', date;
    END IF;
END;
$$ language plpgsql;

-- $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
-- Clear all changes, functions and procedures
DROP FUNCTION shipping_total(input_city varchar);
DROP FUNCTION get_products_in_stock();
DROP FUNCTION set_cash_back(rate float, date date);
call drop_column_cash_back();
DROP procedure clear_column_cash_back();
DROP procedure add_column_cash_back();
DROP procedure drop_column_cash_back();
DROP procedure get_orders_sum_by_statuses(date date);
