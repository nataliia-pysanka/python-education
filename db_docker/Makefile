up:
	sudo docker-compose --env-file ./.env up -d
config:
	sudo docker-compose config
ps:
	sudo docker-compose ps
db:
	sudo docker-compose --env-file ./.env exec db psql -U postgres -c "CREATE DATABASE ${name};"
stop:
	sudo docker-compose down
clear:
	sudo docker system prune -a
