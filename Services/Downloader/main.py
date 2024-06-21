import os
from celery import Celery
import logging
from time import sleep
from btc_price import get_btc_price
from Utilities.mongoConnection import MongoConnection
from Utilities.Queue import QueueInterface

####################################
#   Pedro Diaz - Junio 2024
#   downloader.py de Servicio Downloader
#
#       Ejecutor de descargas de todas las currencies.
#       Almacena en MongoDB. Crea QueueInterface para Plotters.
#
####################################

# Configurar logging
logging.basicConfig(level=logging.DEBUG, handlers=[logging.StreamHandler()])
logger = logging.getLogger(__name__)

# Configurar broker y backend de Celery
broker = os.getenv('CELERY_BROKER', 'redis://redis:6379/0')
app = Celery('tasks', broker=broker, backend=broker)

# Definir la tarea downloader
@app.task(name='downloader')
def downloader(currency):
    try:
        logger.info('Se ha iniciado task downloader.')
        logger.info(f'Moneda recibida: {currency}')

        price = get_btc_price(currency)
        if price is not None:
            logger.info(f'Valor obtenido en Task downloader: {price}')
            #Procedemos a almacenar en coleccion de mongo.
            mongo_conn = MongoConnection()
            mongo_conn.set_collection(f'btc{currency}')
            mongo_conn.collection.insert_one(price)
            logger.info(f'Valor para {currency} agregado a MongoDB.')
        else:
            logger.error(f'Ocurrió un error al obtener el valor btc de {currency}')

        #Creamos QueueInterfaces para Plotter.
        plotter_queue = QueueInterface('Plotter')
        #Agregamos a Queue el currency.
        plotter_queue.add_to_queue(currency)



        logger.info('La task downloader ha finalizado.')
    except Exception as e:
        logger.error(e, exc_info=True)