#!/bin/bash

set -o errexit 
set -o pipefail 
set -o nounset 

# check if POSTGRES_USER is empty, then add the default "postgres" as the user. 
if [ -z "${POSTGRES_USER}" ]; then 
    base_postgres_image_default_user='postgres'
    export POSTGRES_USER="${base_postgres_image_default_user}"
fi 

export DATABASE_URL="postgres://${POSTGRES_USER}:${POSTGRES_PASSWORD}@${POSTGRES_HOST}:${POSTGRES_PORT}/${POSTGRES_DB}"

python << END 
import sys 
import time 
import psycopg2

suggest_postgres_unrecoverable_after_time = 30
start_time = time.time()

while True: 
    try: 
        psycopg2.connect(
            dbname="${POSTGRES_DB}", 
            user="${POSTGRES_USER}", 
            password="${POSTGRES_PASSWORD}", 
            host="${POSTGRES_HOST}", 
            port="${POSTGRES_PORT}",
        )
        break
    except psycopg2.OperationalError as err: 
        sys.stderr.write("Waiting for PostgreSQL to become available ... \n")
        if time.time() - start_time > suggest_postgres_unrecoverable_after_time: 
            sys.stderr.write("This is taking longer than expected. The following may be the root cause "
            "for the error: '{}'\n".format(err))
    time.sleep(1)
END

>&2 echo "PostgresSQL is available"

exec "$@"