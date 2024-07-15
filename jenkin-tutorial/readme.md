
# Tutorial
Following the tutorial [here](https://www.jenkins.io/doc/tutorials/create-a-pipeline-in-blue-ocean/) giving the requirements to run the project
# Table of Contents
  - [Requirements](#requirements)
  - [Guilder](#guilder)


## Requirements
Need 2 container which help run container in side the jenkins application
  - [container run docker server](#subsetting-for-execure-docker-command-in-jenkin)
  - [container run jenkin with blueocean extension](#run-jenkin-with-attribute)

## Guilder

### Network
- check available network for jenkin or create new with this 
```docker network create jenkins```

### Subsetting for execure docker command in jenkin
- Using docker:dind image
```
docker run --name jenkins-docker --rm --detach \
  --privileged --network jenkins --network-alias docker \
  --env DOCKER_TLS_CERTDIR=/certs \
  --volume jenkins-docker-certs:/certs/client \
  --volume jenkins-data:/var/jenkins_home \
  --publish 3000:3000 --publish 5000:5000 --publish 2376:2376 \
  docker:dind --storage-driver overlay2
```

### Build and Run jenkin with attribute
```
docker build -t myjenkins-blueocean:2.452.3-1 .
```

With semi-real implementation, cuz try to restart when fail
```
docker run --name jenkins-blueocean --detach \
  --network jenkins --env DOCKER_HOST=tcp://docker:2376 \
  --env DOCKER_CERT_PATH=/certs/client --env DOCKER_TLS_VERIFY=1 \
  --publish 8080:8080 --publish 50000:50000 \
  --volume jenkins-data:/var/jenkins_home \
  --volume jenkins-docker-certs:/certs/client:ro \
  --volume "$HOME":/home \
  --restart=on-failure \
  --env JAVA_OPTS="-Dhudson.plugins.git.GitSCM.ALLOW_LOCAL_CHECKOUT=true" \
  myjenkins-blueocean:2.452.3-1
```
or just for testing with rm container after stop
```
docker run --name jenkins-blueocean --rm --detach \
  --network jenkins --env DOCKER_HOST=tcp://docker:2376 \
  --env DOCKER_CERT_PATH=/certs/client --env DOCKER_TLS_VERIFY=1 \
  --publish 8080:8080 --publish 50000:50000 \
  --volume jenkins-data:/var/jenkins_home \
  --volume jenkins-docker-certs:/certs/client:ro \
  --volume "$HOME":/home \
  --env JAVA_OPTS="-Dhudson.plugins.git.GitSCM.ALLOW_LOCAL_CHECKOUT=true" \
  myjenkins-blueocean:2.452.3-1
```
### Get begin key for setting jenkins
```
docker logs jenkins-blueocean
```
