FROM python:3.8-slim

WORKDIR /app

COPY requirements.txt /app
COPY test.py /app

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 6210

CMD ["python3", "test.py"]
