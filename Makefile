install: # инсталяция
        poetry install


brain-games: # запуск brain_games.py
        poetry run brain-games


build: # собрать какой то пакет
        poerty build


publish: # публикация
        poetry publish --dry-run


package-install: # инсталяция чего то
        python3 -m pip install --user dist/*.whl


lint: # запуск линтера
        poetry run flake8 brain_games


brain-calc:
        poetry run brain-calc


brain-gcd:
        poetry run brain-gcd


brain-progression:
        poetry run brain-progression
