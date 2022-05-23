--Show cities with the no branch and counts of customers in them
SELECT city.name, count(customer.id_customer) FROM customer
    INNER JOIN zip USING (id_zip)
    INNER JOIN city USING (id_city)
    LEFT JOIN branch ON
        zip.id_zip = branch.id_zip
    WHERE branch.id_branch IS NULL
    GROUP BY city.name
    ORDER BY count(customer.id_customer) DESC;


--Show customers during the summer of 2020 from biggest term of rent to lowest
SELECT first_name ||' '||last_name as name, date_renting,
       (date_renting + (period::varchar||' day')::interval)::date as finish_date,
       sum(renting.period) FROM customer
    INNER JOIN renting USING (id_customer)
    WHERE date_renting >= '2020-06-01'::date AND
        date_renting + (period::varchar||' day')::interval <= '2020-08-30'::date
    GROUP BY name, date_renting, finish_date
    ORDER BY date_renting DESC;


-- Show average age of customers in each city they are live
SELECT DISTINCT
    state.name,
	city.name,
	AVG (EXTRACT (YEAR FROM now()::date) - EXTRACT (YEAR FROM birth))
	    OVER (PARTITION BY city.name
	)::integer
FROM
	customer
	INNER JOIN zip USING (id_zip)
	INNER JOIN city USING (id_city)
	INNER JOIN state USING (id_state);

