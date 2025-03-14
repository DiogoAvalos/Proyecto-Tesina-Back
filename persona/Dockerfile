FROM python:3.10.5-slim
WORKDIR /code
COPY ./requirements.txt /code/requirements.txt
RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt
COPY ./ /code/app
CMD ["uvicorn", "app.main:app", "--port", "80", "--host", "0.0.0.0"]
