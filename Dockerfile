FROM python:3.11-slim   
WORKDIR /app

COPY requirements.txt .
RUN pip install --upgrade pip setuptools==78.1.1 wheel msgpack==1.2.1 \
    && pip install -r requirements.txt

COPY app.py .
CMD ["python", "app.py"]


