#!/bin/bash

# Iniciar el cron
cron

# Ejecutar el comando de celery
exec celery -A main worker -E --loglevel=info -c 1