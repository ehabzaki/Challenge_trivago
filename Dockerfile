FROM python:3

COPY . /app
WORKDIR /app

RUN pip install -r requirements.txt
 
#VOLUME . /app
CMD [ "python", "./main.py" ]
