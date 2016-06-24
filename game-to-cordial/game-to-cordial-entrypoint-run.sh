#!/bin/bash
set -e
source "/opt/ros/$ROS_DISTRO/setup.bash"
source catkin_ws/devel/setup.bash
export ROS_PACKAGE_PATH=/cordial:$ROS_PACKAGE_PATH
rosrun game_to_cordial example.py