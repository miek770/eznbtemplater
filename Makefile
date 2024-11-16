NAME = $(shell grep '^name =' pyproject.toml | sed -E 's/name = "(.*)"/\1/')
VERSION = $(shell grep '^version =' pyproject.toml | sed -E 's/version = "(.*)"/\1/')

info:
	@echo $(NAME), version $(VERSION)

publish:
	uv run twine upload -r pypi dist/*

tests:
	uv run python -m pytest

.PHONY: info publish tests
