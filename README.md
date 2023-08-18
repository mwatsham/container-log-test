# container-log-test
Container producing output to STDOUT/STDERR to test external logging such as forwarding these log streams central logging tool like Splunk.

Logging to STDOUT/STDERR instead of a local file for an app in a container is inline with standard container logging features and best practice. The intention then is to forward these log streams central logging tool like Splunk.

This container image can be used as a simple test logging container to drive integration testing.

## Example output
```
...
04-Jun-2021 (09:34:54.411185) - This is STDOUT from 8fd93320bf59
04-Jun-2021 (09:34:54.411185) - This is STDERR from 8fd93320bf59
04-Jun-2021 (09:34:55.417241) - This is STDOUT from 8fd93320bf59
04-Jun-2021 (09:34:55.417241) - This is STDERR from 8fd93320bf59
04-Jun-2021 (09:34:56.418825) - This is STDOUT from 8fd93320bf59
04-Jun-2021 (09:34:56.418825) - This is STDERR from 8fd93320bf59
04-Jun-2021 (09:34:57.421353) - This is STDOUT from 8fd93320bf59
04-Jun-2021 (09:34:57.421353) - This is STDERR from 8fd93320bf59
04-Jun-2021 (09:34:58.423973) - This is STDOUT from 8fd93320bf59
04-Jun-2021 (09:34:58.423973) - This is STDERR from 8fd93320bf59
04-Jun-2021 (09:34:59.429255) - This is STDOUT from 8fd93320bf59
04-Jun-2021 (09:34:59.429255) - This is STDERR from 8fd93320bf59
04-Jun-2021 (09:35:00.412609) - This is STDOUT from 8fd93320bf59
...
```

## Building the container
Once we have the code we need to prepare the container image that will be used to run the code. The important thing here is that the base image we use must contain the appropriate Python environment to be able to run our Python code.

We also what to keep our image and running container as small as possible so in this case we've opted for a Python specific Alpine image (python:3.6-alpine).

The next steps assume a local Docker environment as already been prepared.

### Preparing build directory
The following dir structure for the build environment...
```
container-log-test
├── Dockerfile
└── app
    └── logging.py
```

### Create Dockerfile
The contents of the 'Dockerfile' are basically a set of instructions on how to build the container image.

`Dockerfile`...
```
FROM python:3.6-alpine
 
MAINTAINER Mark Watsham "mark@watsham.net"
 
WORKDIR /
 
COPY . /
 
ENTRYPOINT [ "python3" ]
 
CMD [ "app/logging.py" ]
```
  `FROM` - Every Dockerfile starts with a FROM keyword. It's used to specify the base image from which the image is built.
  
  `MAINTAINER` - Information about the image author.
  
  `WORKDIR` - sets the working directory in the container which is used by RUN, COPY, etc...
  
  `COPY` - The COPY command is used to copy files/directories from the host machine to the container during the build process. In this case, we are copying the application files.
  
  `ENTRYPOINT` - Defines the entry point of the application i.e python3 <python script file>
  
  `CMD` - What the container executes at runtime. Here it runs the logging.py file in the app directory.

### Build the container image
Here we compile the the container image.

NB: On the first run the the build process will download the python:3.6-alpine image. The following example shows use of a locally cached version from previous builds.
```
$ docker build -t logging-test:0.3 .
[+] Building 2.8s (8/8) FINISHED
 => [internal] load build definition from Dockerfile                                                                                       0.1s
 => => transferring dockerfile: 40B                                                                                                        0.0s
 => [internal] load .dockerignore                                                                                                          0.1s
 => => transferring context: 2B                                                                                                            0.0s
 => [internal] load metadata for docker.io/library/python:3.6-alpine                                                                       2.3s
 => [auth] library/python:pull token for registry-1.docker.io                                                                              0.0s
 => CACHED [1/3] FROM docker.io/library/python:3.6-alpine@sha256:492bb540e9c9bc9f586d5d69467c66bc32072d9af48463b1f0054d4ff9b93709          0.0s
 => [internal] load build context                                                                                                          0.0s
 => => transferring context: 89B                                                                                                           0.0s
 => [2/3] COPY . /                                                                                                                         0.1s
 => exporting to image                                                                                                                     0.1s
 => => exporting layers                                                                                                                    0.1s
 => => writing image sha256:1174578b0c963f9248f79b824e9643cc0a34a2e5e29eb7879413313344115ab8                                               0.0s
 => => naming to docker.io/library/logging-test:0.3
```

## Testing the container image
```
$ docker run -d logging-test:0.3
33e3e18d1edfb70d6cd6833b5acfd25743bf22462883a7f1db31f14d40544c4c
```
### Examining the container log output
```
$ docker logs -n 10 33e3e18d1edfb70d6cd6833b5acfd25743bf22462883a7f1db31f14d40544c4c
08-Jun-2021 (10:49:05.868650) - This is STDERR from 33e3e18d1edf
08-Jun-2021 (10:49:06.874755) - This is STDOUT from 33e3e18d1edf
08-Jun-2021 (10:49:06.874755) - This is STDERR from 33e3e18d1edf
08-Jun-2021 (10:49:07.877766) - This is STDOUT from 33e3e18d1edf
08-Jun-2021 (10:49:07.877766) - This is STDERR from 33e3e18d1edf
08-Jun-2021 (10:49:08.880207) - This is STDOUT from 33e3e18d1edf
08-Jun-2021 (10:49:08.880207) - This is STDERR from 33e3e18d1edf
08-Jun-2021 (10:49:09.886627) - This is STDOUT from 33e3e18d1edf
08-Jun-2021 (10:49:09.886627) - This is STDERR from 33e3e18d1edf
08-Jun-2021 (10:49:10.892490) - This is STDOUT from 33e3e18d1edf
```
