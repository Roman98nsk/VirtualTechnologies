FROM python:3.6.9
WORKDIR /home/roman/Рабочий стол/4 курс/8 семестр/ТехВирт/Приложение/lab2
COPY server.py .
CMD ["python3", "server.py"]