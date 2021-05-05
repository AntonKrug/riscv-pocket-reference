import os
import sys
from datetime import date
import sphinx_rtd_theme

project = u'RISC-V pocket reference'
release = u'v0.1'
copyright = date.today().strftime("%Y") + u' Anton Krug'
author = u'Anton Krug'

sys.path.insert(0, os.path.abspath('.'))

needs_sphinx = '3.3'

extensions = [
    'sphinx.ext.todo', 'sphinx_tabs.tabs', 'sphinx.ext.graphviz', 
    'myst_parser', 'sphinxcontrib.wavedrom', 'sphinx_copybutton', 'sphinx_rtd_theme' ]

numfig = True
wavedrom_html_jsinline = False
render_using_wavedrompy = False

autosectionlabel_prefix_document = True

sphinx_tabs_valid_builders = ['linkcheck']
templates_path = []
source_suffix = ['.md']
source_encoding = 'utf-8-sig'
master_doc = 'index'

language = None
exclude_patterns = ['Thumbs.db', '.DS_Store']
pygments_style = 'sphinx'
todo_include_todos = False

html_theme = "sphinx_rtd_theme"
html_theme_options = {
    'collapse_navigation': False,
    'sticky_navigation': False,
    'navigation_depth': 3,
    'includehidden': False,
}
html_static_path = ['_static']
html_css_files = ['myOverrides.css']

templates_path = ['_templates']

html_show_sphinx = True
html_show_sourcelink = True
