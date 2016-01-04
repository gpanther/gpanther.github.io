Title: How to quickly start up a webserver with Python
Date: 2011-02-06 08:14
Author: Attila-Mihaly Balazs
Slug: how-to-quickly-start-up-webserver-with
Status: published

[![SONY
DSC](http://lh5.ggpht.com/_hrvCBhtWhJ4/TU48Om-cOpI/AAAAAAAADUc/acZFvbo5170/4046936655_d7f4067d5c_o_thumb%5B3%5D.jpg?imgmax=800 "SONY DSC")](http://lh6.ggpht.com/_hrvCBhtWhJ4/TU48NhVJ-OI/AAAAAAAADUY/98zjzpClrvY/s1600-h/4046936655_d7f4067d5c_o%5B5%5D.jpg)
Sometimes you need to quickly start up a webserver that serves up static
files (I will describe such a case in the next post). Python to the
rescue (works on both Linux and Windows if you have Python installed):

For Python 2.x (this is what most sites show you):

`python -m SimpleHTTPServer 9914`

For Python 3.x (thanks to [this
comment](http://linux.byexamples.com/archives/506/python-simple-http-server-for-file-sharing/#comment-99256)):

`python -m http.server 9914`

These will start up a webserver on port 9914, and you can access it via
the address <http://localhost:9914>. Warning! The webserver will be
available to anyone who can connect to your computer directly (unless
there are other mechanisms to restrict it – like firewalls or NAT), so
use your judgment!

Picture taken from [bob's
photostream](http://www.flickr.com/photos/mahbobyusof/4046936655/) with
permission.
