#!/bin/bash
set -e
# setup ros environment
source "/opt/ros/$ROS_DISTRO/setup.bash"
export ROS_PACKAGE_PATH=/cordial:$ROS_PACKAGE_PATH
exec "$@"
