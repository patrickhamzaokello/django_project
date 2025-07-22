FROM ubuntu:latest
LABEL authors="pkase"

ENTRYPOINT ["top", "-b"]