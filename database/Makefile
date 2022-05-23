up:
	sudo docker-compose --env-file ./.env up -d
config:
	sudo docker-compose config
ps:
	sudo docker-compose ps
db:
	sudo docker-compose --env-file ./.env exec db psql -U postgres -c "CREATE DATABASE cs;"
table:
	sudo docker cp ./cs_create_tables.sql database_db_1:/usr/src/cs_create_tables.sql
	sudo docker-compose --env-file ./.env exec db psql -U postgres -d cs -f /usr/src/cs_create_tables.sql
copy:
	sudo docker cp ./data/car_model.csv database_db_1:/usr/src/car_model.csv
	sudo docker cp ./data/city.csv database_db_1:/usr/src/city.csv
	sudo docker cp ./data/customer.csv database_db_1:/usr/src/customer.csv
	sudo docker cp ./data/state.csv database_db_1:/usr/src/state.csv
	sudo docker cp ./data/zip.csv database_db_1:/usr/src/zip.csv
	sudo docker cp ./data/street.csv database_db_1:/usr/src/street.csv

	sudo docker cp ./cs_copy_data.sql database_db_1:/usr/src/cs_copy_data.sql
	sudo docker-compose --env-file ./.env exec db psql -U postgres -d cs -f /usr/src/cs_copy_data.sql
insert:
	sudo docker cp ./DB_function.sql database_db_1:/usr/src/DB_function.sql
	sudo docker-compose --env-file ./.env exec db psql -U postgres -d cs -f /usr/src/DB_function.sql

	sudo docker cp ./cs_insert_data.sql database_db_1:/usr/src/cs_insert_data.sql
	sudo docker-compose --env-file ./.env exec db psql -U postgres -d cs -f /usr/src/cs_insert_data.sql
stop:
	sudo docker-compose down
clear:
	sudo docker system prune -a
	sudo docker rm -f $(docker ps -a -q)
	sudo docker volume rm $(docker volume ls -q)
drop_data:
	sudo docker cp ./DB_drop.sql database_db_1:/usr/src/DB_drop.sql
	sudo docker-compose --env-file ./.env exec db psql -U postgres -d cs -f /usr/src/DB_drop.sql
