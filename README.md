# docker-instructions


## Basic
### build image
```docker build -t imagename .```

### run image detached
```docker run -d imagename```

## Running a server
```docker run -d -p 5000:5000 myimage```


## deleting a container
```docker ps -a```
```docker rm -f <id>```

## deleting an image
To delete an image you need to first delete connected containers running
```docker images```
```docker rmi <id>```
