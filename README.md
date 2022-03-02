# docker-instructions


## Basic
### build image
```docker build -t imagename .```

### run image detached
```docker run -d imagename```

## Running a server
```docker run -d -p 5000:5000 myimage```


## deleting a container
First this will list all your containers
```docker ps -a```
Then...
```docker rm -f <id>```

## deleting an image
To delete an image you need to first delete connected containers running
```docker images```
The -f flag force the container deletion
```docker rmi -f <id>```
