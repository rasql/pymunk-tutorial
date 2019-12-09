
How to create a tutorial
========================

Create GitHub repository
------------------------

* create a new repository (pymunk-tutorial)
* create a README file
* select a licence (MIT)
* add ``.gitignore` file (Python)
* add these files to .gitignore
  * .DS_Store
  * .vscode
  * .pytest_cache

Create Sphinx documentation
---------------------------

* install Sphinx with one of these

```zsh
brew install sphinx-doc
conda install sphinx
```

* create a ``docs`` folder
* set-up the framework for using Sphinx

```zsh
cd docs
sphinx-quickstart
```

* Add project title, author, release
* in ``conf.py`` add

```zsh
html_theme = 'sphinx_rtd_theme'
```

* in ``index.rst`` add

```bash
intro/intro.rst
```

* run ``make html``

Connect to Read the Docs
------------------------

* connect with GitHub account
* import the project
* add this to conf.py

```
master_doc = 'index'
```