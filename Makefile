PACKAGE := chess

coverage:
	pytest --cov=$(PACKAGE) --cov-report=term-missing --cov-fail-under=100 tests
.PHONY: coverage

pyenv:
	virtualenv -p python3 pyenv
	pyenv/bin/pip install -r requirements.txt
.PHONY: pyenv

test:
	pytest -xv tests
.PHONY: test

flake8:
	flake8 $(PACKAGE) tests
.PHONY: flake8

freeze:
	pyenv/bin/pip freeze | egrep -v "$(PACKAGE)|flake8|pylint|pytest|pkg-resources" > requirements.txt
.PHONY: freeze

pylint: pylint_pkg pylint_examp pylint_tests pylint_examples
.PHONY: pylint
