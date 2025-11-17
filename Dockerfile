ARG DEBIAN_12_IMAGE=debian@sha256:936abff852736f951dab72d91a1b6337cf04217b2a77a5eaadc7c0f2f1ec1758
ARG NONROOT_IMAGE=gcr.io/distroless/python3-debian12@sha256:1a7c3d2445f783c51be174c8913624dc5bea2cd7ff1f94b9a229a16f0e40fa34

FROM ${DEBIAN_12_IMAGE} AS build
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
COPY gunicorn.conf.py run.py .
COPY api api/
ENTRYPOINT [ "/venv/bin/gunicorn", "run:app" ]
