FROM ubuntu

# File Author / Maintainer
MAINTAINER andrewyang96@gmail.com

# Install pip
RUN apt-get update -y
RUN apt-get install -y python-pip

# Add and install Python modules
ADD requirements.txt /src/requirements.txt
RUN cd /src; pip install -r requirements.txt

# Bundle app source
ADD . /src
WORKDIR /src

# Expose port
EXPOSE 5001

# Run
CMD ["gunicorn", "--bind", "0.0.0.0:5001", "app:app"]
