# Usa una imagen base de Python
FROM python:3.11

# Establece el directorio de trabajo en el contenedor
WORKDIR /app

# Copia el archivo de requisitos y los instala
COPY requirements.txt .
RUN pip install -r requirements.txt

# Copia el resto de la aplicación en el contenedor
COPY . .

# Configura las variables de entorno para Django
ENV DJANGO_SETTINGS_MODULE=estaciones.settings
ENV PYTHONUNBUFFERED=1

# Expone el puerto de Django
EXPOSE 8000

# Ejecuta el servidor de Django
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
