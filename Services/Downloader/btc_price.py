import requests
import logging
from datetime import datetime as dt

####################################
#   Pedro Diaz - Junio 2024
#   btc_price.py
#
#       Obtiene los precios para la currency recibida de coingecko.
#       Retorna objeto JSON con su respectivo valor y fecha actual de consulta.
####################################

# Configurar logging
logging.basicConfig(level=logging.DEBUG, handlers=[logging.StreamHandler()])
logger = logging.getLogger(__name__)

def get_btc_price(currency):
    try:
        logger.info(f'Obteniendo precio BTC (coingecko) para :{currency}')

        # Obtener la fecha y hora actuales
        now = dt.now()
        # Formatear la fecha y hora según el formato requerido (YYYY-mm-dd HH:MM)
        formatted_now = now.strftime('%Y-%m-%d %H:%M')

        url = 'https://api.coingecko.com/api/v3/simple/price'
        params = {
            'ids': 'bitcoin',
            'vs_currencies': currency
        }

        #Realizamos solicitud GET
        response = requests.get(url, params=params)
        if response.status_code == 200:
            # Convertir la respuesta a formato JSON
            prices = response.json()
            prices['date'] = formatted_now
            logger.info(f'Solicitud realizada con exito. Precio para {currency}: {prices}')
            return prices
        else:
            prices = None
            logger.error(f'Error en la solicitud. Error code: {response.status_code}')
            return prices
    except Exception as e:
        logger.error(e, exc_info=True)