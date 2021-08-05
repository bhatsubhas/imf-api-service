init:
	pip install -r requirements/dev.txt
test:
	coverage run -m pytest -vvv
	coverage report
	coverage html
clean:
	rm -rf __pycache__
	rm -rf .pytest_cache
	rm -rf htmlcov
	rm .coverage
all: init test

