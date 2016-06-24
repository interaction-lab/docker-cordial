FROM agakshat/cordial-base
ADD cordial ./cordial
ADD cordial_entrypoint.sh /
RUN apt-get update && apt-get install -y ros-indigo-rospy-tutorials python-twisted
RUN /cordial_entrypoint.sh rosmake cordial_dragonbot cordial_tablet
ENTRYPOINT ["./cordial_entrypoint.sh"]