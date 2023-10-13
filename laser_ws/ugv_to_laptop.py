#!/usr/bin/env python
# license removed for brevity
import rospy
from std_msgs.msg import Bool
import sys

# this is only for testing purposes, delete later vvv
import random

class UGVToLaptop:
	def __init__(self):
		rospy.init_node('ugv_to_laptop')

		self.publisher = rospy.Publisher('laser_to_laptop', Bool, queue_size = 10)
		self.subscriber = rospy.Subscriber('ugv_to_laser', Bool, self.callback)

	def callback(self, message):
		rospy.loginfo("Can we scan? %i", message.data)

		# prepare the  response message
		if message.data:
			self.publisher.publish(message.data)


if __name__ == '__main__':
	node = UGVToLaptop()
	rospy.spin()
