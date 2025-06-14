FROM ubuntu:latest

# Install dependencies
RUN apt-get update && apt-get install -y \
    python3 \
    python3-venv \
    git

RUN python3 -m venv /venv
RUN /venv/bin/pip install PyYAML

COPY feed.py /usr/bin/feed.py
COPY entrypoint.sh /entrypoint.sh

ENTRYPOINT ["/entrypoint.sh"]