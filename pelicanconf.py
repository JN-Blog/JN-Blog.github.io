#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'Julien Nuellas'
SITENAME = 'JN-Blog'
SITEURL = ''

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

DEFAULT_LANG = 'fr'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Category Settings
DEFAULT_CATEGORY = 'home'
USE_FOLDER_AS_CATEGORY = True
DISPLAY_CATEGORIES_ON_MENU = True

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


# Theme settings
# THEME = "themes/Responsive-Pelican"

# Blogroll
LINKS = (('Pelican', 'http://getpelican.com/'),
         ('Python.org', 'http://python.org/'),
         ('Jinja2', 'http://jinja.pocoo.org/'),
         ('You can modify those links in your config file', '#'),)

# Social widget
SOCIAL = (('twitter', 'https://twitter.com/JulienNuellas'),
          ('linkedin', 'https://fr.linkedin.com/in/julien-nuellas'),
          ('github', 'https://github.com/JN-Lab'))

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
