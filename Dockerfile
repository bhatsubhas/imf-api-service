ARG NONROOT_IMAGE=gcr.io/distroless/python3-debian12@sha256:fdb3a044d46989e59648dae450d09cd76560013c12947ee4102a416e39621fb9

FROM debian:12-slim AS build
RUN apt-get update && \
    apt-get install --no-install-suggests --no-install-recommends --yes python3-venv gcc libpython3-dev && \
    python3 -m venv /venv && \
    /venv/bin/pip install --upgrade pip setuptools wheel

FROM build AS build-env
COPY requirements requirements
COPY requirements.txt requirements.txt
RUN /venv/bin/pip install --disable-pip-version-check -r /requirements.txt

FROM ${NONROOT_IMAGE}
COPY --from=build-env /venv /venv
WORKDIR /app
COPY gunicorn.conf.py .
COPY api api/
ENTRYPOINT [ "/venv/bin/gunicorn", "api.app:app" ]
