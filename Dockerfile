FROM python:3.6.9
WORKDIR /usr/src/app/
COPY server.py .
EXPOSE 80
CMD ["python3", "server.py"]
RUN groupadd -r nonroot && useradd -r -g nonroot nonroot
USER nonroot

#COPY docker_gosu.sh .
#RUN chmod +x docker_gosu.sh
#ENTRYPOINT ["docker_gosu.sh"]
#CMD ["/bin/bash", "-c", "docker_gosu.sh"]