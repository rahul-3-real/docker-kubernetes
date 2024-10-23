# Commands to Dockerize MERN App

## Frontend

Build Image
docker build -t <image-name:tag> .

Run Container
docker run -d -p 3000:3000 --rm --name <container-name> <image-name>

Network does not needed as frontend talks to browser

## Backend

Build Image
docker build -t <image-name:tag> .

Run Container
docker run -d -p 80:80 --rm --name <container-name> <image-name>

Run Container using Network
docker run -d -p 80:80 --network <network-name> --rm --name <container-name> <image-name>

## MongoDB

Run MongoDB Container
docker run -p <port>:<port> -d --rm --name <container-name> <image-name>

Run MongoDB Container using Network
docker run -d --network <network-name> --rm --name <container-name> <image-name>
