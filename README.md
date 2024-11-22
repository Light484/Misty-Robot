# HRI - Simon Says With Misty II

## Description
This code gives a Misty robot the ability to engage in a Simon Says game either while gazing at a participant or staring blankly. This code is used in a Human-Robot Interaction study that evaluates the effect of robot gaze on human mental workload during problem solving tasks.

## Installation
Installation instructions vary from the instructions provided in the [mistyPy documentation](https://pypi.org/project/mistyPy/). 

1. Download Anaconda: </br> ```https://www.anaconda.com/download/```
2. Open a terminal using the Anaconda UI and enter: </br> ```conda create -n <your_custom_environment_name> python=3.12 requests```
3. Now that your environment is set up, activate the environment using the ```<custom-environment-name>``` you chose: </br> 
* ```conda source activate misty_developer```
* ```pip install mistyPy```
* ```pip install websocket-client==0.52.0```

Every time you open a new terminal enter:
```conda source activate <your_custom_environment_name>```

## Usage
Code provided can only run on the Misty II robot. Robot implementation is written in Python using the mistyPy package.

## Authors
Anna Sheaffer, Marti Zentmeier, Qimou Zhou