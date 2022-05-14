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
	sudo docker cp ./pagila-schema.sql docker_db_1:/usr/src/pagila-schema.sql
	sudo docker cp ./pagila-insert-data.sql docker_db_1:/usr/src/pagila-insert-data.sql
table:
	sudo docker-compose --env-file ./.env exec db psql -U postgres -c "CREATE DATABASE pagila;"
	sudo docker-compose --env-file ./.env exec db psql -U postgres -d pagila -f /usr/src/pagila-schema.sql
	sudo docker-compose --env-file ./.env exec db psql -U postgres -d pagila -f /usr/src/pagila-insert-data.sql
stop:
	sudo docker-compose down
clear:
	sudo docker system prune -a
