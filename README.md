# BTC Prices with Celery, Redis and Flask
Retrieving Bitcoin prices for various currencies.
This example implements asynchronous task management using Celery. Flower is used for visualizing the state and execution of tasks.

The application contains a series of services that perform the following tasks:

- Definition of currencies.
- Downloading Bitcoin prices for the defined currencies using requests, which are then stored in MongoDB in their respective collections.
- Generating a graph of the last 50 values obtained with Matplotlib.
- Displaying graphs through an API built with Flask.

Currently the defined currencies are: ARS, USD, EUR, and DKK.


#### Tools / Frameworks

![Bitcoin](https://img.shields.io/badge/Bitcoin-000?style=for-the-badge&logo=bitcoin&logoColor=white)
![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![Celery](https://img.shields.io/badge/celery-%23a9cc54.svg?style=for-the-badge&logo=celery&logoColor=ddf4a4)
![Redis](https://img.shields.io/badge/redis-%23DD0031.svg?style=for-the-badge&logo=redis&logoColor=white)
![MongoDB](https://img.shields.io/badge/MongoDB-%234ea94b.svg?style=for-the-badge&logo=mongodb&logoColor=white)
![Matplotlib](https://img.shields.io/badge/Matplotlib-%23ffffff.svg?style=for-the-badge&logo=Matplotlib&logoColor=black)
![Flask](https://img.shields.io/badge/flask-%23000.svg?style=for-the-badge&logo=flask&logoColor=white)
![Docker](https://img.shields.io/badge/docker-%230db7ed.svg?style=for-the-badge&logo=docker&logoColor=white)

## Pre - requisites

You need to have Docker & docker-compose installed. For more information, visit  [this link](https://docs.docker.com/manuals/).

You also need Git installed. You can download it [here](https://git-scm.com/downloads)

## Installation

Download the repository using the following command:
```
git clone https://github.com/akak92/celery-redis-example.git
```

#### Initialize the services

Execute the following commands to initialize the containers:
```
docker-compose build
```
And then:
```
docker-compose up -d
```
The container will initialize in the background, thanks to the `-d` argument. Remember that to view the logs of the services, you can use the command:
```
docker logs <CONTAINER_NAME>
```

And with that last step, we have completed the installation.

#### Flower visualization

Flower is an open-source web application for monitoring and managing Celery clusters. It provides real-time information about the status of Celery workers and tasks. You can read more about it [here](https://flower.readthedocs.io/en/latest/)

Once the containers are up and running, to access the Flower dashboard, you need to open a browser and go to the following URL:

```
http://localhost:5555
```
