FROM agakshat/cordial

RUN /bin/bash -c "source /opt/ros/indigo/setup.bash"
RUN mkdir -p ./catkin_ws/src && cd ./catkin_ws/src
ADD src ./catkin_ws/src/

ADD game-to-cordial-buildfile.sh /
RUN /game-to-cordial-buildfile.sh

ADD game-to-cordial-entrypoint.sh /
ADD game-to-cordial-entrypoint-launch.sh /
ADD game-to-cordial-entrypoint-run.sh /
ADD game-to-cordial-entrypoint-jack.sh /
ADD .asoundrc /root/

ENTRYPOINT ["./game-to-cordial-entrypoint.sh"]
