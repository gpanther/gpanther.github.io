Title: Cleaning up Google AppEngine Mapreduce Jobs
Date: 2013-11-12 12:31
Author: Attila-Mihaly Balazs
Tags: mapreduce, jquery, gae, javascript, tip
Slug: cleaning-up-google-appengine-mapreduce
Status: published

Do you use the [Google MapReduce
library](https://developers.google.com/appengine/docs/python/dataprocessing/)
on AppEngine? And do you have a lot of completed tasks which clutter
your dashboard? Use the JS below by pasting it into your developer
console to clean them up! (use it at your own risk, no warranty is
provided :-))

    schedule = function() { window.setTimeout(function() { var c = $('a:contains(Cleanup)').first(); if (c.length > 0) { c.click(); } else { $('a:contains(Next page)').click(); schedule(); } }, 300); return true; }; window.confirm = schedule; schedule();

</code>
