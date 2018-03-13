#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

THEME = 'pelican-bootstrap3'

AUTHOR = 'Network and Information Security Lab, Tsinghua University'
SITENAME = 'NISL@THU'
SITEURL = ''

PATH = 'content'

TIMEZONE = 'Asia/Shanghai'

DEFAULT_LANG = 'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
#LINKS = (('InForSec', 'https://inforsec.org'),
#         ('CTF blue-lotus', 'http://www.blue-lotus.net/'),
#         ('Tsinghua Unvi.', 'http://www.tsinghua.edu.cn/'),
#        )

# Social widget
#SOCIAL = (('You can add links in your config file', '#'),
#          ('Another social link', '#'),)

DEFAULT_PAGINATION = 10

#PLUGIN_PATHS = ['/home/yzm/pelican-plugins', ]
PLUGINS = ['i18n_subsites', 'pelican-toc' ]
JINJA_ENVIRONMENT = {'extensions': ['jinja2.ext.i18n']}

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
