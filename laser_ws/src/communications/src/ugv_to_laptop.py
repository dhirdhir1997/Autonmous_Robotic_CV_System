#!/usr/bin/env python
# license removed for brevity
import rospy
from std_msgs.msg import Bool
from std_msgs.msg import String
import sys
import socket
import time

class UGVToLaptop:
	def __init__(self):
		rospy.init_node('ugv_to_laptop')

		self.actuator_publisher = rospy.Publisher('actuator_topic', String, queue_size = 10, latch = False)
		self.pc_publisher = rospy.Publisher('laptop_to_laser', Bool, queue_size = 10, latch = False)
		self.subscriber = rospy.Subscriber('ugv_to_laser', Bool, self.callback)

		#This is the IP of the computer we're going to connect to
		self.HOST = "192.168.137.119"
		print("Attempting to connect to HOST")

		# initialize the connection
		self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		self.sock.connect((self.HOST, 1234))
		print("Connection made with " + self.HOST)
		print("Connection made with Host") # DELETE AFTER TESTNG

		self.can_move = True # a flag for us to use to tell the vehicle it can move or not
		self.full_msg = '' # a place to store the message
		#self.rate = rospy.Rate(50)

	def callback(self, message):
		rospy.loginfo("Can we scan? %i", message.data)

		# prepare the  response message
		if message.data:
			# back up publication to send the message for redundancy
			# aka, echo the /laser_to_laptop topic to hear the message
			# to the PC
			print(message.data)

			# indicate that we are scanning and shouldn't move
			#self.can_move = False
			#print(self.can_move)

			# Let the actuator go up for 5 seconds
			self.actuator_publisher.publish("up")
			time.sleep(5)
			# Stop the actuator motion
			self.actuator_publisher.publish("stop")

			# Move the actuator down before moving again
			self.actuator_publisher.publish("down")
			time.sleep(5)
			# stop the actuator
			self.actuator_publisher.publish("stop")

			# prepare the message to be sent via socket
			message_to_send = message.data
			# send the message to the server
			self.sock.send(str(message_to_send).encode('utf-8'))
			print("Sent a message that we can start the scan")

			#indicate that we are scanning and shouldn't move
			self.can_move = False

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
			if self.full_msg == "True": self.can_move = True
			# publish the message
			#self.pc_publisher.publish(self.can_move)


		# send the move message
		self.pc_publisher.publish(self.can_move)

	def startup(self):
		self.pc_publisher.publish(True)


if __name__ == '__main__':
	node = UGVToLaptop()
	node.startup()
	rospy.spin()
