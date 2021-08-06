init:
	pip install -r requirements/dev.txt
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
all: init coverage

