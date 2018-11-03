#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'Julien Nuellas'
SITENAME = 'JN-Blog'
SITEURL = ''
SITESUBTITLE = 'JN-Blog'
SITEDESCRIPTION = 'Blog sur le monde informatique et le développement produit.'

PYGMENTS_STYLE = 'monokai'

# THEME = "../JN-PelicanTheme-Minimalist/Responsive-Pelican"

# CSS_FILE = 'style.css'
THEME = "themes/Flex"
PATH = 'content'
STATIC_PATHS = [
    'images',
    'extra/robots.txt',
    'extra/CNAME',
]
EXTRA_PATH_METADATA = {
    'extra/robots.txt': {'path': 'robots.txt'},
    'extra/CNAME': {'path': 'CNAME'},
}

TIMEZONE = 'Europe/Paris'

I18N_TEMPLATES_LANG = 'fr_FR'
DEFAULT_LANG = 'fr_FR'
OG_LOCALE = 'fr_FR'
LOCALE = 'fr_FR'
DEFAULT_LANG = 'fr'

DATE_FORMATS = {
    'fr': '%B %d, %Y',
}

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Category and Tags Settings
USE_FOLDER_AS_CATEGORY = False
DISPLAY_PAGES_ON_MENU = False
DISPLAY_TAGS_ON_MENU = True

MAIN_MENU = False
HOME_HIDE_TAGS = True

# URL Settings

ARTICLE_URL = 'articles/{slug}/'
ARTICLE_SAVE_AS = 'articles/{slug}/index.html'
PAGE_URL = 'pages/{slug}/'
PAGE_SAVE_AS = 'pages/{slug}/index.html'
CATEGORY_URL = 'categorie/{slug}/'
CATEGORY_SAVE_AS = 'categorie/{slug}/index.html'
TAG_URL = 'tag/{slug}/'
TAG_SAVE_AS = 'tag/{slug}/index.html'

CATEGORIES_SAVE_AS = 'categories.html'
TAGS_SAVE_AS = 'tags.html'
INDEX_SAVE_AS = 'index.html'

AUTHOR_URL = 'author/{slug}/'
AUTHOR_SAVE_AS = ''

# ARCHIVES_SAVE_AS = 'archives.html'
# YEAR_ARCHIVES_SAVE_AS = 'articles/{date:%Y}/index.html'
# MONTH_ARCHIVES_SAVE_AS = 'articles/{date:%Y}/{date:%b}/index.html'


# Theme settings for development



# Blogroll
LINKS = (('Pelican', 'http://getpelican.com/'),
         ('Python.org', 'http://python.org/'),
         ('Jinja2', 'http://jinja.pocoo.org/'),)

# Social widget
SOCIAL = (('twitter', 'https://twitter.com/JulienNuellas'),
          ('linkedin', 'https://fr.linkedin.com/in/julien-nuellas'),
          ('github', 'https://github.com/JN-Lab'))

MENUITEMS = (('Archives', '/archives.html'),
             ('Categories', '/categories.html'),
             ('Tags', '/tags.html'),)

CC_LICENSE = {
    'name': 'Creative Commons Attribution-ShareAlike',
    'version': '4.0',
    'slug': 'by-sa'
}

COPYRIGHT_YEAR = 2016

DEFAULT_PAGINATION = 10

PLUGIN_PATHS = ['./pelican-plugins']
PLUGINS = ['sitemap', 'i18n_subsites']

JINJA_ENVIRONMENT = {'extensions': ['jinja2.ext.i18n']}

SITEMAP = {
    'format': 'xml',
    'priorities': {
        'articles': 0.6,
        'indexes': 0.6,
        'pages': 0.5,
    },
    'changefreqs': {
        'articles': 'monthly',
        'indexes': 'daily',
        'pages': 'monthly',
    }
}

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
