#!/bin/bash
set -e
source "/opt/ros/$ROS_DISTRO/setup.bash"
source catkin_ws/devel/setup.bash
export ROS_PACKAGE_PATH=/cordial:$ROS_PACKAGE_PATH
jackd -R -d alsa -d hw:1 & roslaunch game_to_cordial run.launch