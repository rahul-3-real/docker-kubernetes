# Commands to Dockerize MERN App

## Frontend

## Backend

Build Image
docker build -t <image-name:tag> .

Run Container
docker run -d -p 80:80 --rm --name <container-name> <image-name>

## MongoDB

Run MongoDB Container
docker run -p <port>:<port> -d --rm --name <container-name> <image-name>
