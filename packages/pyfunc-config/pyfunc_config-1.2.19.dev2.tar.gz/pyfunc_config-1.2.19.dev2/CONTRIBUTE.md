Publishing a package to PyPI directly from the terminal can be easily accomplished using `twine`, a utility specifically designed for uploading Python packages. Here’s a step-by-step guide to help you publish your package to PyPI:

### Step 1: Prepare Your Package
Ensure you have a `setup.py` or `pyproject.toml` file in your project directory. Here’s an example of a basic `setup.py`:

```python

```

### Step 2: Build Your Package
Use `setuptools` and `wheel` to build your package. If not installed, first install them:

```bash
pip install setuptools wheel
```

Then, build your package:

```bash
python setup.py sdist bdist_wheel
```

For `pyproject.toml` based projects, ensure you are using the right build system:

```toml
[build-system]
requires = ["setuptools>=42", "wheel"]
build-backend = "setuptools.build_meta"
```

Then, run:
```bash
python -m build
```

This will generate distribution archives of your package (e.g., `.tar.gz` and `.whl`) inside the `dist/` directory.

### Step 3: Install and Configure `twine`
Install `twine`:

```bash
pip install twine
```

If you don’t have a `.pypirc` file (PyPI configuration file), you can create it in your home directory (`~/.pypirc`). Here’s an example configuration:

```ini
[pypi]
  username = __token__
  password = pypi-<your-generated-token>
```

Generate a token by visiting the following URL and creating it under "API tokens":
[PyPI – API tokens](https://pypi.org/manage/account/token/)

### Step 4: Upload Your Package to PyPI
Use `twine` to upload your dist archives to PyPI:

```bash
twine upload dist/*
```

This command will prompt you for your PyPI username and password unless they are configured in the `.pypirc` file.

### Step 5: Verify Your Package on PyPI
Visit [PyPI](https://pypi.org/) and verify that your package appears and is downloadable.

### Example Process
Here’s a complete script that you can run in your terminal to automate the process:

```bash
#!/bin/bash

# Ensure you’re in the project directory
cd /path/to/your/project

# Optionally clean previous builds
rm -rf build dist *.egg-info

# Install required tools
pip install setuptools wheel build twine

# Build the package
python -m build

# Upload the package to PyPI
twine upload dist/*

# Successful upload message
echo "Package successfully uploaded to PyPI"
```

### Security Note:
- Always secure your API tokens. 
- Do not commit API tokens or credentials to version control systems like Git.
- Consider using environment variables for credentials in CI/CD pipelines.

By following these steps, you can smoothly publish your Python package to PyPI directly from your terminal. This method ensures that your package is built and uploaded efficiently, making it available for others to easily install.



To use `setuptools-git-versioning` for managing version numbers directly from Git tags in a semantic versioning format (major.minor.patch), you need to update your `pyproject.toml` with the correct configuration. This allows you to automatically generate version numbers based on your Git tags during the build process.

First, ensure you have `setuptools-git-versioning` installed:
```bash
pip install setuptools-git-versioning
```

Here's an example `pyproject.toml` configuration with a clean structure that uses `setuptools-git-versioning` to manage versioning:

### Example pyproject.toml

```toml
[build-system]
requires = ["setuptools>=42", "wheel", "setuptools-git-versioning"]
build-backend = "setuptools.build_meta"

[project]
name = "your-package-name"
description = "A brief description of your package"
requires-python = ">=3.6"
dependencies = [
    # List your dependencies here
]

[tool.setuptools.package-data]
your_package_name = ["data/*.dat"]

[tool.setuptools-git-versioning]
enabled = true
# Prefix can be used if you have a pattern like "v1.2.3" for tags
version-format = "{tag}"
unreleased-version = "0.0.0"
starting-version = "0.1.0"
tag-refs = true

[project.urls]
homepage = "https://your-homepage.com"
repository = "https://github.com/yourusername/your-repo"
changelog = "https://github.com/yourusername/your-repo/releases"
documentation = "https://your-documentation-url.com"

[project.authors]
# Add your authors here
authors = [
    { name = "Your Name", email = "your-email@example.com" },
]

[project.maintainers]
maintainers = [
    { name = "Your Maintainer Name", email = "maintainer-email@example.com" }
]

[project.classifiers]
# Add Trove classifiers for your project
classifiers = [
    "Development Status :: 5 - Production/Stable",
    "Intended Audience :: Developers",
    "License :: OSI Approved :: MIT License",
    "Programming Language :: Python :: 3",
    "Programming Language :: Python :: 3.7",
    "Programming Language :: Python :: 3.8",
    "Programming Language :: Python :: 3.9",
    "Programming Language :: Python :: 3.10",
    "Programming Language :: Python :: 3.11",
]
```

### Explanation:

1. **[build-system]**:
   - `requires` includes `setuptools-git-versioning`, `setuptools`, and `wheel`.
   - `build-backend` is set to `setuptools.build_meta`.

2. **[project]**:
   - Basic metadata for the project, including name, description, Python version requirement, and dependencies.

3. **[tool.setuptools.package-data]**:
   - Specifies additional package data to include.

4. **[tool.setuptools-git-versioning]**:
   - `enabled`: Enables the plugin.
   - `version-format`: Defines the version format, set to `{tag}` to use the Git tag as the version.
   - `unreleased-version`: Default version when no tag is found.
   - `starting-version`: Defines the starting version.
   - `tag-refs`: If set to true, it adds Git ref tags.

5. **[project.urls]**:
   - Provides URLs related to the project.

6. **[project.authors] & [project.maintainers]**:
   - Lists authors and maintainers information.

7. **[project.classifiers]**:
   - Provides Trove classifiers for your project.

### Setting Up Git Tags

Ensure that your Git repository uses semantic versioning tags:
```bash
git tag v1.0.0
git tag v1.1.0
git push origin v1.0.0
git push origin v1.1.0
```

Or, if you prefer using lightweight tags without a `v` prefix:
```bash
git tag 1.0.0
git tag 1.1.0
git push origin 1.0.0
git push origin 1.1.0
```

### Building and Publishing

Once configured, the version will be determined by the latest Git tag during the build process. Use the following commands to build and publish your package:

1. **Build the Package**:
```bash
python -m build
```

2. **Publish to PyPI**:
```bash
python -m pip install --upgrade twine
twine upload dist/*
```

Following this setup ensures that your package version is accurately managed by your Git tags, following a consistent semantic versioning pattern, and automates the version management during the build process.






The error `No module named setuptools_git_versioning` suggests that `setuptools-git-versioning` has not been correctly installed or is not being recognized in your current environment.

Let's ensure that `setuptools-git-versioning` is installed correctly and integrated into your build process.

### Step 1: Ensure Installation
First, verify and install `setuptools-git-versioning`:

```bash
pip install setuptools-git-versioning
```

You can also add it directly into your project’s dependencies:

```bash
pip install setuptools>=42 wheel setuptools-git-versioning
```

### Step 2: Check Installation
Verify that `setuptools-git-versioning` is installed by listing your installed packages:

```bash
pip list
```

Ensure you see `setuptools-git-versioning` in the list of installed packages.

### Step 3: Update pyproject.toml
Ensure your `pyproject.toml` is correctly configured. Here is a complete and corrected configuration as per the latest practices:

```toml
[build-system]
requires = ["setuptools>=42", "wheel", "setuptools-git-versioning"]
build-backend = "setuptools.build_meta"

[project]
name = "your-package-name"
description = "A brief description of your package"
requires-python = ">=3.6"
dependencies = [
    "example-dependency>=1.0.0",
    # List your dependencies here
]

[tool.setuptools.package-data]
your_package_name = ["data/*.dat"]

[tool.setuptools-git-versioning]
enabled = true
template = "{tag}"
unreleased-version = "0.0.0"

[project.urls]
homepage = "https://your-homepage.com"
repository = "https://github.com/yourusername/your-repo"
changelog = "https://github.com/yourusername/your-repo/releases"
documentation = "https://your-documentation-url.com"

[project.authors]
authors = [
    { name = "Your Name", email = "your-email@example.com" },
]

[project.maintainers]
maintainers = [
    { name = "Your Maintainer Name", email = "maintainer-email@example.com" }
]

[project.classifiers]
classifiers = [
    "Development Status :: 5 - Production/Stable",
    "Intended Audience :: Developers",
    "License :: OSI Approved :: MIT License",
    "Programming Language :: Python :: 3",
    "Programming Language :: Python :: 3.7",
    "Programming Language :: Python :: 3.8",
    "Programming Language :: Python :: 3.9",
    "Programming Language :: Python :: 3.10",
    "Programming Language :: Python :: 3.11",
]
```

### Step 4: Integrate with Git
Ensure that your Git tags follow a semantic versioning format:

```bash
git tag 1.0.0
git tag 1.1.0
git push origin --tags
```

### Step 5: Build and Upload

1. **Build the Package**:
   Ensure you are in the root directory of your project and then run:

   ```bash
   python -m build
   ```

2. **Upload to PyPI**:
   If you have not installed Twine, install it using:

   ```bash
   pip install twine
   ```

   Then upload your package:

   ```bash
   twine upload dist/*
   ```

### Example Workflow

For a complete and automated workflow, consider the following bash script to build and publish your package:

```bash
#!/bin/bash

# Ensure you are in the project’s root directory
cd /path/to/your/project

# Optional: Clean previous builds
rm -rf build dist *.egg-info

# Install required tools
pip install --upgrade setuptools wheel setuptools-git-versioning build twine

# Ensure setuptools-git-versioning is installed and recognized
python -m pip show setuptools-git-versioning

# Build the package
python -m build

# Upload the package to PyPI
twine upload dist/*

# Successful upload message
echo "Package successfully uploaded to PyPI"
```

### Troubleshooting Tips
- Make sure no conflicting Python versions or environments are being used.
- Verify that your `pyproject.toml` file is in the correct format and includes all necessary configurations.
- Ensure that Git tags follow a proper semantic versioning pattern and are pushed to the remote repository.

By following this setup and ensuring that all dependencies are correctly installed, you should be able to use `setuptools-git-versioning` and avoid errors related to module not found or conflicting configurations.





## dirty


Gdy widzisz "dirty" w wersji twojego projektu, oznacza to, że w twoim repozytorium Git są niezatwierdzone zmiany (uncommitted changes). Oto kilka powodów, dlaczego to może się zdarzyć i jak to naprawić:

1. Niezatwierdzone zmiany:
   - Masz zmodyfikowane pliki, które nie zostały jeszcze dodane do staging area lub zatwierdzone.
   - Rozwiązanie: Zatwierdź wszystkie zmiany lub cofnij je.
     ```
     git add .
     git commit -m "Commit message"
     ```

2. Nieśledzone pliki:
   - Masz nowe pliki, które nie są śledzone przez Git.
   - Rozwiązanie: Dodaj te pliki do repozytorium lub dodaj je do .gitignore.
     ```
     git add .
     git commit -m "Add new files"
     ```
   - Lub dodaj do .gitignore, jeśli nie chcesz ich śledzić.

3. Pliki w .gitignore:
   - Upewnij się, że wszystkie pliki, które nie powinny być śledzone (np. pliki tymczasowe, katalogi build), są w .gitignore.

4. Sprawdź status repozytorium:
   - Użyj `git status`, aby zobaczyć, które pliki są zmodyfikowane lub nieśledzone.

5. Problemy z końcem linii:
   - Czasami różnice w końcach linii między systemami mogą powodować oznaczenie jako "dirty".
   - Rozwiązanie: Skonfiguruj Git do konsekwentnego traktowania końców linii.
     ```
     git config --global core.autocrlf input
     ```

6. Problemy z uprawnieniami plików:
   - Zmiany w uprawnieniach plików mogą być traktowane jako modyfikacje.
   - Rozwiązanie: Użyj `git config core.fileMode false`, jeśli nie chcesz śledzić zmian uprawnień.

7. Podmoduły Git:
   - Jeśli używasz podmodułów, upewnij się, że są one w prawidłowym stanie.

8. Konfiguracja narzędzia wersjonowania:
   - Sprawdź, czy twoja konfiguracja w `pyproject.toml` lub `setup.py` nie wymusza dodawania "dirty" do wersji.

Aby rozwiązać problem:
1. Wykonaj `git status`, aby zobaczyć, co jest niezatwierdzone.
2. Zatwierdź, cofnij lub zignoruj zmiany według potrzeb.
3. Jeśli wszystko jest czyste, a nadal widzisz "dirty", sprawdź konfigurację narzędzia wersjonowania.

Pamiętaj, że "dirty" w wersji nie jest samo w sobie błędem - to informacja, że twoje lokalne repozytorium ma niezatwierdzone zmiany. Jeśli chcesz mieć "czystą" wersję, upewnij się, że wszystkie zmiany są zatwierdzone przed budowaniem pakietu.