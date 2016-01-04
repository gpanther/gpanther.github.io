Title: Fixing CVS annotate
Date: 2009-10-07 17:19
Author: Attila-Mihaly Balazs
Tags: programming, perl, version control, cvs
Slug: fixing-cvs-annotate
Status: published

[![3415325123\_d6e1435b48\_b](http://lh6.ggpht.com/_hrvCBhtWhJ4/SsyjaeBg20I/AAAAAAAAB84/PKECSBB_7LA/3415325123_d6e1435b48_b_thumb.jpg?imgmax=800 "3415325123_d6e1435b48_b")](http://lh4.ggpht.com/_hrvCBhtWhJ4/SsyjaNkjZgI/AAAAAAAAB80/3I4afc30z2g/s1600-h/3415325123_d6e1435b48_b2.jpg)
Yes, some of us work on projects started almost a decade ago and as such
we use CVS (yes, CVS has many limitations and yes, git is better – for a
nice introduction see [Randal Schwarz’s video about
git](http://video.google.com/videoplay?docid=-3999952944619245780#)),
but migrating is not directly justifiable (it would involve: training IT
staff to be able to maintain the repo, rewriting automation code which
relies on CVS and training programmers – even though some of these could
be postponed given that git contains a CVS bridge). Anyway, the problem
which I faced was the following: `cvs annotate` only displays the first
8 characters of the username, which can be ambiguous if multiple people
have similar usernames (which can easily happen if there is a convention
like name.surname). Here is my solution to the problem: fetch the log
for the file get the user associated whit each version (in the log CVS
includes the full usernames). Then fetch the annotated version of the
file and use the version to disambiguate the user. Here is some Perl
code:

    sub processAnnotations {
      my $fileName = shift;
      my ($cmdLine, $pid, %revisions);

      $cmdLine = "cvs -z9 log -N '$fileName'";
      $pid = open F, "$cmdLine |";
      my $rev;
      while () {
        $rev = $1 if (/^revision ([0-9\.]+)$/);
        $revisions{$rev} = $1 if (/^date:.*?author: (.*?);/);
      }
      close F;
      waitpid($pid, 0);

      $cmdLine = "cvs -z9 annotate '$fileName'";
      $pid = open F, "$cmdLine |";
      my @annFileLines;
      while () {
        if (/^(\d[0-9\.]+)(\s+)\(\S+ (.*)/s && exists $revisions{$1}) {
          $_ = "$1$2(" . $revisions{$1} . " $3";
        }
        push @annFileLines, $_;
      }  
      close F; 
      waitpid($pid, 0);    
      
      return join('', @annFileLines);
    }

</p>
PS. I verified in the CVS source that the output width for the author
field is hardcoded:

               sprintf (buf, "%-12s (%-8.8s ",
                     prvers->version,
                     prvers->author);

Picture taken from [Valeriana Solaris'
photostream](http://www.flickr.com/photos/valerianasolaris/) with
permission.
