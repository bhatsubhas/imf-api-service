SHELL := /bin/bash
base = venv/bin
image_name = imf-api
image_tag = 1.0.0
dive = docker run -ti --rm  -v /var/run/docker.sock:/var/run/docker.sock wagoodman/dive
trivy = docker run -ti --rm  -v /var/run/docker.sock:/var/run/docker.sock aquasec/trivy

init:
	$(base)/pip install -r requirements/dev.txt
lint:
	$(base)/flake8
test:lint
	$(base)/pytest -vvv
coverage:lint
	$(base)/coverage run -m pytest -vvv
	$(base)/coverage report
report: coverage
	$(base)/coverage html
clean:
	rm -rf htmlcov/ .pytest_cache/ .coverage bom.json payload.json 2>/dev/null || true
	find . -name '__pycache__' -exec rm -rf {} +
	find . -name '*.pyc' -exec rm -f {} +
	find . -name '*.pyo' -exec rm -f {} +
start_dev:
	$(base)/flask --app api run --debug
start:
	$(base)/gunicorn run:app
build:
	docker image build -t $(image_name):$(image_tag) .
analyze:
	$(dive) $(image_name):$(image_tag)
scan:
	$(trivy) image --exit-code 1 --severity CRITICAL,HIGH $(image_name):$(image_tag)
run:
	docker container run -d --rm -p 9080:9080 --name $(image_name) $(image_name):$(image_tag)
push_sbom:
	./push_sbom.sh
logs:
	docker container logs -f $(image_name)
stop:
	docker container stop $(image_name)
all: init coverage

