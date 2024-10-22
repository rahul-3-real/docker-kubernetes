FROM node:20.16.0

WORKDIR /app

COPY package.json /app

RUN npm install

COPY . /app

ARG DEFAULT_PORT=80

ENV PORT $DEFAULT_PORT

EXPOSE $PORT

# VOLUME [ "/app/node_modules" ]

VOLUME [ "/app/temp" ]

CMD ["npm", "run", "dev"]