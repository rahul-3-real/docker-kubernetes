# Docker Cheatsheet

## Basic Commands

| Command            | Description                       |
| ------------------ | --------------------------------- |
| `docker --version` | Show the Docker version installed |
| `docker info`      | Display system-wide information   |
| `docker --help`    | Get help on any Docker command    |

## Container Lifecycle

| Command                                    | Description                             |
| ------------------------------------------ | --------------------------------------- |
| `docker ps`                                | List running containers                 |
| `docker ps -a`                             | List all containers (including stopped) |
| `docker start <container_id>`              | Start a container                       |
| `docker stop <container_id>`               | Stop a running container                |
| `docker restart <container_id>`            | Restart a container                     |
| `docker kill <container_id>`               | Kill a container                        |
| `docker rm <container_id>`                 | Remove a stopped container              |
| `docker logs <container_id>`               | Fetch logs of a container               |
| `docker exec -it <container_id> <command>` | Run a command in a running container    |

## Images

| Command                             | Description                      |
| ----------------------------------- | -------------------------------- |
| `docker images`                     | List all Docker images           |
| `docker pull <image_name>`          | Pull an image from a registry    |
| `docker rmi <image_name>`           | Remove an image                  |
| `docker build -t <image_name> .`    | Build an image from a Dockerfile |
| `docker tag <image_name> <new_tag>` | Tag an image with a new tag      |

## Networks

| Command                                           | Description                           |
| ------------------------------------------------- | ------------------------------------- |
| `docker network ls`                               | List all networks                     |
| `docker network create <name>`                    | Create a new network                  |
| `docker network rm <name>`                        | Remove a network                      |
| `docker network inspect <name>`                   | Inspect a network                     |
| `docker network connect <network> <container>`    | Connect a container to a network      |
| `docker network disconnect <network> <container>` | Disconnect a container from a network |

## Volumes

| Command                        | Description         |
| ------------------------------ | ------------------- |
| `docker volume ls`             | List volumes        |
| `docker volume create <name>`  | Create a new volume |
| `docker volume rm <name>`      | Remove a volume     |
| `docker volume inspect <name>` | Inspect a volume    |

## Docker Compose

| Command                | Description                                               |
| ---------------------- | --------------------------------------------------------- |
| `docker-compose up`    | Start all services defined in `docker-compose.yml`        |
| `docker-compose down`  | Stop and remove containers, networks, etc.                |
| `docker-compose ps`    | List containers managed by Docker Compose                 |
| `docker-compose build` | Build images for services defined in `docker-compose.yml` |
| `docker-compose logs`  | View logs for all services                                |

## Useful Dockerfile Instructions

| Instruction                        | Description                                                   |
| ---------------------------------- | ------------------------------------------------------------- |
| `FROM <image>`                     | Set the base image for the Dockerfile                         |
| `COPY <source> <destination>`      | Copy files from host to container                             |
| `RUN <command>`                    | Run a command in the container                                |
| `CMD ["command", "param1"]`        | Specify a default command to run in the container             |
| `ENTRYPOINT ["command", "param1"]` | Define the command that always runs when the container starts |
| `EXPOSE <port>`                    | Expose a port                                                 |

## Miscellaneous

| Command                                    | Description                                             |
| ------------------------------------------ | ------------------------------------------------------- |
| `docker system prune`                      | Remove unused containers, networks, images, and volumes |
| `docker inspect <container_id>`            | Get detailed information about a container              |
| `docker stats`                             | Display a live stream of container(s) resource usage    |
| `docker top <container_id>`                | Display running processes in a container                |
| `docker commit <container_id> <new_image>` | Create a new image from a container's changes           |
