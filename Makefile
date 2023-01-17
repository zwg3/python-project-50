install:
	poetry install
build:
	poetry build
publish:
	poetry publish --dry-run
package-install:
	python3 -m pip install --user dist/gendiff-0.1.0-py3-none-any.whl
gen:
	poetry run gendiff
lint:
	poetry run flake8 gendiff
