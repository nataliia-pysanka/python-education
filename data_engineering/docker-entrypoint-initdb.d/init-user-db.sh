#!/bin/bash
set -e

psql -v ON_ERROR_STOP=1 --username "$POSTGRES_USER" --dbname "$POSTGRES_DB" <<-EOSQL
	CREATE USER covid_agent;
	CREATE DATABASE covid_data;
	GRANT ALL PRIVILEGES ON DATABASE covid_data TO covid_agent;
EOSQL