install:
	poetry install

config:
	poetry config virtualenvs.in-project true

lint:
	poetry run flake8

test:
	poetry run coverage run -m pytest

coverage:
	poetry run coverage lcov
