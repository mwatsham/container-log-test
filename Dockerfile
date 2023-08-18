FROM python:3.6-alpine
 
MAINTAINER Mark Watsham "mark.watsham@sky.uk"
 
WORKDIR /
 
COPY . /
 
ENTRYPOINT [ "python3" ]
 
CMD [ "app/logging.py" ]
