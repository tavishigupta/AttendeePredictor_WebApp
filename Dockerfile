FROM ubuntu

# sets the Author field of the image (useful when pushing to Docker Hub)
MAINTAINER Your Name "tgupta24@wisc.edu"

# && \ isn�t Docker specific, but tells Linux to run the next command as part of the existing line (instead of using multiple RUN directives, you can use just one)
RUN apt-get update -y && \
    apt-get install -y python-pip python-dev

# We copy just the requirements.txt first to leverage Docker cache
COPY ./requirements.txt /app/requirements.txt

# sets the working directory (all following instructions operate within this directory)
WORKDIR /app

RUN pip install -r requirements.txt

COPY . /app

# unblock port 80 for the Flask app to run on
EXPOSE 80

# configures the container to run as an executable; only the last ENTRYPOINT instruction executes
ENTRYPOINT [ "python" ]

CMD [ "runserver.py" ]