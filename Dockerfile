FROM python:3.12-slim
WORKDIR /app

RUN apt-get update && apt-get upgrade -y && apt-get install -y --no-install-recommends \
    libssl3 \
    && rm -rf /var/lib/apt/lists/*

COPY requirements.txt .
RUN pip install --upgrade pip \
    && pip install -r requirements.txt \
    && pip uninstall -y setuptools wheel \
    && pip install setuptools==78.1.1 wheel==0.46.2 \
    && rm -rf ~/.cache/pip

COPY app.py .
EXPOSE 5055
CMD ["python3", "app.py"]






