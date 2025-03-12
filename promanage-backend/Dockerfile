FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

# Migrations
RUN alembic init migrations
RUN alembic revision --autogenerate -m "Initial migration"
RUN alembic upgrade head

CMD [ "sh", "-c", "alembic upgrade head && uvicorn app.main:app --host 0.0.0.0 --port 8000 --reload" ]