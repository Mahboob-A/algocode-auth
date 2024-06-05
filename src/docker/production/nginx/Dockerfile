
# nginx is not used in production. nginx proxy manager is used. 
# To test production in locally, use the Nginx config from dev.yml
FROM nginx:1.24.0-alpine

RUN rm /etc/nginx/conf.d/default.conf

COPY ./docker/production/nginx/default.conf /etc/nginx/conf.d/default.conf
