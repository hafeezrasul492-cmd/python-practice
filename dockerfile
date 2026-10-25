FROM python:3.12-slim
RUN apt-get update && apt-get install -y iputils-ping && rm -rf /var/lib/apt/lists/*
WORKDIR /app
COPY ping_checker.py .
CMD ["python", "ping_checker.py"]

