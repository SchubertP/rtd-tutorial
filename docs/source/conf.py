# Configuration file for the Sphinx documentation builder.

import sys
import os

# -- Project information

project = 'Lumache'
copyright = '2021, Graziella'
author = 'Graziellax'

release = '0.2.2'
version = '0.2.2'

# patch the Sphinx run to directly run from the sources
sys.path.insert(0, os.path.abspath('../..'))

# -- General configuration

extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.autosummary',
    'sphinx.ext.mathjax',
    'nbsphinx',
]

#mathjax_path = "https://cdn.mathjax.org/mathjax/latest/MathJax.js?config=TeX-AMS-MML_HTMLorMML"

# -- Options for HTML output

html_theme = 'alabaster'

# -- Options for EPUB output
epub_show_urls = 'footnote'


# -- Options for LaTeX output --------------------------------------------------

# Grouping the document tree into LaTeX files. List of tuples
# (source start file, target name, title, author, documentclass [howto/manual]).
# latex_documents = [('index', 'lumache.tex', u'Lumache Documentation', 'Peter Schubert', 'manual')]

# Additional stuff for the LaTeX preamble.
latex_elements = {}
latex_elements['preamble'] = r"\usepackage{amsmath}\usepackage{amsfonts}\usepackage{bm}\usepackage{morefloats}"

# latex_show_urls = 'footnote'
