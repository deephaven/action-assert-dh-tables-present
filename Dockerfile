FROM docker/compose:alpine-1.29.2

COPY entrypoint.sh /entrypoint.sh
COPY validate /github-actions-validate

RUN ["chmod", "+x" ,"/entrypoint.sh"]

ENTRYPOINT ["/entrypoint.sh"]
