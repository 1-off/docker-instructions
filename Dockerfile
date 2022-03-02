# set base image (host OS)
FROM python:latest

# set the working directory in the container
WORKDIR /

COPY . .

# install dependencies
RUN pip install -r requirements.txt

# command to run on container start
CMD [ "python3", "main.py"] 