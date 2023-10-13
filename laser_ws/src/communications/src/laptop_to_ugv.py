#!/usr/bin/env python
# license removed for brevity

import rospy
from std_msgs.msg import Bool
# from std_msgs.msg import String
from std_msgs.msg import Float32MultiArray
import sys
import json

class LaptopToUGV:
    # This will store the next coordinate the bot is supposed to go to.
    # coordinates = {
    #    'x0': 0,
    #    'y0': 0,
    #    'x1': 0,
    #    'y1': 0,
    #    'x2': 0,
    #    'y2': 0,
    #    'x3': 0,
    #    'y3': 0,
    #    'x4': 0,
    #    'y4': 0
    # }
    coordinates = [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]
    # This will track the dimensions of the object, length then width
    object_dimensions = [0.761, 0.233]
    # This contains the original distance of the bot from the object.
    object_distance = [1.55, 2.5]
    # This will keep track of the offset distance in meters we need to be from the object.
    offset = 1.0

    def __init__(self):
        rospy.init_node('laptop_to_ugv')

        self.test_publisher = rospy.Publisher('scan_test', Float32MultiArray, queue_size = 10, latch = True)
        self.move_publisher = rospy.Publisher('laser_to_ugv', Bool, queue_size = 10, latch = False)
        self.subscriber = rospy.Subscriber('laptop_to_laser', Bool, self.callback)
	self.scan_count = 0
	self.rate = rospy.Rate(50)

    def register_control(self):
	# de-register registered publishers and subscribers
	if self.test_publisher is not None:
	    print("Deregistering p's and s's")
	    self.test_publisher.unregister()
	    self.move_publisher.unregister()
	    self.subscriber.unregister()
	# re-register unregistered publishers and subscribers
	print("Reregistering p's and s's")
        self.test_publisher = rospy.Publisher('scan_test', Float32MultiArray, queue_size = 10, latch = True)
        self.move_publisher = rospy.Publisher('laser_to_ugv', Bool, queue_size = 10, latch = False)
	self.subscriber = rospy.Subscriber('laptop_to_laser', Bool, self.callback)

    def callback(self, message):
        rospy.loginfo("Can the UGV move? %i", message.data)
        # prepare the response message
        if message.data and self.scan_count == 0:
	    self.positions()
	    rospy.sleep(3)
	    self.move_publisher.publish(True)
	    self.register_control()
	    self.scan_count += 1
	elif message.data and self.scan_count > 0:
	    # Tell the UGV it can move again
            self.move_publisher.publish(True)
	    self.register_control()
	    self.scan_count += 1


    def positions(self):
	# calculate all of the positions relative to the bots starting location
	self.coordinates[2] = self.object_distance[0] + self.object_dimensions[0] + self.offset
	self.coordinates[3] = self.object_distance[1] + self.object_dimensions[1] / 2
	self.coordinates[4] = self.offset + self.object_dimensions[1] / 2
	self.coordinates[5] = self.offset + self.object_dimensions[0] / 2
	self.coordinates[6] = self.offset + self.object_dimensions[0] / 2 
	self.coordinates[7] = self.offset + self.object_dimensions[1] / 2
	self.coordinates[8] = self.offset + self.object_dimensions[1] / 2 
	self.coordinates[9] = self.offset + self.object_dimensions[0] / 2

        #Format the data into json
        # json_coordinates = json.dumps(self.coordinates)
        # prepare the message
        message = Float32MultiArray()
        message.data = self.coordinates
	print(message.data)

        #publish the data to the ugv team
	self.test_publisher.publish(message)
	print("published message to topic scan_test")

if __name__ == '__main__':
    node = LaptopToUGV()
    rospy.spin()
