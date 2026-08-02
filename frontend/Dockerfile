FROM python:3.10-slim

WORKDIR /app

COPY . .

ENV PYTHONUNBUFFERED=1
EXPOSE 3000

CMD sh -c "python -m http.server ${PORT:-3000} --bind 0.0.0.0"
