# Usa una imagen base de Python para FastAPI
FROM python:3.10

# Establece el directorio de trabajo
WORKDIR /app

# Copia los archivos del proyecto
COPY . .

# Instala las dependencias
RUN pip install --no-cache-dir -r requirements.txt

# Expone el puerto 8000
EXPOSE 8000

# Comando para ejecutar FastAPI (ajusta si usas otro framework)
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
