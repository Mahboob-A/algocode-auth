#!/bin/bash 

set -o errexit 

set -o nounset

exec watchfiles celery.__main__.main \
    --args \
    "-A algocode_backend.celery -b \"${CELERY_BROKER_URL}\" flower --basic_auth=\"${CELERY_FLOWER_USER}:${CELERY_FLOWER_PASSWORD}\""