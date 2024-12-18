# Dockerfile
FROM python:3.9-slim

WORKDIR /app

# Copia os requisitos e o script
COPY requirements.txt requirements.txt
RUN pip install --no-cache-dir -r requirements.txt
COPY script.py script.py

CMD ["python", "script.py"]
