#!/usr/bin/env python
import datetime
import re

title = raw_input("Title: ")
slug = title.lower()
slug = re.sub(r'\W+', '-', slug)
now = datetime.datetime.now()
filename = 'content/blog/' + now.strftime('%Y-%m') + '-' + slug + '.md'

with open(filename, 'w') as f:
	f.write('''Title: %s
Date: %s
Author: Attila-Mihaly Balazs
Tags:

Here!
''' % (
title,
now.strftime('%Y-%m-%d %H:%M'),
))

