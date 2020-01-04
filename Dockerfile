ARG PYTHON_IMAGE=python:3.8-buster

# Dev stage
FROM ${PYTHON_IMAGE} as imgboardengdev

# Install gettext if you want to make Django translation strings
# RUN apt-get update && apt-get install -y --no-install-recommends gettext

COPY requirements.txt /tmp/requirements.txt
RUN pip3 install -r /tmp/requirements.txt

RUN mkdir -p /imgboardeng/ && useradd -d /imgboardeng/ -u 1000 python && chown -R python /imgboardeng/

USER python
