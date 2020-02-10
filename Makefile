install:
	poetry install

lint:
	poetry run flake8 ./gendiff

publish:
	poetry build
	poetry publish -r test
