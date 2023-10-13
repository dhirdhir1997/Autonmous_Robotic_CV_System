#!/usr/bin/env python
# license removed for brevity
import rospy
import Jetson.GPIO as GPIO
from std_msgs.msg import String

class ActuatorController:

        def __init__(self):
		# Initialize the ROS node
		rospy.init_node('actuator_controller') # initialize the ROS node with the name 'actuator_controller'
		rospy.Subscriber('actuator_topic', String, self.callback) # subscribe to the 'actuator_topic' topic with the callback function 'callback'

		# Set the GPIO pins for the L298N module
		self.gpio_in1 = 11 # set the input pin to 1 WHEN PIN 11 GOES HIGH THE ACUTATOR GOES UP IF PIN 13 IS LOW
		self.gpio_in2 = 13 # set the input pin to 2 WHEN PIN 13 GOES HIGH THE ACTUATOR GOES DOWN IF PIN 11 IS LOW

		# Set the GPIO mode
		GPIO.setmode(GPIO.BOARD) # set the pin numbering mode to BOARD

		# Set the GPIO pins as output
		GPIO.setup(self.gpio_in1, GPIO.OUT)
		GPIO.setup(self.gpio_in2, GPIO.OUT)

		# Keeps the ROS node running until it is killed
		rospy.spin()

	def callback(self, msg):
		if msg.data == "up":
			self.up()
		elif msg.data == "down":
			self.down()
		elif msg.data == "stop":
			self.stop()

	def __del__(self):
		GPIO.cleanup()


	def up(self):
		#  Move the actuator up
		GPIO.output(self.gpio_in1, GPIO.HIGH)
		GPIO.output(self.gpio_in2, GPIO.LOW)
		print("moving actuator up")

	def down(self):
		# Move the actuator down
		GPIO.output(self.gpio_in1, GPIO.LOW)
		GPIO.output(self.gpio_in2, GPIO.HIGH)
		print("Moving actuator down")

	def stop(self):
		# Stop the motor
		GPIO.output(self.gpio_in1, GPIO.LOW)
		GPIO.output(self.gpio_in2, GPIO.LOW)
		print("Stopping the motor")


if __name__ == '__main__':
	node = ActuatorController()
