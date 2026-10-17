FROM python:3.9-slim
WORKDIR /app
COPY . .
RUN pip install matplotlib
CMD ["python", "relogio.py"]
