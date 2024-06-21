# BTC Prices with Celery, Redis and Flask
Retrieving Bitcoin prices for various currencies.
This example implements asynchronous task management using Celery.

The application contains a series of services that perform the following tasks:

- Definition of currencies.
- Downloading Bitcoin prices for the defined currencies using requests, which are then stored in MongoDB in their respective collections.
- Generating a graph of the last 50 values obtained with Matplotlib.
- Displaying graphs through an API built with Flask.

Currently the defined currencies are: ARS, USD, EUR, and DKK.


#### Tools / Frameworks

![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![Celery](https://img.shields.io/badge/celery-%23a9cc54.svg?style=for-the-badge&logo=celery&logoColor=ddf4a4)
![Redis](https://img.shields.io/badge/redis-%23DD0031.svg?style=for-the-badge&logo=redis&logoColor=white)
![MongoDB](https://img.shields.io/badge/MongoDB-%234ea94b.svg?style=for-the-badge&logo=mongodb&logoColor=white)
![Matplotlib](https://img.shields.io/badge/Matplotlib-%23ffffff.svg?style=for-the-badge&logo=Matplotlib&logoColor=black)
![Flask](https://img.shields.io/badge/flask-%23000.svg?style=for-the-badge&logo=flask&logoColor=white)
![Docker](https://img.shields.io/badge/docker-%230db7ed.svg?style=for-the-badge&logo=docker&logoColor=white)
