## Description
* Add PYPI_USERNAME and PYPI_PASSWORD to `Secrets and variables > Actions > Secrets` using GitHub GUI. This is required to push your package to PyPI.
* Run `customize.py` to take care of the rest.
* Each time you push a new release, code is automatically published on PyPI via the workflow. `pip install -U <your_package>` should then install the latest version of your package.

## How to add badges?
### CI status badge
![image](https://github.com/patel-zeel/pip-template/assets/59758528/5e2bf572-08a9-4d96-86ea-946e89686870)

### Coverage badge
![image](https://github.com/patel-zeel/pip-template/assets/59758528/c924ffc5-7974-4a6a-a225-1c6de96dd826)


