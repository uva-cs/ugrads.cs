#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'Aaron Bloomfield'
SITENAME = u'Undergrad CS Resources @ UVa'
SITEURL = 'http://ugrads.cs.virginia.edu'

PATH = 'content'

TIMEZONE = 'America/New_York'

DEFAULT_LANG = u'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (('UVa CS', 'http://www.cs.virginia.edu'),
         ('UVa', 'http://virginia.edu'),
         ('UVa Collab','https://collab.itc.virginia.edu/portal'),
         ('SIS login','https://sisuva.admin.virginia.edu/psp/epprd/EMPLOYEE/EMPL/h/?tab=PAPP_GUEST'),)

# Social widget
SOCIAL = (('Facebook (by students)', 'https://www.facebook.com/groups/216856585086114'),
          ('Offical UVa CS page', 'https://www.facebook.com/uvacs'),
          ('Github','https://github.com/uva-cs'),
          ('Twitter feed: @CS_UVa','https://twitter.com/cs_uva'),
          ('LinkedIn account','https://www.linkedin.com/groups/3998950'),
          ('Instragram','https://www.instagram.com/uva_cs/'),)

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

ARTICLE_ORDER_BY = 'sortorder'
PAGE_ORDER_BY = 'sortorder'
