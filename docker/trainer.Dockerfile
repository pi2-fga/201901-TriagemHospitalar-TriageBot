FROM requirements:latest

COPY ./bot /bot

RUN mkdir /src_models

WORKDIR /bot

RUN make train-nlu

RUN make train-core

RUN find /. | grep -E "(__pycache__|\.pyc|\.pyo$)" | xargs rm -rf
