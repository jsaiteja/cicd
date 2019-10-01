FROM python:3.5.7-alpine3.9 
RUN mkdir -p /app
COPY . /app
WORKDIR /app
RUN pip3 install -r requirements.txt
EXPOSE 8086
ENTRYPOINT ["python"]
CMD ["flask_api/api.py"]
