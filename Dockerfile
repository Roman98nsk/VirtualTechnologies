FROM python:3.6.9
WORKDIR /usr/src/app/
COPY server.py .
EXPOSE 80
CMD ["python3", "server.py"]