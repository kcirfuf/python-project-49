install:
	poetry install

build:
	poetry build

package-install:
	python3 -m pip install --user dist/*.whl

publish:
	poetry publish --dry-run

brain-games:
	poetry run brain-games