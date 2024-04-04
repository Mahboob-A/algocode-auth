# 040424, Thursday, 09.00 am 
# Steps (multistage buils)
# 1. Build Dependecy Wheels 
# 2. RUN Application 


ARG PYTHON_VERSION=3.10-bullseye


FROM python:${PYTHON_VERSION} as python 


# 1. Python Dependency Wheels | Build Stage 1 
FROM python as python-build-stage
ARG BUILD_ENVIRONMENT=dev 

RUN apt-get update && apt-get install --no-install-recommends -y \
        build-essential \
        libpq-dev 

COPY ./requirements . 


RUN pip wheel --wheel-dir /usr/src/app/wheel \
        -r ${BUILD_ENVIRONMENT}.txt 



# Run the Application | Build Stage 2

# image 
FROM python as python-run-stage 

# args
ARG BUILD_ENVIRONMENT=dev 
ARG APP_HOME=/app 

# envs 
ENV PYTHONDONTWRITEBYTECODE 1 
ENV PYTHONUNBUFFERED 1 
ENV BUILD_ENV ${BUILD_ENVIRONMENT}


WORKDIR ${APP_HOME}

RUN apt-get update && apt-get install --no-install-recommends -y \
        libpq-dev \
        gettext \
        && apt-get purge -y --auto-remove -o APT::AutoRemove::RecommendsImportant=false \
        && rm -rf /var/lib/apt/lists/*


COPY --from=python-build-stage /usr/src/app/wheel /wheels/

RUN pip install --no-cache-dir --no-index --find-links=/wheels/ /wheels/* \
        && rm -rf /wheels/ 


# check if database is ready from the entrypoint 
# copy the entrypoint 
COPY ./docker/dev/django/entrypoint.sh /entrypoint.sh

# tell docker that is unix based system not windows 
RUN sed -i 's/\r$//g' /entrypoint.sh

# give the user execution permission (+x) with chmod to /entrypoiny dir  
# checks the postgres db availability 
RUN chmod +x /entrypoint.sh


# copy the app 
COPY ./docker/dev/django/start /start

# tell docker that is unix based system not windows 
RUN sed -i 's/\r$//g' /start 

# give the user execution permission (+x) with chmod to /entrypoiny dir  
RUN chmod +x /start 


# start celery worker 
COPY ./docker/dev/django/celery/worker/start /start-celeryworker

RUN sed -i 's/\r$//g' /start-celeryworker

RUN chmod +x /start-celeryworker

# start flower to monitor celery 
COPY ./docker/dev/django/celery/flower/start /start-flower

RUN sed -i 's/\r$//g' /start-flower

RUN chmod +x /start-flower


COPY . ${APP_HOME} 

ENTRYPOINT ["/entrypoint.sh"]
