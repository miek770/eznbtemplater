NAME = $(shell grep '^name =' pyproject.toml | sed -E 's/name = "(.*)"/\1/')
VERSION = $(shell grep '^version =' pyproject.toml | sed -E 's/version = "(.*)"/\1/')

info:
	@echo $(NAME), version $(VERSION)

tests:
	uv run python -m pytest

.PHONY: info tests
