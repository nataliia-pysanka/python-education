EXPLAIN ANALYZE
SELECT
    a.first_name ||' '|| a.last_name as actor_name,
    c.name as film_category,
    count(c.name)
FROM
    actor a
    INNER JOIN film_actor fa ON a.actor_id = fa.actor_id
    INNER JOIN film f ON fa.film_id = f.film_id
    LEFT JOIN film_category fc
        ON f.film_id = fc.film_id
    INNER JOIN category c
    ON fc.category_id = c.category_id
    WHERE fc.film_id IS NOT NULL
GROUP BY actor_name, film_category
ORDER BY
    actor_name,
    count(c.name) DESC;
-- Sort  (cost=808.27..821.93 rows=5462 width=108) (actual time=550.757..578.778 rows=2596 loops=1)
-- Planning Time: 6.950 ms
-- Execution Time: 607.469 ms

CREATE INDEX idx_actor_name ON actor USING btree (first_name, first_name);
-- Planning Time: 2.264 ms
-- Execution Time: 851.911 ms
-- Result became worse
DROP INDEX idx_actor_name;
-- Planning Time: 2.802 ms
-- Execution Time: 558.206 ms
-- Result became better

DROP INDEX idx_actor_first_name;
DROP INDEX idx_actor_last_name;
-- Planning Time: 2.101 ms
-- Execution Time: 750.537 ms
-- Result became worse


CREATE INDEX idx_actor_first_name ON actor(first_name);
-- Planning Time: 2.339 ms
-- Execution Time: 639.438 ms

CREATE INDEX idx_actor_last_name ON actor(last_name);
-- Planning Time: 2.824 ms
-- Execution Time: 612.028 ms
-- Index on last_name doesn't make better result

CREATE INDEX idx_name ON category USING btree (name);
-- Planning Time: 6.579 ms
-- Execution Time: 601.586 ms
-- Result became a little better

DROP INDEX idx_name;
CREATE INDEX idx_name ON category USING hash (name);
-- Sort  (cost=505.81..510.93 rows=2048 width=108) (actual time=535.396..558.854 rows=2596 loops=1)
-- Planning Time: 2.596 ms
-- Execution Time: 574.141 ms
-- Result became a much better

-- ----------------------------------------------------------------------------
EXPLAIN ANALYZE
SELECT
    c.first_name||' '||c.last_name as name,
    count(p.amount)
FROM
    payment p
     LEFT JOIN rental r ON p.rental_id = r.rental_id
     INNER JOIN customer c on c.customer_id = r.customer_id
     WHERE r.rental_id IS NOT NULL
GROUP BY name
ORDER BY name;
-- Sort  (cost=1177.73..1179.23 rows=599 width=40) (actual time=2310.893..2317.953 rows=599 loops=1)
-- Planning Time: 1.005 ms
-- Execution Time: 2326.685 ms

CREATE INDEX idx_customer_first_name ON customer USING btree (first_name);
-- Planning Time: 13.818 ms
-- Execution Time: 3038.487 ms
-- Result became worse

DROP INDEX idx_customer_first_name;
CREATE INDEX idx_customer_first_name ON customer USING hash (first_name);
-- Planning Time: 1.053 ms
-- Execution Time: 2156.349 ms
-- Result became a little better

-- DROP INDEX idx_customer_last_name;
-- This index doesn't change result

-- ----------------------------------------------------------------------------

EXPLAIN ANALYZE
SELECT
    city.city,
    c.country,
    cs.first_name||' '||cs.last_name as name
FROM
    city
    LEFT JOIN country c on city.country_id = c.country_id
    LEFT JOIN address a on city.city_id = a.city_id
    RIGHT OUTER JOIN customer cs on cs.address_id = a.address_id
    WHERE a.address_id IS NOT NULL
ORDER BY city, country;
-- Sort  (cost=93.93..95.43 rows=599 width=50) (actual time=111.968..117.397 rows=599 loops=1)
-- Planning Time: 3.847 ms
-- Execution Time: 122.661 ms

CREATE INDEX idx_country ON country USING hash (country);
-- Planning Time: 1.064 ms
-- Execution Time: 156.576 ms
-- Result became worse

DROP INDEX idx_country;
CREATE INDEX idx_country ON country USING btree (country);
-- Planning Time: 0.677 ms
-- Execution Time: 116.597 ms
-- Result became a little better

CREATE INDEX idx_city ON city USING btree (city);
-- Planning Time: 1.171 ms
-- Execution Time: 123.434 ms
-- No betters