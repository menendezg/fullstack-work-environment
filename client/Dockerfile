# Tell Docker we want to use Node v8.7.0 installed in a alpine Linux image.
# The alpine image is an extremely optimized minimal Docker image based 
# on the Alpine Linux. 
# Its own size is as small as 5 MB, adding Node on top of it will make it around 50 MB,
# still very slim (quasi 1/10 of the “-slim” Linux image whose size is about 650 MB,
FROM node:8.7.0-alpine

# Create app directory and use it as the working directory.
# The -p flag enable to create the directory recursively whithout having to go into 
# each level
RUN mkdir -p /srv/app/foo-client
WORKDIR /srv/app/foo-client

COPY package.json /srv/app/foo-client
COPY package-lock.json /srv/app/foo-client

run npm install

copy . /srv/app/foo-client
CMD [ "npm", "start" ]
