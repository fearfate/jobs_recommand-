ARG PYTHON_VERSION=3.8
FROM python:${PYTHON_VERSION}
LABEL maintainer="Aproc, aprothtristan@foxmail.com"

ENV PATH="/opt/miniconda3/bin:${PATH}"
ENV PYSPARK_PYTHON="/opt/miniconda3/bin/python"

#COPY bde-spark.css /css/org/apache/spark/ui/static/timeline-view.css
RUN apt-get update && \
    sh -c '/bin/echo -e "Y\n" |apt-get install python3-pip python-dev build-essential' &&\
    pip install django &&\
    pip install --no-cache nameko && \
    apt-get autoremove -y && \
    apt-get clean && \
    mkdir /WebServer

# Fix the value of PYTHONHASHSEED
# Note: this is needed when you use Python 3.3 or greater
EXPOSE 8000
WORKDIR /WebServer
ENV PYTHONHASHSEED 1
CMD ["python","manage.py","runserver", "0.0.0.0:8000"]