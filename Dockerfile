FROM python:3.11-slim

WORKDIR /app
COPY . /app

RUN pip install --no-cache-dir textual

CMD ["textual", "run", "your_app.py", "--web", "--host", "0.0.0.0", "--port", "8080"]
