# Makefile
.PHONY: test

help:
	@echo "test - run all tests"

test:
	pytest tests
