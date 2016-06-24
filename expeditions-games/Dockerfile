FROM agakshat/game-to-cordial
COPY ./public_html /var/www
RUN apt-get update && apt-get install -y lighttpd
EXPOSE 80
ADD games_entrypoint.sh /
ENTRYPOINT ["./games_entrypoint.sh"]