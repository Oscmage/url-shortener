# TODO: Move to alpine version
FROM python:3.8.12

WORKDIR /code

COPY ./requirements.txt /code/requirements.txt

RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt

COPY ./app /code/app

# TODO: Update to use gunicorn for production
CMD ["uvicorn", "app.main:start", "--host", "0.0.0.0", "--port", "8080"]