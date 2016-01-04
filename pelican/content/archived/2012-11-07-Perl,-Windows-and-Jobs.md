Title: Perl, Windows and Jobs
Date: 2012-11-07 13:04
Author: Attila-Mihaly Balazs
Tags: open source, windows, perl
Slug: Perl,-Windows-and-Jobs
Status: draft

Just to make it clear: this post won't be about jobs in the traditional
sense of the word (like paying jobs), rather the Job “object” present in
the MS Windows API which can be used to manipulate groups of processes
at once.

With this out of the way, lets get back to our sheep, shall we: in the
MSDN the [Job
object](http://msdn2.microsoft.com/en-us/library/ms684841.aspx) is
defined as follows:

> A job object allows groups of processes to be managed as a unit. Job
> objects are namable, securable, sharable objects that control
> attributes of the processes associated with them. Operations performed
> on the job object affect all processes associated with the job object.

Here are some very cool things you can do with jobs (a small note: jobs
are available only in the Win2k family, meaning Win2K, XP, Win2k3 and
Vista, but I'm assuming that almost nobody is doing serious work on the
Win9x family anymore):

-   Limit the maximum runtime of either one process or all the processes
    attached to the job (of course you could create the code to do this
    by hand, but why reinvent the wheel?)
-   Make the processes in a job run with a given security token
-   Limit the maximum amount of memory the processes can allocate and/or
    can have in the RAM at any given time (aka. the working set)
-   Adjust processor affinity
-   Limit the interaction with the clipboard, the ability to create /
    switch desktops, to shut down windows,
    [etc](http://msdn2.microsoft.com/en-us/library/ms684152.aspx)
-   Make Windows silently write out a crash long instead of stopping a
    process with an error reporting popup

To summarize it up, job objects are very useful in a shared environment
(both in the sense that different type of services run on the same
machine and that multiple copies of the same service run on the machine)
to control

http://search.cpan.org/\~gsar/libwin32-0.191/Job/Job.pm

sub start\_job {  
my \$param = shift;  
my \$shell = \$param-\>{shell} || \$\^X; chomp \$shell; \# just in
case..  
loginfo(qq{Starting "\$param-\>{script}" (shell: \$shell)});

my \$job\_parameters = {  
breakaway\_ok =\> 1,  
die\_on\_unhandled\_exception =\> 1,  
};  
\$job\_parameters-\>{limit\_job\_time} = \$param-\>{max\_runtime} if
(exists \$param-\>{max\_runtime});  
my \$job = Win32::Job-\>new(\$job\_parameters);

\# 10:36 AM 10/16/2008 - amx  
if(!defined \$job){  
logerror("Win32::Job error: \\\$\^E=\$\^E");  
}

my \$current\_dir = cwd;  
chdir dirname(\$param-\>{script});  
\$job-\>spawn(\$shell, "\$shell \$param-\>{script}", {  
new\_console =\> 1,  
auto\_resume =\> 1,  
window\_attr =\> 'minimized',  
});

chdir \$current\_dir;

\#needed, because this process (almost) never terminates  
flush\_counters();

sleep 2;  
increment\_counter('started new child');

return \$job;  
}

Ghostery has found the following on this page:New Relic
