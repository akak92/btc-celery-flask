FROM python:3.12

# Establecemos zona horaria
ENV TZ=America/Argentina/Buenos_Aires
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone

# Instalar cron
RUN apt-get update && apt-get install -y cron

# Establecer el directorio de trabajo en el contenedor
WORKDIR /app

# Copiamos requirements.txt en el contenedor
COPY requirements.txt .

# Instalar el resto de las bibliotecas y paquetes usando pip
RUN pip install --no-cache-dir -r requirements.txt

# Copiar el contenido del directorio actual en el contenedor
COPY . .

# Añadir el cron job
RUN echo "*/2 * * * * /usr/local/bin/python /app/main.py >> /var/log/cron.log 2>&1" > /etc/cron.d/mycron

# Dar permisos correctos al cron job
RUN chmod 0644 /etc/cron.d/mycron

# Aplicar el cron job
RUN crontab /etc/cron.d/mycron

# Crear el fichero de logs de cron
RUN touch /var/log/cron.log

# Copiar el script de entrada
COPY entrypoint.sh /entrypoint.sh

# Dar permisos de ejecución al script de entrada
RUN chmod +x /entrypoint.sh

# Establecer el script de entrada como el punto de entrada del contenedor
ENTRYPOINT ["/entrypoint.sh"]