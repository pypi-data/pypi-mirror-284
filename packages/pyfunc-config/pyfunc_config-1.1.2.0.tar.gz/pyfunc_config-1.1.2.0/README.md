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

```bash
git tag 1.2.1
git push origin --tags
```

VERSION
```bash
python -m setuptools_git_versioning
```

update requirements
```bash
pip-compile pyproject.toml
pip-sync
```

### build and publish your package:

Clean
```bash
rm -rf build dist *.egg-info
```


Build the Package
```bash
python -m build --sdist --wheel -n
```



Publish to PyPI
```bash
python -m twine upload dist/*
```




Here's an updated GitHub Actions workflow to include the script execution:

```bash
py generate_init.py -p src/pyfunc-config
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


