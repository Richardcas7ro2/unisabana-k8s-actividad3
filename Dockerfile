# Usar la imagen oficial y ligera de Python 3.11
FROM python:3.11-slim

# Metadatos del mantenedor
LABEL maintainer="Ricardo Castro <ricardo@example.com>"
LABEL description="Microservicio base para práctica K8S con FastAPI"

# Establecer directorio de trabajo dentro del contenedor
WORKDIR /code

# Evitar que Python genere archivos de bytecode (.pyc) y forzar logs directos (sin buffer)
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Copiar el archivo de reqs para instalar dependencias primero (cache de capas de Docker)
COPY requirements.txt /code/

# Instalar dependencias sin usar caché para alivianar la imagen final
RUN pip install --no-cache-dir --upgrade pip \
    && pip install --no-cache-dir -r requirements.txt

# Copiar el código real de la aplicación (incluyendo la carpeta templates)
COPY ./app /code/app

# Crear un usuario no-root por seguridad (buena práctica en contenedores y K8S)
RUN useradd -m myapiuser
USER myapiuser

# Exponer el puerto donde FastAPI escuchará tráfico
EXPOSE 8000

# Comando para levantar la aplicación usando Uvicorn, escuchando en todas las interfaces de red del contenedor
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000", "--proxy-headers"]

