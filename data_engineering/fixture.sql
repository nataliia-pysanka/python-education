CREATE TABLE IF NOT EXISTS covid_data (
    date_notif date,
    country varchar,
    code_region smallint,
    name_region varchar,
    code_province smallint,
    name_province varchar,
    abreviature_province varchar,
    latitude numeric,
    longitude numeric,
    total_cases int,
    notes text
);