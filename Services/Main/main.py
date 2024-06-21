import os
from celery import Celery
import logging
from time import sleep
from Utilities.Queue import QueueInterface

####################################
#   Pedro Diaz - Junio 2024
#   main.py de Servicio Main
#
#       Iniciador de evento. Carga las currency's en Queue Downloader [redis] para
#           dar comienzo al funcionamiento del aplicativo.
#
####################################

# Configurar logging
logging.basicConfig(level=logging.DEBUG, handlers=[logging.StreamHandler()])
logger = logging.getLogger(__name__)

# Configurar broker y backend de Celery
broker = os.getenv('CELERY_BROKER', 'redis://redis:6379/0')
app = Celery('tasks', broker=broker, backend=broker)

# Definir la tarea main_event
@app.task(name='main_event')
def main_event():
    try:
        logger.info('Ha iniciado main_event.')

        downloader_queue = QueueInterface('Downloader')
        currencies = ['ars', 'eur', 'usd', 'dkk']
        for c in currencies:
            downloader_queue.add_to_queue(c, 'downloader')

        logger.info('Ha finalizado main_event.')

    except Exception as e:
        logger.error(e, exc_info=True)

if __name__ == '__main__':
    logger.info('==== Main Event ====')
    result = app.send_task('main_event')
    print(f'Task ID: {result.id}')
    print(f'Task result: {result.get()}')