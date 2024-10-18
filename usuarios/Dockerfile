# FROM python:3.10.5-slim #TODO: Desarrollo
# WORKDIR /code #TODO: Desarrollo
# COPY ./requirements.txt /code/requirements.txt #TODO: Desarrollo
# RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt #TODO: Desarrollo
# COPY ./ /code/app #TODO: Desarrollo
# CMD ["uvicorn", "app.main:app", "--port", "80", "--host", "0.0.0.0"] #TODO: Desarrollo

FROM python:3.10.5-slim
WORKDIR /code
COPY ./requirements.txt /code/requirements.txt
RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt
COPY ./ /code/app
EXPOSE 80
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "80"]
