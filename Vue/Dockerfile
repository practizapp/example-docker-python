ARG NODE_VERSION
FROM node:${NODE_VERSION} as builder
COPY . /usr/src/app
WORKDIR /usr/src/app
RUN set -ex; \
    npm install @vue/cli-service; \
    npm install; \
    npm run build

FROM nginx:alpine
COPY --from=builder /usr/src/app/dist /build
RUN mkdir -p /logs
RUN echo 'server {\
    listen 80;\
    access_log /logs/access.log;\
    location / {\
        root /build;\
        try_files $uri $uri/ =404;\
        index index.html;\
    }\
}' > /etc/nginx/conf.d/default.conf
EXPOSE 80