# Imagen base oficial de Python
FROM python:3.13-slim

# Crea un directorio de trabajo en el contenedor
WORKDIR /app

# Copia el archivo de dependencias
COPY requirements.txt .

# Instala las dependencias
RUN pip install --no-cache-dir --root-user-action=ignore --disable-pip-version-check -r requirements.txt

# Crea un usuario no-root con ID 1000
RUN useradd -m -u 1000 appuser && \
    chown -R appuser:appuser /app

# Cambia al usuario no-root
USER appuser

# Copia el resto de la aplicación
COPY --chown=appuser:appuser . .