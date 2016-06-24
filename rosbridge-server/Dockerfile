FROM agakshat/game-to-cordial
RUN apt-get update && apt-get install -y python-twisted ros-indigo-rosbridge-server
ADD rosbridge_server_entrypoint.sh /
ENTRYPOINT ["./rosbridge_server_entrypoint.sh"]