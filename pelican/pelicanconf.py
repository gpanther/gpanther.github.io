#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'Grey Panther'
SITENAME = u"Grey Panther's Place"
SITEURL = 'https://gpanther.github.io'
THEME = '../pelican-bootstrap3'
BOOTSTRAP_THEME = 'superhero'
PYGMENTS_STYLE = 'solarizeddark'
PATH = 'content'
TIMEZONE = 'Europe/Bucharest'
ARTICLE_SAVE_AS = '{date:%Y}/{date:%m}/{slug}.html'
ARTICLE_URL = '{date:%Y}/{date:%m}/{slug}.html'
TYPOGRIFY = True
CC_LICENSE = 'CC-BY'
BOOTSTRAP_FLUID = True
DEFAULT_LANG = u'en'
ABOUT_ME = '<a href="/">father, husband, software craftsman</a>'
AVATAR = '/images/profile.png'
TWITTER_CARDS = True
TWITTER_USERNAME = 'cdman83'

FEED_ALL_ATOM = 'feeds/posts/default'
FEED_ALL_RSS = 'feeds/rss'
CATEGORY_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

PLUGIN_PATHS = ['../pelican-plugins']
PLUGINS = ['related_posts', 'sitemap']

DISPLAY_PAGES_ON_MENU = False
DISPLAY_CATEGORIES_ON_MENU = False
MENUITEMS = (
	('About', '/'),
	('Blog', '/category/blog.html'),
	('Resume / Curriculum Vitae', '/pages/resume-curriculum-vitae.html'),
	('Archived blog articles', '/category/archived.html'),
)

LINKS = None

SOCIAL = (
	('linkedin', 'https://ro.linkedin.com/in/gpanther'),
	('stackoverflow', 'http://stackoverflow.com/users/1265/grey-panther', 'stack-overflow'),
	('github', 'https://github.com/gpanther/'),
)

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
