# Introduction to Docker

> Warning! This article is from 2016 and some items might not be relevant anymore!

![alt](/media/docker_pirates.jpg)

## What is Docker ?

* OS level virtualization on Linux
* Resources isolation using Linux kernel features
* Single OS, multiple containter instances
* Application view on OS is isolated
* Provides the same environment on all platforms.

![alt](/projects/docker1.svg)

### Union filesystem

aufs (advanced multi layered unification filesystem)

![alt](/projects/docker2.svg)

## Docker Family
### Docker Inc
Commercial company behind Docker.

### Docker Engine
Docker Engine runs on Linux to create the operating environment for your distributed applications.

#### Docker Daemon
Persistent Linux service that manages containers in the system.
#### Docker Client
Utilises Docker API to talk with the daemon.

### Docker Machine
Automate Docker provisioning. Sets up docker or different systems (cloud, mac, windows)

### Docker Registry
Docker Registry is an open source application dedicated to the storage and distribution of your Docker images.

### Docker Compose
Docker Compose allows you to define your multi-container application with all of its dependencies in a single file, then spin your application up in a single command.

### Docker Swarm
Docker Swarm provides native clustering capabilities to turn a group of Docker engines into a single, virtual Docker Engine.

### Kitematic
Build and run containers through a simple, yet powerful graphical user interface (GUI).

### Docker Datacenter
Docker Datacenter brings container management and deployment services to enterprises with a production-ready platform supported by Docker and hosted locally behind the firewall

### Docker Cloud
A hosted service for Docker container management and deployment.

### Docker Hub
Docker Hub is a cloud hosted service from Docker that provides registry capabilities for public and private content.

### Docker Toolbox
Installer for Docker tools on Windows and Mac.

### boot2docker
Minimalistic Linux distribution used to run Docker on Windows and Mac.

## Concepts

### Image

### Container
Instance of the image.
> The concept is borrowed from Shipping Containers, which define a standard to ship goods globally. Docker defines a standard to ship software.

## Installation
* Ensure if the CPU virtualization is enabled in BIOS.
* Install Docker toolbox (https://www.docker.com/products/docker-toolbox)
* Do not install Virtual Box if it is already installed.
* Setup environment variables accordingly to *docker-machine env*
## Usage
* docker-machine
* run
* -d
* --name
* -p
* -v
* entrypoint
* ps
* images
* build (Dockerfile) (python http server)
* attach
* exec
* commit
* login
* export/save

```
docker run hello-world

docker run -d hello-world

docker run -d --name HELLO hello-world

docker ps

docker ps -a

docker run -d -p 8000:80 --name dokuwiki istepanov/dokuwiki:2.0

docker images*

docker build -t maciejkucia/myapplication .
```

## What next?

See "Dockerize an application" examples (https://docs.docker.com/engine/examples/)

Learn about:

* Volumes (https://docs.docker.com/engine/userguide/containers/dockervolumes/)
* Networking (https://docs.docker.com/engine/userguide/networking/dockernetworks/)
* Logging, Orchestration (Docker Compose) ...

Explore Docker Hub (https://hub.docker.com/)

## References

* <https://docs.docker.com/engine/reference/glossary/>
* <http://developerblog.redhat.com/2016/01/13/a-practical-introduction-to-docker-container-terminology/>
* <https://en.wikipedia.org/wiki/Docker_(software)>
* <https://en.wikipedia.org/wiki/Aufs>
* <https://docs.docker.com/engine/understanding-docker/>
* <https://www.ibm.com/support/knowledgecenter/SS3MQL_1.1.0/manage_services/docker_concepts.dita>
