FROM python:3.11-slim

RUN pip install --no-cache-dir numpy

WORKDIR /app

COPY matrix.py /app/

CMD ["python", "matrix.py"]
