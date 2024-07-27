FROM node:12-alpine

WORKDIR /app

COPY package.json ./
COPY . /app
RUN npm install
RUN npm install pg
RUN npm run build

#EXPOSE 3000

