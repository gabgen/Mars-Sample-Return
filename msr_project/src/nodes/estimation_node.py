#!/usr/bin/env python

import rospy
import threading

from std_msgs.msg import *
from darknet_ros_msgs.msg import *
import sensor_msgs.point_cloud2 as pc2
from sensor_msgs.msg import PointCloud2, PointField


class INIT():
        #Values Initialization    
	def __init__(self):
		rospy.init_node('estimation_node',anonymous=True)
		global center_x, center_y, scale_factor
	        
		scale_factor=1000
                center_x,center_y,u,v = 0,0,0,0

		print("Starting Pose Estimation")
		

class INPUT(threading.Thread):
        
        # Initialization of subscribing elements  
	def __init__(self,bounding_boxes = '/darknet_ros/bounding_boxes', point_cloud="/camera/depth_registered/points"):
                threading.Thread.__init__(self)
		self.bounding_boxes = bounding_boxes
                self.point_cloud = point_cloud


        # Subscribing to bounding box and point cloud topics
	def run(self):
		self.bounding_boxes_sub = rospy.Subscriber(self.bounding_boxes, BoundingBoxes, self.bbox)
		self.pc_prova_sub = rospy.Subscriber(self.point_cloud, PointCloud2, self.pc_prova)

        # Reading bounding box coordinates and related center
	def bbox(self, data):	
										
		global center_x,center_y

		values = data.bounding_boxes
		for data in values:

			bb_xmin = data.xmin
			bb_ymin = data.ymin
			bb_xmax = data.xmax
			bb_ymax = data.ymax
			
			w = bb_xmax - bb_xmin
			h = bb_ymax - bb_ymin
			center_x = bb_xmin + w/2
			center_y = bb_ymin + h/2


        # PointCloud2 message is saved in "point_saved" . The coordinates are scaled in mm and published
	def pose_estimation(self,data):
            
                #u : width
                #v : height

                u=center_x
                v=center_y
               
                point_saved = pc2.read_points(data, field_names = ("x", "y", "z"), skip_nans=True, uvs=[[u,v]]) 
                point=next(point_saved, None)

                pt_x = int(point[0]*scale_factor)
                pt_y = int(point[1]*scale_factor)
                pt_z = int(point[2]*scale_factor)

                print ("The bounding box center (x,y) in px is : {} - {}".format(u , v) )	                
                print("The x coordinate is  %d mm " %pt_x )
                print("The y coordinate is  %d mm " %pt_y )
                print("The z coordinate is  %d mm " %pt_z )
                
  

if __name__ == '__main__':

	init = INIT()
      
	i = INPUT()    
	i.start()

        rospy.spin()
