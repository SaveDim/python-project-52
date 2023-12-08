include .env

MANAGE := poetry run python manage.py

.PHONY: install build run migrations migrate

install:
	poetry install

build:
	poetry build

run:
	python manage.py runserver

migrations:
	$(MANAGE) makemigrations

migrate:
	$(MANAGE) migrate