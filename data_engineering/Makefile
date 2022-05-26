cnf ?= .env
include $(cnf)
export $(shell sed 's/=.*//' $(cnf))

build:
	sudo docker build -t $(APP_NAME):$(VERSION) -t $(APP_NAME):latest .
build-nc:
	sudo docker build --no-cache -t $(APP_NAME):$(VERSION) -t $(APP_NAME):latest .
up:
	sudo docker-compose --env-file ./.env up -d
config:
	sudo docker-compose config
ps:
	sudo docker-compose ps

logs:
	docker logs ${APP_NAME}

copy:
	sudo docker cp ./fixture.sql db-${APP_NAME}:/usr/src/fixture.sql
	sudo docker-compose --env-file ./.env exec db psql -U postgres -d ${POSTGRES_DB} -f /usr/src/fixture.sql
stop:
	sudo docker-compose down