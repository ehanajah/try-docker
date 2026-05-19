FROM python:3.12-slim

# Prevent Python from generating pyc files
ENV PYTHONDONTWRITEBYTECODE=1

# Show logs immediately
ENV PYTHONUNBUFFERED=1

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 5000

CMD ["hypercorn", "run:app", "--bind", "0.0.0.0:5000"]