install:
	poetry install

lint:
	poetry run ruff format --check .
	poetry run ruff check .
	poetry run mypy .

test:
	poetry run pytest

up:
	docker compose --env-file .env -f deploy/docker-compose.yml up --build -d

down:
	docker compose -f deploy/docker-compose.yml down
