# Makefile
.PHONY: test lint check-format format tox clean

PY = py39

help:
	@echo "you need to have tox installed already (I recommend installing it with pipx)"
	@echo "test - install deps and run all tests with $(PY)"
	@echo "lint - run linting"
	@echo "check-format - check formatting"
	@echo "format - run formatting"
	@echo "tox - run all tox actions using existing interpreters"
	@echo "clean - clean project cache"

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

clean:
	@find . -type d -name '__pycache__' | xargs rm -rf
	@find . -type d -name '.pytest_cache' | xargs rm -rf
	@rm .mutmut-cache
