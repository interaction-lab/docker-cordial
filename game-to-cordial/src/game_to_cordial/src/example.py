#!/usr/bin/env python

import roslib; roslib.load_manifest('game_to_cordial')
import rospy
from robot_manager import RobotManager
from sar_robot_command_msgs.msg import RobotCommand
import re
import os
import yaml
import rospkg

rospy.init_node('game_listener')
rm = RobotManager("DB1")

rospack = rospkg.RosPack()
path = rospack.get_path('game_to_cordial')
with open(path+"/speech/phrases.yaml") as f:
	phrases = yaml.load(f)
f.close()

def callback(data):
	rospy.loginfo(rospy.get_caller_id() + ": I heard %s", data.id)
	if data.id in phrases:
		rm.say(data.id, interrupt=True) #maybe change wait=True to interrupt=False
	else:
		rm.say(data.properties, interrupt=True) #maybe change wait=True to interrupt=False

def listener():
	rospy.Subscriber("robot_command",RobotCommand,callback)
	rospy.spin()

if __name__ == '__main__':
	try:
		listener()
	except rospy.ROSInterruptException:
		pass



