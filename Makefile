install:
	poetry install
brain-games:
	poetry run brain-games
brain-even:
	poetry run brain-even
brain-calc:
	poetry run brain-calc
build:
	poetry build
publish:
	poetry publish --dry-run
package-install:
	pipx install dist/*.whl --force
lint:
	poetry run flake8 brain_games
