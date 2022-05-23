-- Function returns query with information about cars was rented full or partly
-- in the specified interval from specified date
CREATE OR REPLACE FUNCTION get_cars_used_in_interval(
    start_date date, input_interval int
) RETURNS table (
    zip_value char(20),
    city char(30),
    street char(50),
    phone char(15),
    model varchar,
    car_number varchar,
    date_rent date,
    interval_ smallint) AS
$$
DECLARE
    days interval;
BEGIN
    days := (input_interval::varchar||' day')::interval;
    RETURN QUERY
        SELECT zip.zip_value, city.name, branch.street, branch.phone,
               car_model.model, car.car_number, date_renting, period FROM renting
            INNER JOIN car USING (id_car)
            INNER JOIN car_model USING (id_car_model)
            INNER JOIN branch USING (id_branch)
            INNER JOIN zip USING(id_zip)
            INNER JOIN city USING(id_city)
            WHERE (date_renting >= start_date AND date_renting <= (start_date + days)) OR
                  (date_renting <= start_date AND date_renting + days > start_date AND
                        (date_renting + days <= (start_date + days) OR date_renting + days > (start_date + days)))
            ORDER BY date_renting;

    IF NOT FOUND THEN
        RAISE EXCEPTION 'No renting between % and %', start_date, start_date + days;
    END IF;
END;
$$ language plpgsql;

SELECT * FROM get_cars_used_in_interval('2020-01-05', 0);
SELECT * FROM get_cars_used_in_interval('2020-12-31', 10);
SELECT * FROM get_cars_used_in_interval('2021-08-01', 3);



-- returns the text with names, phones and dates of rent for the specified year
-- and branch zip value

CREATE OR REPLACE FUNCTION get_customers(show_year integer, show_zip varchar)
   RETURNS TEXT AS
$$
DECLARE
    customers text default '';
    rec_rent record;
    cur_renting CURSOR(show_year integer, show_zip varchar) FOR
		SELECT *
		FROM renting
		INNER JOIN car USING (id_car)
	    INNER JOIN branch USING (id_branch)
		INNER JOIN zip USING (id_zip)
		INNER JOIN customer USING (id_customer)
		WHERE EXTRACT (YEAR FROM date_renting)::int = show_year AND
		       zip_value = show_zip;
BEGIN
    OPEN cur_renting(show_year, show_zip);
       customers := 'Customers:';

       LOOP
          FETCH cur_renting into rec_rent;
          EXIT WHEN NOT found;

          customers := customers || rec_rent.first_name || ' ' || rec_rent.last_name
                           || '('  || rec_rent.phone || ') at ' || rec_rent.date_renting || ';';
       end loop;
       CLOSE cur_renting;
    RETURN customers;
END;
$$ language plpgsql;

SELECT * FROM get_customers(2020, '35226');




-- returns a random number between low and hight
CREATE OR REPLACE FUNCTION random_between(low INT ,high INT)
   RETURNS INT AS
$$
BEGIN
   RETURN floor(random() * (high-low + 1) + low);
END;
$$ language plpgsql;



-- function returns the date in the specified interval
CREATE OR REPLACE FUNCTION get_date(low int default 1960, hight int default 2000)
    RETURNS date AS
$$
DECLARE
    year_ smallint;
    month_ smallint;
    day_ smallint;
    date_ date;
BEGIN
    year_ = random_between(low, hight);
    month_ = random_between(1, 12);
    CASE month_
        WHEN 1, 3, 5, 7, 8, 10, 12 THEN
            day_ := random_between(1, 31);
        WHEN 2 THEN
            day_ := random_between(1, 28);
        ELSE
            day_ := random_between(1, 30);
    END CASE;
    date_ = (year_||'-'||month_||'-'||day_)::date;
    return date_;
end;
$$ language plpgsql;


-- returns a random numbers in the required amount
CREATE OR REPLACE FUNCTION random_numbers(num INT)
   RETURNS varchar AS
$$
DECLARE
    numbers varchar;
BEGIN
    IF num <= 0 THEN
        RETURN '';
    END if;
    SELECT array_to_string(ARRAY(SELECT chr((48 + round(random() * 9)) :: integer)
        FROM generate_series(1,num)), '') into numbers;
    RETURN numbers;
END;
$$ language plpgsql;

-- returns a random uppercase letters in the required amount
CREATE OR REPLACE FUNCTION random_letters(num INT)
   RETURNS varchar AS
$$
DECLARE
    letters varchar;
BEGIN
    IF num <= 0 THEN
        RETURN '';
    END if;
    SELECT array_to_string(ARRAY(SELECT chr((65 + round(random() * 25))::integer)
        FROM generate_series(1,num)), '') into letters;
    RETURN letters;
END;
$$ language plpgsql;


-- returns a random uppercase symbols and numbers in the required amount
CREATE OR REPLACE FUNCTION random_symbols(num INT)
   RETURNS varchar AS
$$
DECLARE
    chars text[] := '{0,1,2,3,4,5,6,7,8,9,A,B,C,D,E,F,G,H,I,J,K,L,M,N,O,P,Q,R,S,T,U,V,W,X,Y,Z}';
    symbols varchar := '';
BEGIN
    IF num <= 0 THEN
        RETURN '';
    END if;
    FOR i IN 1..num LOOP
        symbols := symbols||chars[1 + random() * (array_length(chars, 1)-1)];
    END LOOP;
    RETURN symbols;
END;
$$ language plpgsql;



-- generates phone number in format XXX-XXX-XXX-XXX
CREATE OR REPLACE FUNCTION get_phone_number()
   RETURNS varchar AS
$$
DECLARE
    phone_number varchar := '';
    num varchar;
BEGIN
    FOR i IN 1..4 LOOP
    num := random_numbers(3);
        IF i = 4 THEN
            phone_number := phone_number||num;
        ELSE
            phone_number := phone_number||num||'-';
        END IF;
    END LOOP;

    RETURN phone_number;
END;
$$ language plpgsql;



-- generate car number depending of state and year of car
CREATE OR REPLACE FUNCTION get_car_number(state int default 1, year int default 2000)
   RETURNS varchar AS
$$
DECLARE
    car_number varchar := '';
    prefix varchar := '';
    letters varchar := '';
    numbers varchar := '';
    delimiter varchar := '';
BEGIN
CASE state
    WHEN 1 THEN
        FOR i IN 1..random_between(1, 2) LOOP
            prefix := prefix||'0';
        END LOOP;
        letters := random_letters(2);
        numbers := random_numbers(5 - LENGTH(prefix));
        delimiter := ' ';
    WHEN 2, 12, 15, 16, 18, 23, 25, 28 THEN
        letters := random_letters(3);
        numbers := random_numbers(3);
        delimiter := ' ';
    WHEN 3, 4, 8, 26 THEN
        letters := random_symbols(3);
        numbers := random_symbols(3);
        delimiter := ' ';
    WHEN 5 THEN
        letters := random_symbols(7);
    WHEN 6, 24 THEN
        letters := random_symbols(3);
        numbers := random_symbols(3);
        delimiter := '-';
    WHEN 7 THEN
        delimiter := '•';
        CASE
            WHEN year BETWEEN 2000 AND 2013 THEN
                letters := random_numbers(3);
                numbers := random_letters(3);
            WHEN year > 2015 THEN
                letters := random_letters(2);
                numbers := random_letters(5);
            WHEN year BETWEEN 2013 AND 2015 THEN
                prefix := '1';
                letters := random_numbers(2);
                numbers := random_symbols(3);
            ELSE
                prefix := '1';
                letters := random_symbols(5);
            END CASE;
    WHEN 9 THEN
        letters := random_letters(2);
        numbers := random_letters(4);
        delimiter = '-';
    WHEN 10 THEN
        CASE
            WHEN year BETWEEN 2006 AND 2009 THEN
                letters := random_numbers(3);
                numbers := random_letters(3);
                delimiter = ' ';
            WHEN year < 2006 THEN
                letters := random_symbols(3);
                numbers := random_symbols(3);
                delimiter := ' ';
            ELSE
                letters := random_letters(3);
                numbers := random_symbols(3);
                delimiter := ' ';
            END CASE;
    WHEN 11 THEN
        letters := random_letters(3);
        numbers := random_numbers(4);
    WHEN 13 THEN
        CASE random_between(1, 7)
            WHEN 1 THEN
                prefix := 'A ';
                numbers := random_numbers(6);
            WHEN 2 THEN
                prefix := '0A ';
                numbers := random_numbers(5);
            WHEN 3 THEN
                prefix := '0A ';
                letters := random_letters(1);
                numbers := random_numbers(4);
            WHEN 4 THEN
                prefix := '0A ';
                letters := random_letters(2);
                numbers := random_numbers(3);
            WHEN 5 THEN
                prefix := '0A ';
                letters := random_numbers(4);
                numbers := random_letters(1);
            ELSE
                prefix := '00A ';
                numbers := random_numbers(4);
            END CASE;
    WHEN 14 THEN
        CASE
        WHEN year > 2017 THEN
            letters := random_letters(2);
            numbers := random_numbers(5);
            delimiter := ' ';
        ELSE
            prefix := random_letters(2);
            letters := random_numbers(1);
            numbers := random_numbers(4);
            delimiter := ' ';
        END CASE;
    WHEN 17, 22 THEN
        letters := random_numbers(3);
        numbers := random_letters(3);
    WHEN 19 THEN
        CASE
            WHEN year > 2016 THEN
                letters := random_numbers(3);
                numbers := random_letters(3);
                delimiter := ' ';
            ELSE
                letters := random_letters(3);
                numbers := random_numbers(3);
                delimiter := ' ';
            END CASE;
    WHEN 20 THEN
        letters := random_numbers(4);
        numbers := random_letters(2);
        delimiter := ' ';
    WHEN 21 THEN
        prefix := random_numbers(1);
        letters := random_numbers(2);
        numbers := random_letters(4);
    WHEN 27 THEN
        letters := random_letters(3);
        numbers := random_numbers(3);
    WHEN 29 THEN
        letters := random_numbers(3);
        numbers := random_symbols(3);
        delimiter = '·';
    WHEN 30 THEN
        letters := random_numbers(3);
        numbers := random_numbers(4);
        delimiter = ' ';
    WHEN 31 THEN
        CASE
            WHEN year >= 2010 THEN
                letters := random_symbols(3);
                numbers := random_letters(3);
                delimiter = '-';
            ELSE
                letters := random_letters(3);
                numbers := random_symbols(3);
                delimiter = '-';
        END CASE;
    WHEN 32 THEN
        letters := random_numbers(3);
        numbers := random_letters(3);
        delimiter = '-';
    WHEN 33, 34, 36, 39, 44, 47 THEN
        letters := random_letters(3);
        numbers := random_numbers(4);
        delimiter = '-';
    WHEN 35, 38, 41, 46, 49 THEN
        letters := random_numbers(3);
        numbers := random_letters(3);
        delimiter = ' ';
    WHEN 37 THEN
        letters := random_letters(3);
        numbers := random_numbers(3);
        delimiter = '-';
    WHEN 40 THEN
        letters := random_symbols(6);
    WHEN 42 THEN
        prefix := '00';
        letters := random_letters(1);
        numbers := random_numbers(3);
        delimiter = ' ';
    WHEN 43 THEN
        CASE
            WHEN year <= 2016 THEN
                prefix := random_letters(1);
                letters := random_numbers(2);
                numbers := random_symbols(3);
                delimiter = '-';
            ELSE
                letters := random_symbols(3);
                numbers := random_symbols(3);
                delimiter = '-';
        END CASE;
    WHEN 45 THEN
        letters := random_symbols(5);
    WHEN 48 THEN
        letters := random_letters(3);
        numbers := random_numbers(4);
    WHEN 50 THEN
        delimiter = '-';
        CASE
            WHEN year <= 2017 THEN
                letters := random_numbers(3);
                numbers := random_letters(3);
            ELSE
                letters := random_letters(3);
                numbers := random_numbers(4);
        END CASE;
    WHEN 51 THEN
        prefix := '00';
        numbers := random_letters(5);
        delimiter = '-';
    ELSE
        letters := random_letters(3);
        numbers := random_numbers(4);
    END CASE;

    car_number := prefix||letters||delimiter||numbers;
    RETURN car_number;
END;
$$ language plpgsql;