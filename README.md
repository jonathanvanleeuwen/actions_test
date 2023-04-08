# lib_template
Template repo with automated testing and versioning

Assumes you have python and pip installed

## Install
Cookiecutter template:
* Cd to your new library location
  * `cd /your/new/library/path/`
* Install cookiecutter using pip
  * `pip install cookiecutter`
* Run the cookiecutter template from a github repo
  * `cookiecutter https://github.com/jonathanvanleeuwen/lib_template`
* Fill in your new library values
* Create new virtual environment (where you want to save it)
  *  `python -m venv .venv_repo_name`
* Install libary
  *  `pip install -e .`
* Check proper install by running tests (if they exist)
  *  `pytest`
