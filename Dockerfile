FROM python:3.11-slim

RUN apt-get update && \
    apt-get install -y python3-tk && \
    rm -rf /var/lib/apt/lists/*

WORKDIR /app

COPY py_files/ .

CMD ["python3", "main.py"]
