# -*- coding: utf-8 -*-
DESCRIPTION = (
    'pyecharts map extension - china cities - python package' +
    ''
)
extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.doctest',
    'sphinx.ext.intersphinx',
    'sphinx.ext.viewcode',
]

templates_path = ['_templates']
source_suffix = '.rst'
master_doc = 'index'

project = u'echarts-china-cities-pypkg'
copyright = u'2018 pyecharts dev team'
version = '0.0.2'
release = '0.0.2'
exclude_patterns = []
pygments_style = 'sphinx'
html_theme = 'default'
html_static_path = ['_static']
htmlhelp_basename = 'echarts-china-cities-pypkgdoc'
latex_elements = {}
latex_documents = [
    ('index', 'echarts-china-cities-pypkg.tex',
     'echarts-china-cities-pypkg Documentation',
     'pyecharts dev team', 'manual'),
]
man_pages = [
    ('index', 'echarts-china-cities-pypkg',
     'echarts-china-cities-pypkg Documentation',
     [u'pyecharts dev team'], 1)
]
texinfo_documents = [
    ('index', 'echarts-china-cities-pypkg',
     'echarts-china-cities-pypkg Documentation',
     'pyecharts dev team', 'echarts-china-cities-pypkg',
     DESCRIPTION,
     'Miscellaneous'),
]
