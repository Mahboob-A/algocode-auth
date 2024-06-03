

# ### Docker management commands 
 
docker-up: 
	docker compose -p algocode_backend -f dev.yml up --build -d --remove-orphans 

docker-down: 
	docker compose -p algocode_backend -f dev.yml down

docker-down-v: 
	docker compose -p algocode_backend -f dev.yml down -v

docker-logs: 
	docker compose -p algocode_backend -f dev.yml logs 

docker-logs-api: 
	docker compose -p algocode_backend -f dev.yml logs api 

docker-restart-api: 
	docker compose -p algocode_backend -f dev.yml restart api 

docker-exec-api: 
	docker compose -p algocode_backend -f dev.yml exec api /bin/bash 

docker-check-deploy:
	docker compose -p algocode_backend -f dev.yml run --rm api python manage.py check --deploy 

# ## 


# ### Docker Volume and Postgres Database 

docker-volume: 
	docker volume inspect src_dev_postgres_data

docker-exec-postgres: 
	docker compose -p algocode_backend -f dev.yml exec postgres /bin/bash 

algocode-database: 
	docker compose -p algocode_backend -f dev.yml exec postgres psql --username=mahboob --dbname=algocode-db 

# ## 



# ### Services logs commands 

docker-logs-celery:
	docker compose -p algocode_backend -f dev.yml logs celery_worker

docker-logs-redis:
	docker compose -p algocode_backend -f dev.yml logs redis-for-celery

docker-logs-flower:
	docker compose -p algocode_backend -f dev.yml logs flower

docker-logs-mailhog:
	docker compose -p algocode_backend -f dev.yml logs mailhog

docker-logs-postgres: 
	docker compose -p algocode_backend -f dev.yml logs postgres

# ## 



# ### Django Commands

makemigrations: 
	docker compose -p algocode_backend -f dev.yml run --rm api python manage.py makemigrations

migrate: 
	docker compose -p algocode_backend -f dev.yml run --rm api python manage.py migrate

collectstatic: 
	docker compose -p algocode_backend -f dev.yml run --rm api python manage.py collectstatic --no-input --clear 

superuser: 
	docker compose -p algocode_backend -f dev.yml run --rm api python manage.py createsuperuser 

# ## 

