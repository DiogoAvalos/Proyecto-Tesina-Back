# # Usa una imagen base de Python para FastAPI
# FROM python:3.10

# # Establece el directorio de trabajo
# WORKDIR /app

# # Copia los archivos del proyecto
# COPY . .

# # Instala las dependencias
# RUN pip install --no-cache-dir -r requirements.txt

# # Expone el puerto 8000
# EXPOSE 8000

# # Comando para ejecutar FastAPI (ajusta si usas otro framework)
# CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]

#TODO: PRUEBAS
# Usa una imagen de Docker con Compose para orquestar servicios
FROM docker:latest  

# Instala Docker Compose dentro del contenedor
RUN apk add --no-cache docker-compose  

# Establece el directorio de trabajo
WORKDIR /app  

# Copia todos los archivos del proyecto
COPY . .  

# Expone los puertos necesarios para la API y PostgreSQL
EXPOSE 80 8000 8001 8002 5432  

# Comando para levantar todos los servicios con docker-compose
CMD ["docker-compose", "up"]
