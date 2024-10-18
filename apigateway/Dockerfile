FROM nginx:1.25.3-alpine
RUN rm /etc/nginx/conf.d/default.conf
# COPY . /etc/nginx/conf.d/ #TODO: Pruebas en local
COPY apigateway/default.conf /etc/nginx/conf.d/
EXPOSE 80