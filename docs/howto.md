
How to create a tutorial
========================

* create a new repository (pymunk-tutorial)
* create a README file
* select a licence (MIT)
* add ``.gitignore` file (Python)
* add these files to .gitignore
  * .DS_Store
  * .vscode
  * .pytest_cache

* install Sphinx with one of these

```
brew install sphinx-doc
conda install sphinx
```

* create a ``docs`` folder
* set-up the framework for using Sphinx
```
cd docs
sphinx-quickstart
```
* seperate source and build direc