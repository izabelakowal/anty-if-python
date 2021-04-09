# Makefile
.PHONY: test tox

help:
	@echo "test - run all tests"
	@echo "tox - run tests with tox using existing interpreters"

test:
	tox -e py39

tox:
	tox --skip-missing-interpreters
