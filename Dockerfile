# Imagen base segura y actual
FROM python:3.12-slim

# Directorio de trabajo
WORKDIR /app

# Copiar dependencias
COPY requirements.txt .

# Instalar dependencias
RUN pip install --no-cache-dir --upgrade pip setuptools wheel \
    && pip install --no-cache-dir -r requirements.txt

# Copiar código fuente
COPY app.py .

# Exponer puerto
EXPOSE 5000

# Comando de inicio
CMD ["python", "app.py"]






