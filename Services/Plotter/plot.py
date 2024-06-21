import matplotlib.pyplot as plt
import logging

# Configurar logging
logging.basicConfig(level=logging.DEBUG, handlers=[logging.StreamHandler()])
logger = logging.getLogger(__name__)

def plot(currency, data):
    try:
        dates = []
        values = []

        for d in data:
            dates.append(d['date'])
            values.append(d['bitcoin'][currency])

        #Revertimos resultados.
        dates.reverse()
        values.reverse()

        #Creamos figura.
        plt.figure(figsize=(10, 5))
        plt.plot(dates, values, marker='o')

        # Personalizar la gráfica
        plt.title(f'Plot for btc{currency} values.')
        plt.xlabel('date')
        plt.ylabel('value')
        plt.xticks(rotation=45)
        plt.grid(True)

        # Guardar la gráfica como un archivo PNG
        plt.tight_layout()
        plt.savefig(f'/app/plot_images/plot_{currency}.png', format='png')
    except Exception as e:
        logger.error(e, exc_info=True)