up:
	sudo docker-compose --env-file ./.env up -d
config:
	sudo docker-compose config
ps:
	sudo docker-compose ps
db:
	sudo docker-compose --env-file ./.env exec db psql -U postgres -c "CREATE DATABASE ${name};"
put:
	sudo docker cp ./db/potential_users.csv db_docker_db_1:/usr/src/potential_users.csv
copy:
	sudo docker-compose --env-file ./.env exec db psql -U postgres -c "COPY potential_customers FROM '/usr/src/potential_users.csv' DELIMITER ',';"
stop:
	sudo docker-compose down
clear:
	sudo docker system prune -a
table:
	sudo docker-compose --env-file ./.env exec db psql -U postgres -c "CREATE TABLE IF NOT EXISTS potential_customers (id INT NOT NULL,email VARCHAR(255),name VARCHAR(255),surname VARCHAR(255),second_name VARCHAR(255),city VARCHAR(255),PRIMARY KEY (id));"