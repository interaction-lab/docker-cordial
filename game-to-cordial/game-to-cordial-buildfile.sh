#!/bin/bash
set -e
source "/opt/ros/$ROS_DISTRO/setup.bash"
cd catkin_ws/src
catkin_init_workspace
cd ..
catkin_make
cd src/game_to_cordial/speech
export ROS_PACKAGE_PATH=/cordial:$ROS_PACKAGE_PATH
./gen_audio.sh
rosdep install -y cordial_sound
apt-get update && apt-get install -y alsa jackd1