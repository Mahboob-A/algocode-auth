

# ### Docker management commands 
 
docker-up: 
	docker compose -p algocode_auth_service -f production.yml up --build -d --remove-orphans 

docker-down: 
	docker compose -p algocode_auth_service -f production.yml down

docker-down-v: 
	docker compose -p algocode_auth_service -f production.yml down -v

docker-logs: 
	docker compose -p algocode_auth_service -f production.yml logs 

docker-logs-api: 
	docker compose -p algocode_auth_service -f production.yml logs api 

docker-restart-api: 
	docker compose -p algocode_auth_service -f production.yml restart api 

docker-exec-api: 
	docker compose -p algocode_auth_service -f production.yml exec api /bin/bash 

docker-check-deploy:
	docker compose -p algocode_auth_service -f production.yml run --rm api python manage.py check --deploy 

# ## 


# ### Docker Volume and Postgres Database 

docker-exec-postgres: 
	docker compose -p algocode_auth_service -f production.yml exec postgres /bin/bash 

algocode-database: 
    docker compose -p algocode_auth_service -f production.yml exec postgres psql --username="$(POSTGRES_USER)" --dbname="$(POSTGRES_DB)" 

# ## 



# ### Services logs commands 

docker-logs-celery:
	docker compose -p algocode_auth_service -f production.yml logs celery_worker

docker-logs-redis:
	docker compose -p algocode_auth_service -f production.yml logs redis-for-celery

docker-logs-flower:
	docker compose -p algocode_auth_service -f production.yml logs flower

docker-logs-postgres: 
	docker compose -p algocode_auth_service -f production.yml logs postgres

# ## 



# ### Django Commands

makemigrations: 
	docker compose -p algocode_auth_service -f production.yml run --rm api python manage.py makemigrations

migrate: 
	docker compose -p algocode_auth_service -f production.yml run --rm api python manage.py migrate

collectstatic: 
	docker compose -p algocode_auth_service -f production.yml run --rm api python manage.py collectstatic --no-input --clear 

superuser: 
	docker compose -p algocode_auth_service -f production.yml run --rm api python manage.py createsuperuser 

# ## 

