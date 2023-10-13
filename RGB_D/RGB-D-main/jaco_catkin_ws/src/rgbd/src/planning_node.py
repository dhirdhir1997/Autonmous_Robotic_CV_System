#!/usr/bin/env python
import rospy
from std_msgs.msg import String, Bool
from geometry_msgs.msg import Pose
from geometry_msgs.msg import Twist
from geometry_msgs.msg import Point
from geometry_msgs.msg import Quaternion
from std_srvs.srv import Trigger
import stlMeasure
import numpy 
	
arm_pub = None
ugv_pub = None
rgbd_pub = None
home_arm_pub = None
object_side = 0
arm_points_completed = 0
arm_points_sent = 0
long_length = 0
short_length = 0
height = 0
stl_file_name = "Cutethang.STL"
jaco_done = False
JACO_X_OFFSET = 0.6
CAMERA_OFFSET = 0.7
JACKAL_ROTATION_SPEED = 0.5 # [rad/s]
JACKAL_ROTATION = 1.57079632679 + 0.05 #[rad] added for compensation
JACKAL_LINEAR_SPEED = 0.2 #should be [m/s]
HOME_POSITION = Point(0.210790961981, -0.275413990021, 0.488662302494)
HOME_ORIENTATION = Quaternion (0.610213339329, 0.342876464128, 0.364067733288, 0.614434719086)
HOME_POSE = Pose(HOME_POSITION, HOME_ORIENTATION)


def close_fingers_callback(data):
	# here the camera has determined where the object of interest is and we need
	#to tell the UGV to go there. Not sure how to line the maps up, that will be tough
	#this is the path that the code will take to tell the UGV where to go
	# How do we control the JACKAL?????
	pass

def publish_to_arm(pose):
	global jaco_done
	jaco_done = False
	arm_pub.publish(pose)
	global arm_points_sent 
	arm_points_sent += 1


def makeRectangle(pose, lower_y, upper_y, lower_z, upper_z):
	pose.position.y = lower_y
	pose.position.z = lower_z
	#print(pose)
	publish_to_arm(pose)

	pose.position.z = upper_z
	#print(pose)
	publish_to_arm(pose)

	pose.position.y = upper_y
	#print(pose)
	publish_to_arm(pose)

	pose.position.z = lower_z
	#print(pose)
	publish_to_arm(pose)

	pose.position.y = lower_y
	#print(pose)
	publish_to_arm(pose)

def new_grid(length):
	pose_1 = Pose(Point(0.623664546013, -0.222178667784, 0.0826868936419), Quaternion(0.401, 0.441, 0.567, 0.568))
	pose_1_ = Pose(Point(pose_1.position.x, pose_1.position.y+long_length, pose_1.position.z), pose_1.orientation) 
	pose_2 = Pose(Point(pose_1.position.x, pose_1.position.y, pose_1.position.z+height), pose_1.orientation)
	pose_2_ = Pose(Point(pose_1.position.x, pose_1.position.y+long_length, pose_1.position.z+height), pose_1.orientation)
	pose_3 = Pose(Point(pose_1.position.x, pose_1.position.y+(long_length/2), pose_1.position.z+height), pose_1.orientation)
	pose_4 = Pose(Point(pose_1.position.x, pose_1.position.y+(long_length/2), pose_1.position.z), pose_1.orientation)

	arm_pub.publish(pose_1)
	rospy.sleep(10)
	arm_pub.publish(pose_2)
	rospy.sleep(15)
	arm_pub.publish(pose_3)
	rospy.sleep(15)
	arm_pub.publish(pose_4)
	rospy.sleep(15)
	arm_pub.publish(pose_1)
	rospy.sleep(15)
	arm_pub.publish(pose_4)
	rospy.sleep(20)
	arm_pub.publish(pose_3)
	rospy.sleep(15)
	arm_pub.publish(pose_2_)
	rospy.sleep(20)
	arm_pub.publish(pose_1_)
	rospy.sleep(15)
	arm_pub.publish(pose_4)
	rospy.sleep(15)
	arm_pub.publish(HOME_POSE)
	rospy.sleep(15)

def executeGrid(y_length, z_height):
	print("executing grid")
	global jaco_done
	#jaco_done = False
	desired_arm_pose = Pose()
	desired_arm_pose.orientation = Quaternion(0.401, 0.441, 0.567, 0.568)
	desired_arm_pose.position.x = 1 * JACO_X_OFFSET #hardcoded distance from UGV
	y_length = y_length - 0.2 #remove length since camera has wider field of view
	y_min = y_length / (-2)
	y_max = y_length / (2)
	z_min = 0
	z_max = z_height - 0.2 #allow camera field of view to help

	y_step = 0.1
	rectangles = 3
	y_values = numpy.linspace(y_min, y_max, num = rectangles)
	print("y values: ")
	print(y_values)
	for i in range(rectangles - 1):
		print("sent rectangle")
		makeRectangle(desired_arm_pose, y_values[i], y_values[i+1], z_min, z_max)
	#new_grid(y_length)
	while ( jaco_done != True):
		# print(jaco_done)
		print(arm_points_completed)
		rospy.sleep(1)
	print("Motion completed")
	home_arm_pub.publish(String("home"))
	rospy.sleep(10)
	#we want to wait here until the arm has completed its motion
	#while !(arm x == final_x && arm.z == final_z)

def sendUGVCommands(delay, msg):
	#print(delay)
	start_time = rospy.get_time()
	while (rospy.get_time() - start_time < delay):
		ugv_pub.publish(msg)
		rospy.sleep(0.1)

def moveUGV(first_move_length, second_move_length):
	# added to skip moving the UGV
	print("turning UGV")
	
	#move along first axis
	print("linear")
	msg = Twist()
	msg.linear.x = JACKAL_LINEAR_SPEED
	delay = first_move_length / JACKAL_LINEAR_SPEED
	sendUGVCommands(delay, msg)

	#turn CCW 90 degrees
	print("rotation")
	msg = Twist()
	msg.angular.z = JACKAL_ROTATION_SPEED
	delay = JACKAL_ROTATION / JACKAL_ROTATION_SPEED
	sendUGVCommands(delay, msg)
	
	#move along second axis
	print("linear")
	msg = Twist()
	msg.linear.x = JACKAL_LINEAR_SPEED
	delay = second_move_length / JACKAL_LINEAR_SPEED
	sendUGVCommands(delay, msg)

 


#Need to listen to /ugv_arrived. In this callback, start the logic to make the grid
def ugv_arrived_callback(data):


	ack = String("Ack")
	rgbd_pub.publish(ack)
	
	offset = JACO_X_OFFSET + CAMERA_OFFSET #fixed offset from Jackal to box

	global jaco_done
	jaco_done = False
	
	msg = Twist()
	msg.angular.z = -1 * JACKAL_ROTATION_SPEED 
	delay = JACKAL_ROTATION / JACKAL_ROTATION_SPEED
	sendUGVCommands(delay, msg)
	
	#We are at the first side, run grid
	executeGrid(long_length, height)

	#move jackal from long side to short side
	first_move = (long_length / 2) + offset
	second_move = (short_length / 2) + offset

	moveUGV(first_move, second_move) 

	#at second side (short)
	executeGrid(short_length, height)
	#Move Jackal to long side
	first_move = (short_length / 2) + offset
	second_move = (long_length / 2) + offset
	moveUGV(first_move, second_move) 
	
	#at third side (long)
	executeGrid(long_length, height)
	#move Jackal to Short side
	first_move = (long_length / 2) + offset
	second_move = (short_length / 2) + offset
	moveUGV(first_move, second_move) 
	
	#at fourth side (short)
	executeGrid(short_length, height)
	#we have scanned all 4 sides

def arm_move_testing(data):
	pose_1 = Pose(Point(0.623664546013, -0.222178667784, 0.0826868936419), Quaternion(0.401, 0.441, 0.567, 0.568))
	pose_1_ = Pose(Point(pose_1.position.x, pose_1.position.y+long_length, pose_1.position.z), pose_1.orientation) 
	pose_2 = Pose(Point(pose_1.position.x, pose_1.position.y, pose_1.position.z+height), pose_1.orientation)
	pose_2_ = Pose(Point(pose_1.position.x, pose_1.position.y+long_length, pose_1.position.z+height), pose_1.orientation)
	pose_3 = Pose(Point(pose_1.position.x, pose_1.position.y+(long_length/2), pose_1.position.z+height), pose_1.orientation)
	pose_4 = Pose(Point(pose_1.position.x, pose_1.position.y+(long_length/2), pose_1.position.z), pose_1.orientation)

	arm_pub.publish(pose_1)
	rospy.sleep(10)
	arm_pub.publish(pose_2)
	rospy.sleep(15)
	arm_pub.publish(pose_3)
	rospy.sleep(15)
	arm_pub.publish(pose_4)
	rospy.sleep(15)
	arm_pub.publish(pose_1)
	rospy.sleep(15)
	arm_pub.publish(pose_4)
	rospy.sleep(20)
	arm_pub.publish(pose_3)
	rospy.sleep(15)
	arm_pub.publish(pose_2_)
	rospy.sleep(20)
	arm_pub.publish(pose_1_)
	rospy.sleep(15)
	arm_pub.publish(pose_4)
	rospy.sleep(15)
	arm_pub.publish(HOME_POSE)


def move_ugv_testing(data):
	msg = Twist()
	msg.angular.z = -1 * JACKAL_ROTATION_SPEED 
	delay = JACKAL_ROTATION / JACKAL_ROTATION_SPEED
	sendUGVCommands(delay, msg)


def arm_complete_callback(data):
	print("arm_complete_callback")
	print(data)
	#print(data.data)
	global jaco_done
	jaco_done = data.data
	print(jaco_done)	


	

# main function that gets called to start the program
if __name__ == '__main__':
	try:
		rospy.init_node('planning_node', anonymous=True)
		#home_arm()
		arm_pub = rospy.Publisher('/desired_arm_pose', Pose, queue_size = 100)
		ugv_pub = rospy.Publisher('/jackal_velocity_controller/cmd_vel', Twist, queue_size = 1)
		rgbd_pub = rospy.Publisher('/rgbd/message', String, queue_size = 10)
		home_arm_pub = rospy.Publisher("/Home_Arm", String, queue_size = 10)
		
	
	#types of these subscriptions could change
		rospy.Subscriber("/close_fingers", String, close_fingers_callback)
		rospy.Subscriber("/ugv/message", String, ugv_arrived_callback)
		rospy.Subscriber("/Jaco_Complete", Bool, arm_complete_callback)
		rospy.Subscriber("/move_ugv_testing", String, move_ugv_testing)
		rospy.Subscriber("/arm_move_testing", String, arm_move_testing)
		print("reading file")
		minx, maxx, miny, maxy, minz, maxz = stlMeasure.find_mins_maxs(stl_file_name) # see stl_measure.py file in the same src folder
		print("done reading stl")
		if ((maxx - minx) > (maxy - miny)):
			long_length = maxx - minx
			short_length = maxy - miny
		else:
			short_length = maxx - minx
			long_length = maxy - miny
		height = maxz - minz 
		#above defines global variables for grid creation based on dimensions of stl
		home_arm_pub.publish(String("Initial homing"))
		print("home Arm")
		print(long_length, short_length, height)

		rospy.spin()
		
		# the arm will publish here (or something like it) when if completes each point
	except rospy.ROSInterruptException:
	    pass








