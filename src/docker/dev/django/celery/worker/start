#!/bin/bash 

set -o errexit 

set -o nounset 

exec watchfiles celery.__main__.main --args '-A algocode_backend.celery worker -l INFO' 
 