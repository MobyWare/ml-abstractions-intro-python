# Abstractions - Introduction to Machine Learning (ML) Demo Code

## Overview
This demo code aims to give you an overview of the process of training an ML model using the [scikit-learn](http://scikit-learn.org/), which is a Python library. We will run it in an IDE called Jupyter that you can use from your browser. Jupyter supports several languages including Python. 

The walk-through trains a simple model on a small set of housing data. The goal is to predict housing prices based on zip and square-footage. You want the root-mean-squared error of your prediction to be as small as possible. You will learn how to do that by:

1. How to visualize the data.
2. How to train an evaluate a model.
3. How to improve model performance by correctly encoding categorical data.

## Usage
You can learn more about running python code in the Jupyter IDE [here](http://jupyter-notebook.readthedocs.io/en/latest/examples/Notebook/Running%20Code.html). Below you can learn how to launch the Jupyter environment with the preloaded data and code you need.

### Browser only
The simplest way to run this sample code is to click the link below. It is served up from [MyBinder.org](http://mybinder.org). It's a cool free open-source software (OSS) environment associated with the OSS project called [binder](https://github.com/binder-project/binder)

[![Binder](http://mybinder.org/badge.svg)](http://mybinder.org:/repo/mobyware/ml-abstractions-intro-python)

### Docker
If you have Docker installed you can simply run the image using

> docker run -p 8888:8888 mobyware/anaconda
 
The dockerfile is also included in the repo if you'd like to build it from scratch or modify and rebuild. To build and run use:

> docker build -t <image name you decide> .
> docker run -p 8888:8888 <image name you decide>
	
The "p" switch is to map the port. By default my image uses 8888.

### Local
This is more involved but more rewarding. You can run the notebook included locally or any notebook by installing the Anaconda python libraries. Instructions for you OS are [here](https://docs.continuum.io/anaconda/install).

Once Anaconda is installed you can run the notebook by executing the command below then clicking notebook called index when your browser opens:
> jupyter notebook
