#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'Charles Schultz'
SITENAME = "Intellection"
SITEURL = ''

PATH = 'content'

TIMEZONE = 'America/New_York'

DEFAULT_LANG = 'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = ()

# Social widget
SOCIAL = (('github', 'https://github.com/schultzca'),)

DEFAULT_PAGINATION = 10

# Enable pelican-bootstrap3 theme
THEME = '/home/charlie/projects/pelican-themes/pelican-bootstrap3'

# Enable Bootswatch darkly theme
BOOTSTRAP_THEME = "darkly"

# Enable translation
JINJA_ENVIRONMENT = {'extensions': ['jinja2.ext.i18n']}

# Path to plugins
PLUGIN_PATHS = ['/home/charlie/projects/pelican-plugins'] 

# Enable target plugins
PLUGINS = ['i18n_subsites', 'liquid_tags']

STATIC_PATHS = ['img', 'pdf']

BANNER = 'img/stylized_background.png'

BANNER_SUBTITLE = 'The process of understanding.'

DISPLAY_CATEGORIES_ON_MENU = False

ABOUT_ME = "I am a motivated individual that finds artificial intelligence and the creation of intelligent agents fascinating. My primary motivation is to develop intelligent systems to better the world."

AVATAR = "../img/profile_scaled.jpg"

SIDEBAR_ON_LEFT = False