SHELL := /bin/bash
base = venv/bin
image_name = imf-api
image_tag = 1.0.0
dive = docker run -ti --rm  -v /var/run/docker.sock:/var/run/docker.sock wagoodman/dive
trivy = docker run -ti --rm  -v /var/run/docker.sock:/var/run/docker.sock aquasec/trivy

init:
	$(base)/pip install -r requirements/dev.txt
common:
	$(base)/flake8 api/__init__.py api/app.py
	$(base)/flake8 tests/test_common.py
	$(base)/pytest -vvv tests/test_common.py
imf: common
	$(base)/flake8 api/imf
	$(base)/flake8 tests/test_imf.py
	$(base)/flake8 tests/test_task.py
	$(base)/pytest -vvv tests/test_task.py
coverage:
	$(base)/flake8
	$(base)/coverage run -m pytest -vvv
	$(base)/coverage report
	$(base)/coverage html
clean:
	rm -rf __pycache__/ .pytest_cache/ htmlcov/
	rm .coverage bom.json payload.json > /dev/null 2>&1 || echo ""
start_dev:
	export FLASK_APP=api.app && export FLASK_ENV=development && $(base)/flask run
start:
	$(base)/gunicorn api.app:app
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

