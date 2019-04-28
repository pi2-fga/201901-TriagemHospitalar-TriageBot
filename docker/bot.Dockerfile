FROM requirements:latest

COPY ./bot /bot
COPY ./scripts /scripts

WORKDIR /bot

ENV MAX_TYPING_TIME=10                     \
    MIN_TYPING_TIME=1                      \
    WORDS_PER_SECOND_TYPING=5              \
    ENVIRONMENT_NAME=localhost             \
    BOT_VERSION=last-commit-hash           \
    ENABLE_ANALYTICS=True                 \
    ELASTICSEARCH_URL=elasticsearch:9200

RUN find . | grep -E "(__pycache__|\.pyc|\.pyo$)" | xargs rm -rf

CMD make run-api
