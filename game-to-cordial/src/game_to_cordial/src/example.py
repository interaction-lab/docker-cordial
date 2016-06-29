#!/usr/bin/env python

# Akshat Agarwal
# June 2016
#
# The MIT License (MIT)
#
# Copyright (c) 2016 USC Interaction Lab
# 
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
# 
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
# 
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

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