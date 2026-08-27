FROM python:3.12-slim
WORKDIR /app

RUN apt-get update && apt-get upgrade -y && apt-get install -y --no-install-recommends \
    libssl3 \
    && rm -rf /var/lib/apt/lists/*

COPY requirements.txt .
RUN pip install --upgrade pip setuptools wheel msgpack \
    && pip install -r requirements.txt

COPY app.py .
CMD ["python", "app.py"]



