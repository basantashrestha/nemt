# Stage 1: Build
FROM node:12-alpine as builder
WORKDIR /app
COPY package*.json ./
COPY . /app 
RUN npm install
RUN npm install pg
RUN npm run build

# Stage 2: Serve
FROM nginx:alpine
COPY --from=builder /app/build /usr/share/nginx/html
EXPOSE 80
CMD ["nginx", "-g", "daemon off;"]
