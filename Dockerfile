FROM python:3.12-slim
WORKDIR /app
COPY app.py .
ENV PORT=8080
EXPOSE 8080
USER nobody
CMD ["python", "app.py"]
LABEL org.opencontainers.image.source=https://github.com/emmanuelbanjo/shipit-app
