# set the base image 
FROM python:3.8.10

# File Author / Maintainer
MAINTAINER Overlord

#add project files to the usr/src/app folder
ADD . /home/dev2/Documents/Projects/InvcoiceApp/saasinvoiceapp

#set directoty where CMD will execute 
WORKDIR /home/dev2/Documents/Projects/InvcoiceApp/saasinvoiceapp

COPY requirements.txt ./

# Get pip to download and install requirements:
RUN pip install --no-cache-dir -r requirements.txt; 

 