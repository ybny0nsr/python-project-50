install:	 # Первое клонирование репозитория или восстановление зависимостей
	poetry install

setup: 	build publish package-install  # сборка + публикация + установка пакета

bulld:		# Сборка пакета
	poetry build

publish:	 # Публикация пакета
	poetry publish --dry-run

package-install: # Установка пакета в окружение пользователя
	python3 -m pip install --user --force-reinstall dist/*.whl

test-coverage:
	poetry run pytest --cov=hexlet_code --cov-report xml

lint:		# Линтер
	poetry run flake8 hexlet_code

test:
	poetry run pytest

tests:          # pytest с выводом программы
	poetry run pytest -s

selfcheck:
	poetry check

check: selfcheck test lint

buildc: check
	poetry build

.PHONY: install test lint selfcheck check build
