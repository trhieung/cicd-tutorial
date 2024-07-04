<!-- # 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 -->
# Tutorial

following the tutorial [here](https://www.jenkins.io/doc/tutorials/create-a-pipeline-in-blue-ocean/)

## network
- check available network for jenkin or create new with this ```docker network create jenkins```

## subsetting for execure docker command in jenkin
- using docker:dind image
```
docker run --name jenkins-docker --rm --detach \
  --privileged --network jenkins --network-alias docker \
  --env DOCKER_TLS_CERTDIR=/certs \
  --volume jenkins-docker-certs:/certs/client \
  --volume jenkins-data:/var/jenkins_home \
  --publish 3000:3000 --publish 5000:5000 --publish 2376:2376 \
  docker:dind --storage-driver overlay2
```

## run jenkin with attribute
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
  myjenkins-blueocean:2.452.2-1
```
## access docker log blueocean to get the key
- ```docker logs myjenkins-blueocean:2.452.2-1```
