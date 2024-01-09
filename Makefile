install:
	poetry install

configure:
	poetry config virtualenvs.in-project true

lint:
	poetry run flake8

test:
	poetry run coverage run -m pytest

cover:
	poetry run coverage lcov
