FROM nginx:1.23-alpine

RUN rm /etc/nginx/nginx.conf /etc/nginx/conf.d/default.conf
# COPY content /usr/share/nginx/html
# COPY nginx.conf /etc/nginx/site-enabled/default
COPY nginx.conf /etc/nginx/conf.d
# VOLUME /usr/share/nginx/html
# VOLUME /etc/nginx

# RUN rm /etc/nginx/conf.d/default.conf
