FROM requirements:latest

COPY ./bot /bot

WORKDIR /bot

RUN find /. | grep -E "(__pycache__|\.pyc|\.pyo$)" | xargs rm -rf
