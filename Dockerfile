FROM python:3.9.6
WORKDIR /Assignment5

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

COPY requirements.txt /Assignment5/
RUN pip3 install -r requirements.txt
#RUN apt-get update; apt-get install -y postgresql-client
#COPY wait-for-postgres.sh /wait-for-postgres.sh
COPY . /Assignment5/
#RUN chmod +x /wait-for-postgres.sh
#RUN export PATH=/Library/PostgreSQL/13/bin/psql:$PATH
#ENTRYPOINT ["bash","/wait-for-postgres.sh"]
#HEALTHCHECK --interval=2s --timeout=2s --start-period=3s \  
#    CMD curl --fail http://localhost:5432 || exit 1