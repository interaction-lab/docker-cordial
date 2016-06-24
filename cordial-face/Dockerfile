FROM agakshat/cordial
RUN cp -r /cordial/cordial_face/web /var/www/
RUN apt-get update && apt-get install -y lighttpd
EXPOSE 80
ADD cordial-face_entrypoint.sh /
ENTRYPOINT ["./cordial-face_entrypoint.sh"]