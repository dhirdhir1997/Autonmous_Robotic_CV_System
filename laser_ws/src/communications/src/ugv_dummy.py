#!/usr/bin/env python
# license removed for brevity

import rospy
from std_msgs.msg import Bool
from std_msgs.msg import String
import sys
import json
import time

class UGVDummy:
    def __init__(self):
        rospy.init_node('ugv_dummy')

        self.coord_subscriber = rospy.Subscriber('scan_coordinates', String, self.callback1)
        self.move_subscriber = rospy.Subscriber('laser_to_ugv', Bool, self.callback)
        self.publisher = rospy.Publisher('ugv_to_laser', Bool, queue_size = 10)

    def callback(self, message):
        rospy.loginfo("Can we move? %i", message.data)

        # prepare the response message
        if message.data:
		time.sleep(5)
		self.publisher.publish(True)

    def callback1(self, message):
	print("got the coordinates, thank you!")

if __name__ == '__main__':
    node = UGVDummy()
    rospy.spin()
