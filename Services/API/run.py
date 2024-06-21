from api import create_app

#   Pedro Diaz | Junio 2024
#       run.py
#       Puerta de entrada de aplicación

app = create_app()

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)