# Official Python base image
FROM python:3.13-slim

# Create a working directory in the container
WORKDIR /app

# Copy the dependencies file
COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir --root-user-action=ignore --disable-pip-version-check -r requirements.txt

# Create a non-root user with ID 1000
RUN useradd -m -u 1000 appuser && \
    chown -R appuser:appuser /app

# Switch to non-root user
USER appuser

# Copy the rest of the application
COPY --chown=appuser:appuser . .