#!/usr/bin/env python
# license removed for brevity
import rospy
from std_msgs.msg import Bool
from std_msgs.msg import String
import sys
import socket
import time

# To run this node open a termnial and enter these commands:
# roscore

# You will also need two additional terminals, the first will
# allow you to make sure the node is sending the signal to start path
# planning calculations. Enter these commands:
# cd ~/Desktop/Laser/laser_ws
# source devel/setup.bash
# rostopic echo /laptop_to_laser

# The second one will allow you to immitate the UGV and send the scan command
# To do this, enter the following commands:
# cd ~/Desktop/Laser/laser_ws
# source devel/setup.bash

# Only run this line when you are ready to start a test in the second window:
# rostopic pub /ugv_to_laser std_msgs/Bool True

# Then open one final terminal and type these commands:
# cd ~/Desktop/Laser/laser_ws
# source devel/setup.bash

# Once you are ready to test your script after editing, run these lines:
# catkin_make
# rosrun communications steve_ntp_testing.py

class UGVToLaptop:
	def __init__(self):
		rospy.init_node('ugv_to_laptop')

		self.nano_publisher = rospy.Publisher('laser_to_laptop', Bool, queue_size = 10)
		self.pc_publisher = rospy.Publisher('laptop_to_laser', String, queue_size = 10)
		self.subscriber = rospy.Subscriber('ugv_to_laser', Bool, self.callback)

		#This is the IP of the computer we're going to connect to
		self.HOST = "172.20.10.6"
		print("Attempting to make connection")

		# initialize the connection
		self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		self.sock.connect((self.HOST, 1234))
		print("connection made with " + self.HOST)

		self.can_move = True # a flag for us to use to tell the vehicle it can move or not
		self.full_msg = '' # a place to store the message

	def callback(self, message):
		rospy.loginfo("Can we scan? %i", message.data)

		# prepare the  response message
		if message.data:
			# back up publication to send the message for redundancy
			# aka, echo the /laser_to_laptop topic to hear the message
			# to the PC
			print(message.data)
			#indicate that we are scanning and shouldn't move
			self.can_move = False
			# prepare the message to be sent via socket
			message_to_send = message.data
			# send the message to the server
			self.sock.send(str(message_to_send).encode('utf-8'))
			print("sent message that we can start the scan")

		while self.can_move == False:
			# reset the overall message
			self.full_msg = ''
			# placeholder for the message incoming from the computer
			msg = ''
			# reconnect to the server, failsafe just incase connectivity issues
			# self.sock = socket.socket(AF_INET, socket.SOCK_STREAM)
			# self.sock.connect((self.HOST, 1234))
			# recieve the message from the server
			while msg == '':
				msg = self.sock.recv(50)
			# decode it so we can use it
			self.full_msg = msg.decode("utf-8")

			# if the message received is True, we are done scanning and can move
			if self.full_msg == True: self.can_move = True
			print(type(self.full_msg))
			print(self.full_msg)
			print(self.can_move)

			self.pc_publisher.publish(self.can_move)


if __name__ == '__main__':
	node = UGVToLaptop()
	rospy.spin()
