Title: Converting datetime to UTC in python
Date: 2013-02-07 19:06
Author: Attila-Mihaly Balazs
Tags: gae, datetime, python, ndb
Slug: converting-datetime-to-utc-in-python
Status: published

So you need to convert a python datetime object which has a timezone set
("aware" in the Python nomenclature) to an UTC one with no timezone set
("naive"), for example because NDB on GAE [can't store anything
else](http://code.google.com/p/appengine-ndb-experiment/source/browse/ndb/model.py?r=6b3f88b663a82831e9ecee8adbad014ff774c365#1916).
The solution will look something like this:

    date = date.astimezone(tz.tzutc()).replace(tzinfo=None)

For searcheability: the exception thrown by NDB if you fail to do this
is "NotImplementedError: DatetimeProperty updated\_at can only support
UTC. Please derive a new Property to support alternative timezones."
