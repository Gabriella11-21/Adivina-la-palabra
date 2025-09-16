# Usar una imagen oficial de Python
FROM python:3.10-slim

# Carpeta de trabajo dentro del contenedor
WORKDIR /app

# Copiar tu código al contenedor
COPY Adivina-palabra.py .

# Comando para ejecutar el programa
CMD ["python", "Adivina-palabra.py"]
