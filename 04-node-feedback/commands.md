# Commands to run in terminal

Build image
docker build -t <image-name:tag> .

Create and run new container
docker run -d -p 3000:80 --rm --name <container-name> <image-name:tag>

Create and run new container with volume
docker run -d -p 3000:80 --rm --name <container-name> -v <volume-name>:/<folder-name> <image-name:tag>

Create and run new container with volume and build mount directory
docker run -d -p 3000:80 --rm --name <container-name> -v <volume-name>:/<folder-name> -v "<root-folder-name>:/<folder-name>" <image-name:tag>

Also adding an anonymous volume
docker run -d -p 3000:80 --rm --name <container-name> -v <volume-name>:/<folder-name> -v "<root-folder-name>:/<folder-name>" -v /<folder-name> <image-name:tag>

Check logs
docker logs <container-name>
