import os
from celery import Celery
import logging
from time import sleep
from Utilities.Queue import QueueInterface
from Utilities.mongoConnection import MongoConnection
from plot import plot

####################################
#   Pedro Diaz - Junio 2024
#   main.py de Servicio Plotter
#
#       Realiza plot del argumento currency. Como máximo plottea 50 elementos.
#       Almacena resultado de plotteo en imagen .PNG
####################################

# Configurar logging
logging.basicConfig(level=logging.DEBUG, handlers=[logging.StreamHandler()])
logger = logging.getLogger(__name__)

# Configurar broker y backend de Celery
broker = os.getenv('CELERY_BROKER', 'redis://redis:6379/0')
app = Celery('tasks', broker=broker, backend=broker)

@app.task(name='plotter')
def plotter_event(currency):
    try:
        logger.info(f'Comienzo de plotteo para: {currency}')
        mongo_conn = MongoConnection()
        logger.info('Conexión a MongoDB establecida.')
        mongo_conn.set_collection(f'btc{currency}')
        logger.info(f'Cambio a collection: btc{currency}')
        result = mongo_conn.collection.find().sort('date', -1).limit(50)
        result = list(result)
        logger.info(f'Resultados obtenidos: {result}')

        logger.info(f'Realizando gráfico para: {currency}')
        plot(currency,result)
        logger.info(f'Grafico finalizado para: {currency}')
    except Exception as e:
        logger.error(e, exc_info=True)