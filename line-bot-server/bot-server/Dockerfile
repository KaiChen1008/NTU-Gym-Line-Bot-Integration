FROM python:3.8.8-alpine3.13

WORKDIR /myapp/

COPY bot-server/requirements.txt ./

RUN pip install --no-cache-dir --upgrade pip && \
	pip install --no-cache-dir -r requirements.txt

COPY ./bot-server/ /myapp

CMD ["python", "manage.py", "runserver", "0.0.0.0:8010"]
