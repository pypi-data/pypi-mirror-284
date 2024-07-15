# [lib](http://lib.pyfunc.com)

libs for cameramonit, ocr, fin-officer, cfo, and other projects



## Install

```bash
git clone https://github.com/pyfunc/lib.git pyfunc
```


## Contributing

```bash
python3 -m venv pytest-env
source pytest-env/bin/activate
```

```bash
pip install --upgrade pip
pip install pytest
```

run the test, execute the pytest command:
```bash
pytest
```



## Tips

simple method to generate a requirements.txt file is to pipe them,
```bash
pip freeze > requirements.txt
```

## if push not possible

```
[remote rejected] (refusing to allow a Personal Access Token to create or update workflow `.github/workflows/python-app.yml` without `workflow` scope)
```

Problem z odrzuceniem tokena dostępu osobistego (Personal Access Token, PAT) podczas próby aktualizacji pliku workflow, 
musisz zaktualizować uprawnienia swojego tokena. 

### Oto kroki, które powinieneś podjąć:

1. Przejdź do ustawień GitHub:
   - Kliknij na swój awatar w prawym górnym rogu GitHub
   - Wybierz "Settings"

2. Przejdź do ustawień deweloperskich:
   - W lewym menu wybierz "Developer settings"

3. Zarządzaj tokenami dostępu:
   - Wybierz "Personal access tokens"
   - Następnie "Tokens (classic)"

4. Utwórz nowy token lub zaktualizuj istniejący:
   - Jeśli tworzysz nowy, kliknij "Generate new token"
   - Jeśli aktualizujesz istniejący, znajdź odpowiedni token i kliknij "Edit"

5. Dodaj uprawnienie "workflow":
   - Przewiń do sekcji "Select scopes"
   - Zaznacz pole obok "workflow"

6. Zapisz zmiany:
   - Przewiń na dół i kliknij "Generate token" (dla nowego) lub "Update token" (dla istniejącego)

7. Skopiuj nowy token:
   - Upewnij się, że skopiowałeś nowy token, ponieważ nie będziesz mógł go zobaczyć ponownie

8. Zaktualizuj token w swoim lokalnym repozytorium:
   - Jeśli używasz HTTPS, zaktualizuj swoje dane logowania
   - Jeśli używasz SSH, upewnij się, że Twój klucz SSH jest poprawnie skonfigurowany

9. Spróbuj ponownie wykonać push:
   - Użyj nowego tokena do autoryzacji

Pamiętaj, że tokeny dostępu osobistego są bardzo wrażliwe na bezpieczeństwo.
Traktuj je jak hasła i nigdy nie udostępniaj ich publicznie. Jeśli przypadkowo ujawnisz swój token, natychmiast go usuń i wygeneruj nowy.

Po wykonaniu tych kroków, powinieneś być w stanie zaktualizować plik workflow bez problemów. Jeśli nadal napotkasz problemy, upewnij się, że masz odpowiednie uprawnienia w repozytorium i że workflow nie są zablokowane przez ustawienia organizacji lub repozytorium.

# update PAT in repo
our local repo and want to push it to a remote repo.

create a PAT (personal access token): official doc here. Make sure to tick the box "workflow" when creating it.
In the terminal, instead of the classic

```bash
git remote add origin https://github.com/<account>/<repo>.git
```

swap it by
```bash
git remote add origin https://<PAT>@github.com/<account>/<repo>.git
```
example
```bash
# check
git remote -v
PAT=...
git remote add origin https://$PAT@github.com/pyfunc/lib.git
# OR update:
git remote set-url origin https://$PAT@github.com/pyfunc/lib.git
# check
git remote -v
git push
```

Follow-up with the classic git branch -M main and git push -u origin main

That worked for me. Hopefully for you too.

## pypi publishing

[Creating a PyPI Project with a Trusted Publisher - PyPI Docs](https://docs.pypi.org/trusted-publishers/creating-a-project-through-oidc/)




The issue you're facing is due to the way directories are specified for inclusion in the build process. In your case, it seems the package is being loaded from the `src` directory, while it should be set up to load from the main project directory.

Let's correct your `pyproject.toml` and ensure that the package structure and build configuration match your desired setup.

### Correction in `pyproject.toml`

If your main source code is stored in a directory like `src` and your package name is `pyfunc2`, you need to specify the package correctly so that it gets included properly in the wheel. Here’s a corrected version of your `pyproject.toml`:

```toml
[build-system]
requires = [
    "hatch-vcs>=0.4",
    "hatchling>=1.18",
    "hatch-requirements-txt",
    "setuptools ~=63.2.0",
    "wheel ~=0.37.1",
]
build-backend = "hatchling.build"

[project.urls]
homepage = "https://www.pyfunc.com"
repository = "https://github.com/pyfunc/lib"
changelog = "https://github.com/pyfunc/lib/releases"
wiki = "https://github.com/pyfunc/lib/wiki"
issue = "https://github.com/pyfunc/lib/issues/new"

[project]
name = "pyfunc2"
version = "0.1.8"
description = "libs for cameramonit, ocr, fin-officer, cfo, and other projects"
readme = "README.md"
readme.content-type = "text/markdown"
keywords = ["test", "framework", "cameramonit", "fin-officer", "console", "terminal", "time"]
license = "Apache-2.0"
requires-python = ">=3.7"
dependencies = [
    "packaging>=23.2",
    "tomli>=2.0.1",
    "stringcase ~=1.2.0",
]
optional-dependencies.docs = [
    "furo>=2023.9.10",
    "sphinx<7.2",
    "sphinx-autodoc-typehints>=1.25.2",
    "pylint ~=2.14.0",
    "toml ~=0.10.2",
    "yapf ~=0.32.0",
]
optional-dependencies.testing = [
    "covdefaults>=2.3",
    "pytest>=7.4.3",
    "pytest-cov>=4.1",
    "pytest-mock>=3.12",
    "setuptools>=69.0.2",
    "wheel>=0.42",
]
authors = [
    { name = "Tom Sapletta", email = "tom@sapletta.com" },
]
maintainers = [
    { name = "pyfunc developers", email = "info@softreck.dev" }
]

classifiers = [
    "Development Status :: 5 - Production/Stable",
    "Environment :: Console",
    "Environment :: MacOS X",
    "Environment :: Other Environment",
    "Environment :: Win32 (MS Windows)",
    "Environment :: X11 Applications",
    "Framework :: IPython",
    "Framework :: Jupyter",
    "Intended Audience :: Developers",
    "Intended Audience :: Education",
    "Intended Audience :: End Users/Desktop",
    "Intended Audience :: Other Audience",
    "Intended Audience :: System Administrators",
    "License :: OSI Approved :: Apache Software License",
    "Operating System :: MacOS",
    "Operating System :: MacOS :: MacOS X",
    "Operating System :: Microsoft",
    "Operating System :: Microsoft :: MS-DOS",
    "Operating System :: Microsoft :: Windows",
    "Operating System :: POSIX",
    "Operating System :: POSIX :: BSD",
    "Operating System :: POSIX :: BSD :: FreeBSD",
    "Operating System :: POSIX :: Linux",
    "Operating System :: POSIX :: SunOS/Solaris",
    "Operating System :: Unix",
    "Programming Language :: Python",
    "Programming Language :: Python :: 3",
    "Programming Language :: Python :: 3.7",
    "Programming Language :: Python :: 3.8",
    "Programming Language :: Python :: 3.9",
    "Programming Language :: Python :: 3.10",
    "Programming Language :: Python :: 3.11",
    "Programming Language :: Python :: 3 :: Only",
    "Programming Language :: Python :: Implementation",
    "Programming Language :: Python :: Implementation :: IronPython",
    "Programming Language :: Python :: Implementation :: PyPy",
    "Programming Language :: Unix Shell",
    "Topic :: Desktop Environment",
    "Topic :: Education :: Computer Aided Instruction (CAI)",
    "Topic :: Education :: Testing",
    "Topic :: Office/Business",
    "Topic :: Other/Nonlisted Topic",
    "Topic :: Software Development :: Build Tools",
    "Topic :: Software Development :: Libraries",
    "Topic :: Software Development :: Libraries :: Python Modules",
    "Topic :: Software Development :: Pre-processors",
    "Topic :: Software Development :: User Interfaces",
    "Topic :: System :: Installation/Setup",
    "Topic :: System :: Logging",
    "Topic :: System :: Monitoring",
    "Topic :: System :: Shells",
    "Topic :: Terminals",
    "Topic :: Utilities"
]

[tool.hatch.metadata.hooks.requirements_txt]
#files = ["requirements.txt"]

[tool.pylint]
max-line-length = 88
disable = [
    "C0103",  # (invalid-name)
    "C0113",  # (missing-module-docstring)
    "C0114",  # (missing-class-docstring)
    "C0115",  # (missing-function-docstring)
    "R0903",  # (too-few-public-methods)
    "R0913",  # (too-many-arguments)
    "W0105",  # (pointless-string-statement)
]

[tool.flake8]
max_line_length = 99
exclude = [
    ".git",
    "__pycache__",
    "build",
    "dist",
    ".eggs",
    ".asv",
    ".tox",
    ".ipynb_checkpoints"
]

[tool.yapf]
spaces_before_comment = [15, 20]
arithmetic_precedence_indication = true
allow_split_before_dict_value = false
coalesce_brackets = true
column_limit = 99
each_dict_entry_on_separate_line = false
space_between_ending_comma_and_closing_bracket = false
split_before_named_assigns = false
split_before_closing_bracket = false
blank_line_before_nested_class_or_def = false

[tool.isort]
line_length = 99
multi_line_output = 4
known_first_party = ["src", "tests"]

[tool.coverage.run]
source = ["src"]

[tool.coverage.report]
show_missing = true

[tool.coverage.html]
show_contexts = true
skip_covered = false

[tool.coverage.paths]
source = [
    "src",
    ".tox*/*/lib/python*/site-packages",
    ".tox*/pypy*/site-packages",
    ".tox*\\*\\Lib\\site-packages",
    "*/src",
    "*\\src"
]

[tool.black]
line-length = 120

[tool.ruff]
src = ["src", "tests"]

[tool.ruff.isort]
known-first-party = ["pyproject_hooks", "tests"]

[tool.mypy]
python_version = "3.11"
show_error_codes = true
strict = true
overrides = [
    { module = ["virtualenv.*"], ignore_missing_imports = true }
]

[tool.hatch.version]
path = "src/__init__.py"

[tool.setuptools.dynamic]
version = { attr = "my_package.VERSION" }
readme = { file = ["README.md", "TODO.md"] }

[tool.setuptools_scm]

[tool.hatch.build.targets.wheel]
packages = ["pyfunc2"]
```

### Explanation of Key Sections:
- **`[build-system]`**: Specifies build dependencies and sets `hatchling` as the build backend.
- **`[project]`**: Contains metadata about your project, like the name, version, description, etc.
- **`[tool.hatch.build.targets.wheel]`**: Lists the packages to be included in the wheel. Here, replacing `["src"]` with `["pyfunc2"]` makes sure it points to your actual package directory.

### Project Structure:
Make sure your project structure follows this layout:
```
my_project/
├── src/
│   └── pyfunc2/
│       ├── __init__.py
│       └── other_module.py
├── pyproject.toml
├── README.md
└── setup.py (if using for additional setup configuration)
```

### Ensure Correct Setup:
1. **Source Directory**: The `src` directory should contain your package directory (`pyfunc2`).
2. **Build System**: The build system in `pyproject.toml` must properly reflect where the source code resides and should not mistakenly package the entire `src` directory unless intended.

### Final Steps:
1. **Verify Local Build**:
Before pushing changes, verify the build process locally.

```bash
pip install -r requirements.txt
python -m build
```

2. **Push Changes**:
Ensure everything is committed and pushed to the repository.

```bash
git add pyproject.toml README.md setup.py (if exists)
git commit -m "Fix project structure and build configuration"
git push origin main
```

3. **Update GitHub Actions Workflow**:
Use the updated workflow to build and publish the package.

```yaml
name: Publish Python Package

on:
  push:
    branches:
      - "main"
  pull_request:
    branches:
      - "main"
  release:
    types: [published]

permissions:
  contents: read
  id-token: write

jobs:
  build:
    runs-on: ubuntu-latest

    steps:
      - uses: actions/checkout@v3

      - name: Set up Python
        uses: actions/setup-python@v3
        with:
          python-version: '3.x'

      - name: Install dependencies
        run: |
          python -m pip install --upgrade pip
          pip install flake8 pytest

          if [ -f requirements.txt ]; then
            pip install -r requirements.txt
          fi

      - name: Lint with flake8
        run: |
          # Stop the build if there are Python syntax errors or undefined names
          flake8 . --count --select=E9,F63,F7,F82 --show-source --statistics
          # Exit-zero treats all errors as warnings. The GitHub editor is 127 chars wide
          flake8 . --count --exit-zero --max-complexity=10 --max-line-length=127 --statistics

      - name: Test with pytest
        run: pytest

  publish:
    needs: build
    runs-on: ubuntu-latest

    steps:
      - uses: actions/checkout@v3

      - name: Set up Python
        uses: actions/setup-python@v3
        with:
          python-version: '3.x'

      - name: Install dependencies
        run: |
          python -m pip install --upgrade pip
          pip install build

      - name: Build package
        run: python -m build

      - name: Publish package to PyPI
        uses: pypa/gh-action-pypi-publish@release/v1
        with:
          user: __token__
          password: ${{ secrets.PYPI_API_TOKEN }}
```

This setup should address the structural issues and configuration errors, ensuring that your package is built correctly and published to PyPI without ending up in the wrong folder path.