ARG NODE_VERSION
FROM node:${NODE_VERSION}
WORKDIR /home/node
USER node
COPY --chown=node:node ./package* ./
RUN npm install
COPY --chown=node:node ./ ./
ENV NODE_ENV=development
CMD [ "node", "server.js" ]