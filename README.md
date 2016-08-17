# Abstractions - Introduction to ML Demo Code

## Overview
This demo code aims to give you an overview of the process of training an ML model using the [scikitlearn], which is a python library. We will run it it an IDE called Jupyter. Jupyter is browser based. You have several ways you can use this demo. See the usage section for me details.
## Usage

### Browser only
The simplest way to run this sample code is to click the link below. It is served up from [MyBinder.org](http://mybinder.org). It's a cool free opensource environment associated with the [binder](project)

[![Binder](http://mybinder.org/badge.svg)](http://mybinder.org:/repo/mobyware/ml-abstractions-intro-python)

### Docker
If you have Docker installed you can simply run the image using

 docker run [TO DO]
 
The dockerfile is also included in the repo if you'd like to build it from scratch or modify and rebuild. To build and run use:
	1. docker build -t <image name you decide> .
	2. docker run -p 8888:8888 <image name you decide>
	
The "p" switch is to map the port. By default my image uses 8888.

### Local
This is more involved but more rewarding. You can run the notebook included locally or any notebook by installing the Anaconda python libraries. Instructions for you OS are [here]().

Once Anaconda is installed you can run the notebook by executing the command below then clicking notebook called index when your browser opens:
 jupyter notebook
