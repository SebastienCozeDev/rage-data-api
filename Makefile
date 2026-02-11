help:	## Show this help message
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' Makefile | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-20s\033[0m %s\n", $$1, $$2}'

build-up:	## [DEV] Build and start the Docker containers
	docker compose -f docker-compose-dev.yml up --build

build-up-d:	## [DEV] Build and start the Docker containers in detached mode
	docker compose -f docker-compose-dev.yml up --build -d

build-up-prod:	## [PROD] Build and start the Docker containers
	docker compose -f docker-compose-dev.yml up --build

build-up-d-prod:	## [PROD] Build and start the Docker containers in detached mode
	docker compose -f docker-compose-dev.yml up --build -d

bash:	## Open a bash shell in the web container
	docker compose run rage-fastapi bash

run:	## Start the Docker containers
	docker compose up

make stop:	## Stop the Docker containers
	docker compose down
