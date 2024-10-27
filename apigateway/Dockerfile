FROM nginx:1.25.3-alpine
RUN rm /etc/nginx/conf.d/default.conf
#TODO: Pruebas en local
COPY . /etc/nginx/conf.d/
#TODO: Produccion
# COPY apigateway/default.conf /etc/nginx/conf.d/
EXPOSE 80