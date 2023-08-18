SHELL := /bin/bash
image_name = imf-api
image_tag = 1.0.0

init:
	pip install -r requirements.txt
common:
	flake8 api/__init__.py api/app.py
	flake8 tests/test_common.py
	pytest -vvv tests/test_common.py
imf: common
	flake8 api/imf
	flake8 tests/test_imf.py
	pytest -vvv tests/test_imf.py
task: common
	flake8 api/task
	flake8 tests/test_task.py
	pytest -vvv tests/test_task.py
coverage:
	flake8
	coverage run -m pytest -vvv
	coverage report
	coverage html
clean:
	rm -rf __pycache__
	rm -rf .pytest_cache
	rm -rf htmlcov
	rm .coverage
start_dev:
	source ./venv/bin/activate && export FLASK_APP=api.app && export FLASK_ENV=development && flask run
start:
	source ./venv/bin/activate && gunicorn api.app:app
build:
	docker image build -t $(image_name):$(image_tag) .
run:
	docker container run -d --rm -p 9080:9080 --name $(image_name) $(image_name):$(image_tag)
logs:
	docker container logs -f $(image_name)
stop:
	docker container stop $(image_name)
all: init coverage

