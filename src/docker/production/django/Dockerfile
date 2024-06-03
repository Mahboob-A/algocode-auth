# 030624, Monday, 07.00 am 
# Steps (multistage buils)
# 1. Build Dependecy Wheels 
# 2. RUN Application 


ARG PYTHON_VERSION=3.10-bullseye



FROM python:${PYTHON_VERSION} as python 


# 1. Python Dependency Wheels | Build Stage 1 
FROM python as python-build-stage
ARG BUILD_ENVIRONMENT=production

RUN apt-get update && apt-get install --no-install-recommends -y \
        build-essential \
        libpq-dev 

COPY ./requirements . 


RUN pip wheel --wheel-dir /usr/src/app/wheel \
        -r ${BUILD_ENVIRONMENT}.txt 



# Run the Application | Build Stage 2

# image 
FROM python as python-run-stage 

RUN addgroup --system algocode && adduser --system --ingroup algocode algocode 

# args
ARG BUILD_ENVIRONMENT=production
ARG APP_HOME=/home/algocode/app 

# envs 
ENV PYTHONDONTWRITEBYTECODE 1 
ENV PYTHONUNBUFFERED 1 
ENV BUILD_ENV ${BUILD_ENVIRONMENT}


WORKDIR ${APP_HOME}


# creating an user for the backend. (algocode is the user and group)


#  create staticfiles dir, and give permission of the dir to the user. 
RUN mkdir -p ${APP_HOME}/staticfiles ${APP_HOME}/mediafiles && \
        chown -R algocode:algocode ${APP_HOME}/staticfiles ${APP_HOME}/mediafiles && \
        chmod -R 775 ${APP_HOME}/staticfiles ${APP_HOME}/mediafiles



RUN apt-get update && apt-get install --no-install-recommends -y \
        libpq-dev \
        gettext netcat \
        && apt-get purge -y --auto-remove -o APT::AutoRemove::RecommendsImportant=false \
        && rm -rf /var/lib/apt/lists/*


COPY --from=python-build-stage /usr/src/app/wheel /wheels/

RUN pip install --no-cache-dir --no-index --find-links=/wheels/ /wheels/* \
        && rm -rf /wheels/ 



# copy the entrypoint as the user 
COPY --chown=algocode:algocode ./docker/production/django/entrypoint.sh /entrypoint.sh

# unix based system 
RUN sed -i 's/\r$//g' /entrypoint.sh

# give the user execution permission (+x) with chmod to /entrypoiny dir  
# checks the postgres db availability 
RUN chmod +x /entrypoint.sh


# copy the start script as the user 
COPY --chown=algocode:algocode ./docker/production/django/start /start

RUN sed -i 's/\r$//g' /start 

# give the user execution permission (+x) with chmod to /entrypoiny dir  
RUN chmod +x /start 


# copy elery worker script as the user
COPY --chown=algocode:algocode ./docker/production/django/celery/worker/start /start-celeryworker

RUN sed -i 's/\r$//g' /start-celeryworker

RUN chmod +x /start-celeryworker

# copy the flower script as the user. it monitors the celery worker. 
# TODO check if project is running and working as expected, else do not chage the ownership of flower. 
COPY --chown=algocode:algocode ./docker/production/django/celery/flower/start /start-flower

RUN sed -i 's/\r$//g' /start-flower

RUN chmod +x /start-flower


COPY --chown=algocode:algocode . ${APP_HOME} 



# ownership of APP_HOME
RUN chown algocode:algocode ${APP_HOME}nx: 
#   build: 
#     context: . 
#     dockerfile: ./docker/production/nginx/Dockerfile
#   restart: always
#   depends_on: 
#     - api 
#   volumes: 
#     - static_volume:/app/staticfiles
#     - media_volume:/app/mediafiles 
#   ports: 
#     - "8080:80"
#   networks: 
#     - algocode-backend-reverse-proxy-network

USER algocode

ENTRYPOINT ["/entrypoint.sh"]
