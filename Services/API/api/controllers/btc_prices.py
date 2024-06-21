from flask import Blueprint, render_template

btc_prices_bp = Blueprint('btc_prices', __name__)
@btc_prices_bp.route('/plot/<currency>', methods=['GET'])
def plot(currency):
    image_filename = f'plot_{currency}.png'
    return render_template('plot.html', image_filename=image_filename, currency=currency)