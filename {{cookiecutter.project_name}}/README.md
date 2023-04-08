# {{cookiecutter.project_name}}
* Automated testing on PR using github actions
* Semantic release using github actions

## Install
Cookiecutter template:
* Cd to your new libary location
  * `cd /your/new/library/path/`
* Install cookiecutter using pip
  * `pip install cookiecutter`
* Run the cookiecutter template from this github repo
  * `cookiecutter https://github.com/jonathanvanleeuwen/lib_template`
* Fill in your new library values
* Create new virtual environment
  *  `python -m venv .venv_repo_name`
* Install libary
  *  `pip install -e .`
* Check proper install by running tests
  * `pytest`

# Semantic release
https://python-semantic-release.readthedocs.io/en/latest/

When committing use the following format for your commit message:
* patch:
  `fix: commit message`
* minor:
  `feat: commit message`
* major/breaking (add the breaking change on the third  line of the message):
    ```
    feat: commit message

    BREAKING CHANGE: commit message
    ```


# Protect your main branch
To ensure that only accepted code is put on main, make sure that all changes to main happen using a PR and at least 1
reviewer.
You also want to ensure that no tests are allowed to fail when merging

## Branch Protection
### Ensure branch protection for PRs
In the repo on github go to:
* Settings -> Branches and click "add rule"
* Enable:
  * Require a pull request before merging
    * Require approvals (set the number of required reviewers)
  * Require status checks to pass before merging
    * Require branches to be up to date before merging
  * Require conversation resolution before merging

### Ensure workflow protection
this is not entirely fool proof and secure, but better than nothing, in the repo on github go to:
* Settings -> Actions -> General
* Enable:
  * Allow [owner], and select non-[owner], actions and reusable workflows
* In "Allow specified actions and reusable workflows" add the following string:
  * actions/checkout@v2,
actions/setup-python@v3,
relekang/python-semantic-release@master,

## Create a semantic release PAT and Secrets for the workflow actions
For the semantic release to be able to push new version to the protected branch you need to
create a PAT with the proper permissions and save the pat as a secret in the repo.

### Create PAT
* Click Top right image -> settings
* Developer settings
* Personal access tokens -> Tokens (classic)
* Generate new token -> generate new token (classic)

Settings:
* Note: Semantic release
* Enable:
  * Repo (and all the repo options)
  * workflow
  * admin:repo_hook
* Generate token

Now copy the token (you need this in the next step)

### Create secret
Go to your repo, then:
* Settings -> Secrets -> Actions
* New repository secret
  * Name: SEM_RELEASE
  * Secret: [Your copied PAT token]

The name needs to be the same as this is wat is used in ".github\workflows\semantic-release.yml"


# Coverage report
<!-- Pytest Coverage Comment:Begin -->
<!-- Pytest Coverage Comment:End -->