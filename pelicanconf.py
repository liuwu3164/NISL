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

PAGE_URL = '{slug}.html'
PAGE_SAVE_AS = '{slug}.html'
INDEX_SAVE_AS = 'blog_index.html'
STATIC_PATHS = ['images', 'pdfs', 'photos']

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (('InForSec', 'https://inforsec.org'),
         ('CTF blue-lotus', 'http://www.blue-lotus.net/'),
         ('Tsinghua University', 'http://www.tsinghua.edu.cn/'),
        )

# Social widget
#SOCIAL = (('You can add links in your config file', '#'),
#          ('Another social link', '#'),)

DEFAULT_PAGINATION = 10

#PLUGIN_PATHS = ['/home/yzm/pelican-plugins', ]
PLUGINS = ['i18n_subsites', 'pelican-toc' ]
JINJA_ENVIRONMENT = {'extensions': ['jinja2.ext.i18n']}

TOC = {
    'TOC_HEADERS'       : '^h[1-6]', # What headers should be included in
                                     # the generated toc
                                     # Expected format is a regular expression

    'TOC_RUN'           : 'true',    # Default value for toc generation,
                                     # if it does not evaluate
                                     # to 'true' no toc will be generated

    'TOC_INCLUDE_TITLE': 'false',     # If 'true' include title in toc
}

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
