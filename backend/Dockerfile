# Image Python officielle
FROM python:3.12-slim

# Empêcher la création de fichiers .pyc
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Dossier de travail
WORKDIR /app

# Installer dépendances système
RUN apt-get update && apt-get install -y gcc libpq-dev && rm -rf /var/lib/apt/lists/*

# Copier requirements
COPY requirements.txt .

# Installer dépendances Python
RUN pip install --upgrade pip && pip install -r requirements.txt

# Copier le code
COPY app ./app

# Exposer le port FastAPI
EXPOSE 8000

# Lancer l’API
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
