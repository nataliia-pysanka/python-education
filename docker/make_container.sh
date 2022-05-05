#!/bin/bash
sudo docker-compose --env-file ./.env up -d
sudo docker-compose ps
#docker_db_1
sudo docker cp ./pagila-schema.sql docker_db_1:/usr/src/pagila-schema.sql
sudo docker cp ./pagila-insert-data.sql docker_db_1:/usr/src/pagila-insert-data.sql
sudo docker-compose --env-file ./.env exec db psql -U postgres -c "CREATE DATABASE pagila;"
sudo docker-compose --env-file ./.env exec db psql -U postgres -d pagila -f /usr/src/pagila-schema.sql
sudo docker-compose --env-file ./.env exec db psql -U postgres -d pagila -f /usr/src/pagila-insert-data.sql
