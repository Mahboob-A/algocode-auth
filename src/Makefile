

# ### Docker management commands 
 
docker-up: 
	docker compose -f dev.yml up --build -d --remove-orphans 

docker-down: 
	docker compose -f dev.yml down

docker-down-v: 
	docker compose -f dev.yml down -v

docker-logs: 
	docker compose -f dev.yml logs 

docker-logs-api: 
	docker compose -f dev.yml logs api 

docker-restart-api: 
	docker compose -f dev.yml restart api 

docker-exec-api: 
	docker compose -f dev.yml exec api /bin/bash 

# ## 


# ### Docker Volume and Postgres Database 

docker-volume: 
	docker volume inspect src_dev_postgres_data

docker-exec-postgres: 
	docker compose -f dev.yml exec postgres /bin/bash 

algocode-database: 
	docker compose -f dev.yml exec postgres psql --username=mahboob --dbname=algocode-db 

# ## 



# ### Services logs commands 

docker-logs-celery:
	docker compose -f dev.yml logs celery_worker

docker-logs-redis:
	docker compose -f dev.yml logs redis

docker-logs-flower:
	docker compose -f dev.yml logs flower

docker-logs-mailhog:
	docker compose -f dev.yml logs mailhog

docker-logs-postgres: 
	docker compose -f dev.yml logs postgres

# ## 



# ### Django Commands

makemigrations: 
	docker compose -f dev.yml run --rm api python manage.py makemigrations

migrate: 
	docker compose -f dev.yml run --rm api python manage.py migrate

collectstatic: 
	docker compose -f dev.yml run --rm api python manage.py collectstatic --no-input --clear 

superuser: 
	docker compose -f dev.yml run --rm api python manage.py createsuperuser 

# ## 

