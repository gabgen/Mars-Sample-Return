# Mars-Sample-Return
Ros repository of a possible autonomous recognition stoftware for the Mars Sample Return's Fetch Rover.
![Fetch Rover](/MSR/logo.png)

## What Mars Sample Return is ?
It is a Nasa and Esa space mission aimed to bring back to the Earth martian soil,rocks and gas inside small samples.
This research project has been realized in Thales Alenia Space site(Turin) in collaboration with PIC4SER(Mechatronic research group of Polytechnic University of Turin).

## Hardware 
- Realsense D435i depth camera
- Nvdia Jetson Nano 

## Software  
- ROS Melodic with the following packages:
  - realsense package
  - darknet package
  - opencv package
  - image pipeline package
 
- AlexeyAB repository (https://github.com/AlexeyAB/darknet.git)
- Realsense driver
- CUDA driver

## Project implementation
In order to realise this solution, three main steps have occured:

#### 1. Dataset images collection phase 
 The dataset contains about 5000 training-images and 700 test-images. The system recognise only the class "sample" . The model of the sample is designed with Solidworks.
 The images have been captured in Roxy(ROver eXploration facilitY) area , located in Thales Alenia Space site, in Turin. Several conditions have been reproduced during the dataset realisetion:
 - lighting condition (up to 30k lux)
 - distance (0.5m to 5m)
 - sample visible or partially occluded
 - sample covered by soil
 - sample undershadow
 
 #### 2. Re-training phase 
 It has been occured a re-training phase of the popular YOLO algorithm aimed to teach Yolo how to recognise the sample.
 YOLO versions involved :
 -YOLO v3 tiny
 -YOLO v3 tiny 3l ( it contains a third detection layer)
 The versions have been modified for the specific purpose. The re-training has been realized on Google Colab platform thanks to AlexeyAB's repository.
 
 #### 3. Estimation node phase 
 The last step concerns the implementation of an "estimation_node" . It has the task to connect the object detection system and the depth camera system. 

 

## How to install it 
Download the "msr_project" package and move it in your "catkin/src/" folder. Then re-build your ROS environment. 

## How to use it 
Launch the "device_start_complete.launch" file . It will run the required nodes with related parameters:
- the depth camera node 
- the darknet node
- the pose estimation node
The yolo output and the original image will appear on the screen while on an another terminal screen the coordinates information of the recognised objects will be published.
![output](https://github.com/gabgen/Mars-Sample-Return/blob/main/MSR/test.PNG)
