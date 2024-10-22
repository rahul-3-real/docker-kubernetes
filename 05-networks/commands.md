# Commands to run in terminal

Installing Mongo Image and Running Container
docker run -d --name <container-name> mongo

Build image
docker build -t <image-name:tag> .

Create and run new container
docker run -d -p 3000:3000 --rm --name <container-name> <image-name:tag>

Adding network
docker network <network-name>
