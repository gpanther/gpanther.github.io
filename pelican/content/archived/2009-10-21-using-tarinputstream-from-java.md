Title: Using TarInputStream from Java
Date: 2009-10-21 19:38
Author: Attila-Mihaly Balazs
Tags: programming, archive, java
Slug: using-tarinputstream-from-java
Status: published

[![994941366\_af693049f1\_o](http://lh6.ggpht.com/_hrvCBhtWhJ4/St85BzIfuwI/AAAAAAAAB9c/K96xgYTo9uc/994941366_af693049f1_o_thumb.png?imgmax=800 "994941366_af693049f1_o")](http://lh4.ggpht.com/_hrvCBhtWhJ4/St85BWq7yJI/AAAAAAAAB9Y/ZNz-TVsKCxs/s1600-h/994941366_af693049f1_o%5B2%5D.png)
Recently I had to parse trough a bunch of logs, scattered in
subdirectories and different types of archives (tar, bz and gz). My
first thought was of course Perl (since it is *the* language for parsing
quasi-freeform text), however I didn’t have “streaming” implementation
for the archive modules, which in my case was very important, since the
archives were *big* and reading them completely into memory was not
acceptable. So I fund the
[TarInputStream](http://api.dpml.net/ant/1.7.0/org/apache/tools/tar/TarInputStream.html)
/
[CBZip2InputStream](http://api.dpml.net/ant/1.7.0/org/apache/tools/bzip2/CBZip2InputStream.html)
from Apache Ant and
[GZIPInputStream](http://java.sun.com/javase/6/docs/api/java/util/zip/GZIPInputStream.html),
which is readily available in the JRE. While the last two are quite
straight-forward to use, I’ve had to beat my head against the wall for
quite some time before I managed to use TarInputStream. To save other
people the hassle, here is a short writeup on what I’ve learned:

-   After creating the TarInputStream, you start out by calling
    [getNextEntry](http://api.dpml.net/ant/1.7.0/org/apache/tools/tar/TarInputStream.html#getNextEntry()).
-   You do this until it returns null (similar to how you would read a
    textfile line-by-line with BufferedReader)
-   tar doesn’t actually compress anything, it just concatenates the
    data in a sequence of  
   <header>
    <data> series. After calling getNextEntry the TarInputStream is
    positioned right at the start of the data for the given entry (if it
    is a file, which you should also check) </data>
    </header>
-   To read the data associated with the TarEntry you just obtained, you
    have two possibilities:
    -   You can use the the
        [copyEntryContents](http://api.dpml.net/ant/1.7.0/org/apache/tools/tar/TarInputStream.html#copyEntryContents(java.io.OutputStream))
        method *on the stream* to put the data in an other stream (in
        memory, in an other file, etc). Just make sure that you have
        enough memory / disk space to do so
    -   You can read the contents directly from the stream. For example
        you can layer a GZIPInputStream (or CBZip2InputStream) over the
        TarInputStream if you have a gz / bz2 in a tar (usually it’s the
        reverse, this was the case for my little parser for example)

One thing to watch out for if you choose the second method, is the fact
that TarInputStream is very sensible to positioning. So if the stream
you layer on top of it has a off-by-one error (ie. it reads a couple of
bytes more than the actual size of the data), you can quickly get a
mysterious IOException which says something along the lines of “reading
from output buffer”.

My solution to the problem was to layer a custom FilterStream on top of
TarInputStream before handing it over to an other stream which does two
things:

1.  it makes sure that the stream on top of it can read only N bytes,
    where N is the size of the entry and
2.  when close is called on it, it doesn’t propagate it to the
    TarInputStream (so that it doesn’t get closed and further entries
    can be processed)

Below you can see this filter stream:

    public class SizeLimiterInputStream extends FilterInputStream {
      final long maxSize;
      final InputStream base;
      long alreadyRead;
      
      public SizeLimitInputStream(InputStream in, long maxSize) {
        super(in);
        this.maxSize = maxSize;
        alreadyRead = 0;
        base = in;
      }
      
      @Override
      public synchronized int available() throws IOException {      
        long a = base.available();
        if (alreadyRead + a > maxSize)
          a = maxSize - alreadyRead;
        return (int)a;          
      }
      
      @Override
      public void close() {
        // do nothing
      }
      
      @Override
      public boolean markSupported() {
        return false;
      }
      
      @Override
      public void mark(int readlimit) {
        // do nothing
      }
      
      @Override
      public void reset() throws IOException {
        // do nothing 
      }
      
      @Override
      public synchronized int read() throws IOException {
        if (alreadyRead >= maxSize)
          throw new EOFException();
        int r = base.read();
        alreadyRead += 1;
        return r;
      }
      
      @Override
      public synchronized int read(byte[] b) throws IOException {
        return read(b, 0, b.length);
      }
      
      @Override
      public synchronized int read(byte[] b, int off, int len) throws IOException {
        if (alreadyRead >= maxSize)
          return -1;
        if (alreadyRead + len > maxSize)
          len = (int)(maxSize - alreadyRead);
        int r = base.read(b, off, len);
        alreadyRead += r;
        return r;
      }
      
      @Override
      public synchronized long skip(long n) throws IOException {
        if (n < 0)
          return 0;
        if (alreadyRead >= maxSize)
          return 0;
        if (alreadyRead + n > maxSize)
          n = maxSize - alreadyRead;
        long r = base.skip(n);
        alreadyRead += r;
        return r;
      }
        
    }

So your code would like something along the lines of:

    TarInputStream tis = new TarInputStream(fileInputStream);
    TarEntry tarEntry;
    while ((tarEntry = tis.getNextEntry()) != null) {
      if (tarEntry.isDirectory()) continue;

      InputStream tmpIn = new SizeLimitInputStream(tis, tarEntry.getSize());                
      // process tmpIn - create other streams on top of it for example ...
    }
    tis.close();

Hope this helps.

Picture taken from [quapan's
photostream](http://www.flickr.com/photos/hinkelstone/) with permission.
