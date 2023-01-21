FROM python:3.9-slim-buster

WORKDIR /app

COPY . /app

RUN pip --no-cache-dir install -r requirements.txt

EXPOSE 5000

ENTRYPOINT ["python3"]

CMD ["main.py"]


