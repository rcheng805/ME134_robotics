#!/usr/bin/env python
 
## Publish goal messages to the move_base node 
## Students must complete this template with the correct message format
## to the correct topic
import rospy
from std_msgs.msg import String
from geometry_msgs.msg import PoseStamped

def talker():

    
    ### FINISH THIS LINE TO PUBLISH TO CORRECT TOPIC WITH CORRECT MESSAGE TYPE
    pub = rospy.Publisher(...)
    ######
    
    rospy.init_node('talker', anonymous=True)
    rate = rospy.Rate(10) # 10hz
    while not rospy.is_shutdown():
        goal = PoseStamped()
        ### WRITE YOUR SCRIPT HERE...
        ###
        ###
        ###
        #rospy.loginfo(goal)
        pub.publish(goal)
        rate.sleep()

if __name__ == '__main__':
    try:
        talker()
    except rospy.ROSInterruptException:
        pass
