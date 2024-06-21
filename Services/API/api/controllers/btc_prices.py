from flask import Blueprint, render_template

#   Pedro Diaz | Junio 2024
#       btc_prices.py
#           Controlador que contiene único método GET.
#               Lo utilizamos en el template plot.html donde se
#               visualiza imagen de ploteo.           
#

btc_prices_bp = Blueprint('btc_prices', __name__)
@btc_prices_bp.route('/plot/<currency>', methods=['GET'])
def plot(currency):
    image_filename = f'plot_{currency}.png'
    return render_template('plot.html', image_filename=image_filename, currency=currency)