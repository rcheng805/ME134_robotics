#!/usr/bin/env python

import rospy
import tf2_ros
import ros_numpy
import actionlib
from std_msgs.msg import String
from geometry_msgs.msg import PoseStamped
from geometry_msgs.msg import PoseWithCovarianceStamped
from geometry_msgs.msg import Pose, Point
from nav_msgs.msg import OccupancyGrid
from nav_msgs.msg import MapMetaData
from sensor_msgs.msg import LaserScan
#from actionlib_msgs.msg import GoalStatusArray
from move_base_msgs.msg import MoveBaseAction, MoveBaseGoal
from tf.transformations import euler_from_quaternion, quaternion_from_euler
#from std_msgs.msg import Int8MultiArray
import numpy
import math
import matplotlib.pyplot as plt

def scanCallback(self,scanData):
        rospy.loginfo(rospy.get_caller_id()+" scan received.")
        scanRanges = scanData.ranges
	for i in range(length(scanRanges)):
		
	scanRanges_processed = scanRanges
	scanData.scanRanges_processed
	pub.publish(scanData)
        pass      

if __name__ == '__main__':
    rospy.init_node('scan_fix', anonymous=False)
    rospy.Subscriber("scan", LaserScan, self.scanCallback)
    pub = rospy.Publisher("base_scan", LaserScan, queue_size=5)
    rate = rospy.Rate(10.0)
    while not rospy.is_shutdown():
        rate.sleep()
