install:	 # Первое клонирование репозитория или восстановление зависимостей
	poetry install

setup: 	build publish package-install  # сборка + публикация + установка пакета

build:		# Сборка пакета
	poetry build

publish:	 # Публикация пакета
	poetry publish --dry-run

package-install: # Установка пакета в окружение пользователя
	python3 -m pip install --user --force-reinstall dist/*.whl

test-coverage:
	poetry run pytest --cov=gendiff --cov-report xml

test-coveragevv:
	poetry run pytest --cov=gendiff

lint:		# Линтер
	poetry run flake8 gendiff

test:
	poetry run pytest

testvv:     # pytest с выводом программы
	poetry run pytest -vv

selfcheck:
	poetry check

check: selfcheck test lint

buildc: check
	poetry build

.PHONY: install test lint selfcheck check build
