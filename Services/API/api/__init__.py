from flask import Flask, send_from_directory

#   Pedro Díaz | Junio 2024
#   create_app
#       Función que retorna el objeto app (Flask)
#       Es utilizado en run.py para dar inicio a la REST API
#
#       Redefinimos 'static' mediante serve_image.
#

def create_app():
    app = Flask(__name__, static_folder='/app/plot_images', static_url_path='/plot_images')

    @app.route('/plot_images/<path:filename>')
    def serve_image(filename):
        return send_from_directory(app.static_folder, filename)

    from api.controllers.btc_prices import btc_prices_bp
    app.register_blueprint(btc_prices_bp)
    return app