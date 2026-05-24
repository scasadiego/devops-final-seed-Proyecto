FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY src/ ./src/

ENV DB_PATH=/data/tasks.db
ENV PORT=5000

EXPOSE 5000

CMD ["python", "src/app.py"]
