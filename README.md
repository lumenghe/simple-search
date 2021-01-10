# Simple Search Engine

## Summary

The purpose of this project is to develop a command line text search engine.

It contains the following files and folders:
* simple_search/: core search python code
* tests/:  unit test, integration test
* requirements.txt: all python library need
* CHANGELOG.md
* Dockerfile
* docker-compose.yml
* Makefile
* pylintrc
* README.md
* reports: this folder will be generated automatically by 'make test-unit path=$files_path', it gives unit test reports


## How to build and run code

* `python simple_search/app.py <pathToDirectoryContainingTextFiles>`: to run the project. You can also use docker mode with `make run path=$files_path`

* `make format path=$files_path`: to run black lib on all the code (code formatter)

* `make style path=$files_path`: pylint all the codes folders

* `make test path=$files_path`: to run both unit and integration tests

* `make test-unit path=$files_path`: to run unit tests

* `make test-integration path=$files_path`: to run integration test

* `make down path=$files_path: docker-compose down --volumes`: to remove declared named volumes

## Potential improvements

* Dynamically update the search database when files are added, deleted or modified.

* Define a finer score function using frequency of words in document (a document with 100 times the word 'good' should be returned with higher score than a document with just one occurence)

* Use redis if we would like to scale docker

* Add Cache if necessary, need to maintain consistency between caches and the source of truth

* Think about database (NoSQL or SQL) if we would like to store data not in-memory representation to avoid failure (i.e. power supply shutdown)

* Authentification for database

