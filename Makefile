NOSE=nosetests

.PHONY: all tests clean list

list:
	-find .

check:
	-pycodestyle 1x1/*.py

venv: venv/bin/activate

venv/bin/activate: requirements.txt
	test -d venv || virtualenv venv
	. venv/bin/activate; pip install -Ur requirements.txt
	touch venv/bin/activate
	printf "\n*** Remember to start your venv, like this '. ./venv/bin/activate'\n*** And then you can 'make develop'\n\n"

develop:
	python setup.py develop

tests: venv
	printf "\n*** Remember to start your venv, like this '. ./venv/bin/activate'\nbefore running tests\n\n"
	${NOSE}

clean:
	rm -rf venv
	find . -iname "*.pyc" -o -iname "*.pyo" -o -iname "*.so" -o -iname "#*#" -delete

all: tests

