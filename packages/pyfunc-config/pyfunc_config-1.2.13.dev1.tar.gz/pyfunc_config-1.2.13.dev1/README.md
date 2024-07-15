# [config.pyfunc.com](http://config.pyfunc.com)

## START

setup local environment
```bash
python3 -m venv pytest-env
source pytest-env/bin/activate
```


Install required tools
```bash
pip install setuptools wheel setuptools-git-versioning build twine pip-tools toml path
pip install --upgrade setuptools_scm
pip install --upgrade twine 
pip list
```

## UPDATE

quick update
```bash
git status
git tag 1.2.13
git push origin --tags
git add pyproject.toml
git add .gitignore
git add *.py
git add *.md
git add src/*
git commit -m "new release"
git push
python -m setuptools_git_versioning
rm -rf build dist *.egg-info
python -m build
python -m twine upload dist/*
```

### DETAILS

```bash
git tag 1.2.8
git push origin --tags
```

VERSION
```bash
python -m setuptools_git_versioning
```

update requirements
```bash
pip-compile pyproject.toml
```
```bash
pip-sync
```
### build and publish your package:

Clean
```bash
rm -rf build dist *.egg-info
```


Build the Package with debug
```bash
python -m build --wheel -n
```


Build the Package
```bash
python -m build
```




Publish to PyPI
```bash
python -m twine upload dist/*
```





## Another


Here's an updated GitHub Actions workflow to include the script execution:

```bash
py generate_init.py -p src/pyfunc_config
````

```bash
py -m build
```

```bash
twine check dist/*
```

test before publish
```bash
twine upload -r testpypi dist/*
```

publish
```bash
twine upload dist/* 
```        


## Semantic versioning

The idea of semantic versioning (or SemVer) is to use 3-part version numbers, major.minor.patch, where the project author increments:

    major when they make incompatible API changes,

    minor when they add functionality in a backwards-compatible manner, and

    patch, when they make backwards-compatible bug fixes.


