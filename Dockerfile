# HTTP Web Sunucusu Dockerfile
# Mertcan Gelbal - 171421012

FROM python:3.11-slim

LABEL maintainer="Mertcan Gelbal <mertcan@example.com>"
LABEL description="Sıfırdan geliştirilmiş HTTP Web Sunucusu"
LABEL version="1.0"

WORKDIR /app

RUN apt-get update && apt-get install -y \
    --no-install-recommends \
    && rm -rf /var/lib/apt/lists/*

COPY server.py .
COPY static/ ./static/

RUN mkdir -p static logs

EXPOSE 8080

CMD ["python", "server.py"]

HEALTHCHECK --interval=30s --timeout=3s --start-period=5s --retries=3 \
    CMD python -c "import socket; s=socket.socket(); s.connect(('localhost', 8080)); s.close()" || exit 1 