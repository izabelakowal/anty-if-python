# Makefile
.PHONY: devenv test lint check-format format tox pre-commit clean clean-mutmut

PY = py39

help:
	@echo "initial setup:"
	@echo "you need to have tox and pre-commit installed already (I recommend installing it with pipx)"
	@echo "devenv - if you still want to install extra deps: tox and pre-commit in venv\n"
	@echo "test - install deps and run all tests with $(PY)"
	@echo "lint - run linting"
	@echo "check-format - check formatting"
	@echo "format - run formatting"
	@echo "tox - run all tox actions using existing interpreters"
	@echo "pre-commit - run all pre-commit hooks"
	@echo "clean - clean project cache"
	@echo "clean-mutmut - clean only mutmut cache"

devenv:
	tox -e devenv

test:
	tox -e $(PY)

lint:
	tox -e lint

check-format:
	tox -e fmt-check

format:
	tox -e fmt

tox:
	tox --skip-missing-interpreters

pre-commit:
	pre-commit install
	pre-commit run --all-files

clean:
	@find . -type d -name '__pycache__' | xargs rm -rf
	@find . -type d -name '.pytest_cache' | xargs rm -rf
	@if [ -f .mutmut-cache ]; then rm .mutmut-cache; fi

clean-mutmut:
	@if [ -f .mutmut-cache ]; then rm .mutmut-cache; fi
