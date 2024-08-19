#! /bin/bash

# Bootstrap Sphinx
sphinx-quickstart --sep -p "startrepo" -a "FOO" -r "BAR" -l "en" \
    --ext-autodoc --no-makefile --no-batchfile;

# Copy over the intended copy of conf.py
cp source/conf_correct.py source/conf.py;

# Generate Sphinx documentation
sphinx-apidoc -o source/ ../startrepo/;

# Add "modules" and "Indices and tables" section
cat << "EOF" >> source/index.rst
   modules

Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
EOF

# Generate Sphinx HTML documentation
sphinx-build -W --keep-going -b html source/ build/html/;
