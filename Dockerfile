ARG BASE_REGISTRY=my.repo
ARG BUILD_BASE_IMAGE=ubi9/python-311
ARG BUILD_BASE_TAG=1-52

FROM $BASE_REGISTRY/$BUILD_BASE_IMAGE:$BUILD_BASE_TAG as python-base

RUN pip config set global.index-url http://my.private.repo/artifactory/api/pypi/pypi-public/simple && pip config set global.trusted-host my.private.repo



FROM python-base as poetry-base

USER root

COPY pyproject.toml poetry.lock .

RUN pip install -U pip setuptools \
	&& pip install poetry poetry-plugin-export

# Exports requirements.txt from pyproject.toml
RUN poetry export -f requirements.txt --output /requirements.txt



FROM python-base as runtime

ARG BASE_REGISTRY
ARG BUILD_BASE_IMAGE
ARG BUILD_BASE_TAG

LABEL org.opencontainers.image.base.name=$BASE_REGISTRY/$BUILD_BASE_IMAGE:$BUILD_BASE_TAG


WORKDIR /opt/app-root/src

COPY --from=poetry-base /requirements.txt .

RUN pip install -r requirements.txt

COPY src src/
COPY config.template.ini config.ini

USER default

# Start the application
CMD ["bash", "-c", "python src/my_package/main.py"]
