Title: Clearing your Google App Engine datastore
Date: 2012-08-15 10:08
Author: Attila-Mihaly Balazs
Tags: gae, google app engine, python
Slug: clearing-your-google-app-engine
Status: published

**Warning! This is a method to erase the data from your Google App
Engine datastore. There is no way to recover your data after you go
trough with this! Only use this if you're absolutely certain!**

If you have a GAE account used for experimentation, you might like to
clean it up sometimes (erase the contents of the datastore and blobstore
associated with the application). Doing this trough the admin interface
can become very tedious, so here is an alternative method:

1.  Start your [Remote API
    shell](https://developers.google.com/appengine/articles/remote_api)
2.  Use the following code to delete all datastore entities:

        while True: keys=db.Query(keys_only=True).fetch(500); db.delete(keys); print "Deleted 500 entries, the last of which was %s" % keys[-1].to_path()

3.  Use the following code to delete all blobstore entities:

        from google.appengine.ext.blobstore import *
        while True: list=BlobInfo.all().fetch(500); delete([b.key() for b in list]);  print "Deleted elements, the last of which was %s" % list[-1].filename

The above method is inspired by [this stackoverflow
answer](http://stackoverflow.com/questions/1062540/how-to-delete-all-datastore-in-google-app-engine),
but has the advantage that it does the deletion in smaller steps,
meaning that the risk of the entire transaction being aborted because of
deadline exceeded or over quota errors is removed.

Final caveats:

-   This can be slow
-   This consumes your quota, so you might have to do it over several
    days or raise your quota
-   The code is written in a very non-pythonic way (multiple statements
    on one line) for the ease of copy-pasting

