FROM python:3.6.9
WORKDIR /usr/src/app
COPY . .
EXPOSE 80
RUN pip install psycopg2
CMD ["python", "http_server.py"]

# COPY docker_gosu.sh .
# RUN chmod +x docker_gosu.sh
# ENTRYPOINT [ "docker_gosu.sh" ]
# CMD ["/bin/bash", "-c", "docker_gosu.sh"]
# RUN groupadd -r nonroot && useradd -r -g nonroot nonroot 
# USER nonroot

