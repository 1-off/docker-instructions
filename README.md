# docker-instructions
-- forserveruse 
--- Dockerfile
--- basic_python_server.py
-- singlescript
--- Dockerfile

## Basic
### build image
```docker build -t imagename .```

### run image detached
```docker run -d imagename```

## Running a server
```docker run -d -p 5000:5000 myimage```
