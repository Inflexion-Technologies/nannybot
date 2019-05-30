FROM jfloff/alpine-python:3.7

RUN apk add libressl-dev
RUN pip install errbot[slack]
RUN adduser -Dh /var/lib/err err

WORKDIR /var/lib/err
USER err
RUN errbot --init; rm -rf plugins/err-example; 
COPY config.py .
COPY icii plugins/icii
RUN echo | errbot
RUN echo "{'configs': {'Webserver': {'HOST': '0.0.0.0', 'PORT': 3124}}}" | errbot --storage-merge core
EXPOSE 3124

ENTRYPOINT ["errbot"]
