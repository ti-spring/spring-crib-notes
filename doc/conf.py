# -*- coding: utf-8 -*-
#
# Configuration file for the Sphinx documentation builder.
#
# This file does only contain a selection of the most common options. For a
# full list see the documentation:
# http://www.sphinx-doc.org/en/master/config

# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
import os
# import sys
# sys.path.insert(0, os.path.abspath('.'))


# -- Project information -----------------------------------------------------

project = u'keel-doc'
author = u'TIS'

# The short X.Y version
version = u''
# The full version, including alpha/beta/rc tags
release = u'1.0.0'


# -- General configuration ---------------------------------------------------

# If your documentation needs a minimal Sphinx version, state it here.
#
# needs_sphinx = '1.0'

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    'sphinx.ext.todo',
    'sphinx.ext.coverage',
    'sphinx.ext.extlinks',
    'sphinx.ext.mathjax',
]

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# The suffix(es) of source filenames.
# You can specify multiple suffix as a list of string:
#
# source_suffix = ['.rst', '.md']
source_suffix = '.rst'

# The master toctree document.
master_doc = 'index'

# The language for content autogenerated by Sphinx. Refer to documentation
# for a list of supported languages.
#
# This is also used if you do content translation via gettext catalogs.
# Usually you set "language" from the command line for these cases.
language = u'ja'

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path .
exclude_patterns = [u'_build', 'Thumbs.db', '.DS_Store']

# The name of the Pygments (syntax highlighting) style to use.
pygments_style = 'none'


# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = 'sphinx_rtd_theme'

# Theme options are theme-specific and customize the look and feel of a theme
# further.  For a list of options available for each theme, see the
# documentation.
#
html_theme_options = {
  'collapse_navigation': False,
  'navigation_depth': 3,
  'prev_next_buttons_location': None
}

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']

# Custom sidebar templates, must be a dictionary that maps document names
# to template names.
#
# The default sidebars (for documents that don't match any pattern) are
# defined by theme itself.  Builtin themes are using these templates by
# default: ``['localtoc.html', 'relations.html', 'sourcelink.html',
# 'searchbox.html']``.
#
# html_sidebars = {}

# Hide "View page source"
html_show_sourcelink = False

# Custom stylesheet
html_style = "css/customize-rtd.css"

# バージョン表記を削除するためタイトルを明示
html_title = project

# -- Options for HTMLHelp output ---------------------------------------------

# Output file base name for HTML help builder.
htmlhelp_basename = 'keel-docdoc'


# -- Options for LaTeX output ------------------------------------------------

latex_elements = {
    # The paper size ('letterpaper' or 'a4paper').
    #
    # 'papersize': 'letterpaper',

    # The font size ('10pt', '11pt' or '12pt').
    #
    # 'pointsize': '10pt',

    # Additional stuff for the LaTeX preamble.
    #
    # 'preamble': '',

    # Latex figure (float) alignment
    #
    # 'figure_align': 'htbp',
}

# Grouping the document tree into LaTeX files. List of tuples
# (source start file, target name, title,
#  author, documentclass [howto, manual, or own class]).
latex_documents = [
    (master_doc, 'keel-doc.tex', u'keel-doc Documentation',
     u'TIS', 'manual'),
]


# -- Options for manual page output ------------------------------------------

# One entry per manual page. List of tuples
# (source start file, name, description, authors, manual section).
man_pages = [
    (master_doc, 'keel-doc', u'keel-doc Documentation',
     [author], 1)
]


# -- Options for Texinfo output ----------------------------------------------

# Grouping the document tree into Texinfo files. List of tuples
# (source start file, target name, title, author,
#  dir menu entry, description, category)
texinfo_documents = [
    (master_doc, 'keel-doc', u'keel-doc Documentation',
     author, 'keel-doc', 'One line description of project.',
     'Miscellaneous'),
]


# -- Options for Epub output -------------------------------------------------

# Bibliographic Dublin Core info.
epub_title = project
epub_author = author
epub_publisher = author

# The unique identifier of the text. This can be a ISBN number
# or the project homepage.
#
# epub_identifier = ''

# A unique identification for the text.
#
# epub_uid = ''

# A list of files that should not be packed into the epub file.
epub_exclude_files = ['search.html']


# -- Extension configuration -------------------------------------------------

# -- Options for todo extension ----------------------------------------------

# If true, `todo` and `todoList` produce output, else they produce nothing.
todo_include_todos = True

branch_name = os.getenv('BRANCH_NAME', 'master')
sample_app_base = 'https://github.com/Fintan-contents/spring-crib-notes/tree/' + branch_name

extlinks = {
  'sample-app': (sample_app_base + '/samples/%s', None),
  'spring-framework-doc': ('https://docs.spring.io/spring-framework/docs/' + '5.3.24' + '/%s', None),
  'spring-boot-doc': ('https://docs.spring.io/spring-boot/docs/' + '2.7.6' + '/%s', None),
  'spring-batch-doc': ('https://docs.spring.io/spring-batch/docs/' + '4.3.7' + '/%s', None),
  'spring-session-doc': ('https://docs.spring.io/spring-session/reference/' + '2.7.0' + '/%s', None),
  'spring-security-doc': ('https://docs.spring.io/spring-security/reference/' + '5.7.5' + '/%s', None),
  'spring-cloud-aws-doc': ('https://docs.awspring.io/spring-cloud-aws/docs/' + '2.4.2' + '/%s', None),
  'macchinetta-server-guideline-thymeleaf-doc': ('https://macchinetta.github.io/server-guideline-thymeleaf/' + '1.8.1.SP1.RELEASE' + '/ja/%s', None),
  'macchinetta-cloud-guideline-doc': ('https://macchinetta.github.io/cloud-guideline/' + '1.2.0.RELEASE' + '/ja/%s', None),
  'macchinetta-batch-guideline-doc': ('https://macchinetta.github.io/batch-guideline/' + '2.3.1.RELEASE' + '/ja/%s', None),
  'thymeleaf-tutorials-doc': ('https://www.thymeleaf.org/doc/tutorials/' + '3.0' + '/%s', None),
  'doma-spring-boot-source': ('https://github.com/domaframework/doma-spring-boot/blob/' + '1.6.0' + '/%s', None),
  'doma-doc': ('https://doma.readthedocs.io/en/' + '2.53.0' + '/%s', None),
  'hibernate-validator-doc': ('https://docs.jboss.org/hibernate/validator/' + '6.2' + '/%s', None),
  'nablarch-doc': ('https://nablarch.github.io/docs/' + '5u21' + '/%s', None)
}

# linkcheck option
linkcheck_timeout = 10
linkcheck_retries = 2