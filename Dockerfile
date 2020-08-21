# set base image (host OS)
FROM python:3

# set the working directory in the container
WORKDIR /code

# copy the content of the local src directory to the working directory
ADD *.py .
EXPOSE 8080
# command to run on container start
CMD [ "python", "./pywai.py" , "8080"]