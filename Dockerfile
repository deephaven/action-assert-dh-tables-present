FROM docker/compose:alpine-1.29.2

COPY entrypoint.sh /entrypoint.sh
COPY validate /assert-tables

ENTRYPOINT ["/entrypoint.sh"]
