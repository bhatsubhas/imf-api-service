FROM debian:11-slim AS build
RUN apt-get update && \
    apt-get install --no-install-suggests --no-install-recommends --yes python3-venv gcc libpython3-dev && \
    python3 -m venv /venv && \
    /venv/bin/pip install --upgrade pip setuptools wheel

FROM build AS build-env
COPY requirements requirements
COPY requirements.txt requirements.txt
RUN /venv/bin/pip install --disable-pip-version-check -r /requirements.txt

FROM gcr.io/distroless/python3-debian11
COPY --from=build-env /venv /venv
WORKDIR /app
COPY gunicorn.conf.py .
COPY api api/
ENTRYPOINT [ "/venv/bin/gunicorn", "api.app:app" ]
