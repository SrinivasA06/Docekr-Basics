# start by pulling the python image
FROM tiangolo/nginx-rtmp:latest

# copy the requirements file into the image
COPY ./requirements.txt /app/requirements.txt

# switch working directory
WORKDIR /app

# install the dependencies and packages in the requirements file


RUN apt update
RUN apt install python3 -y
RUN apt install python3-pip -y
RUN pip3 install Flask
RUN pip3 install -r requirements.txt
RUN pip3 install opencv-contrib-python


# copy every content from the local file to the image
COPY . /app

# configure the container to run in an executed manner
ENTRYPOINT [ "python" ]

CMD ["view.py" ]