FROM ros:indigo

ADD pyvona-master.zip .
ADD maestro-linux.zip .

RUN apt-get update && apt-get install -y ros-indigo-rosbridge-suite python-gst0.10 python-scipy unzip python-pygame ros-indigo-tf python-serial python-requests vorbis-tools libusb-1.0-0-dev mono-runtime libmono-winforms2.0-cil
RUN unzip pyvona-master.zip && cd pyvona-master && ./setup.py install && cd .. && rm -rf pyvona-master && rm pyvona-master.zip
RUN unzip maestro-linux.zip && cp ./maestro-linux/99-pololu.rules /etc/udev/rules.d && rm maestro-linux.zip