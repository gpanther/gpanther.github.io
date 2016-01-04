Title: Setting the maximum number of opened files under Ubuntu (for JProfiler)
Date: 2011-03-20 14:29
Author: Attila-Mihaly Balazs
Tags: ubuntu, linux, jprofiler, java, tip
Slug: setting-maximum-number-of-opened-files
Status: published

**As I found out "on my own skin", setting fs.file-max in
/etc/sysctl.conf is a BAD idea. It can render your system useless in one
step. Please don't do it! If you did it, use the recovery mode to roll
back the change. Also, currently I would only recommend doubling the
limit (ie going from 1024 to 2048 or from 2048 to 4096) not going to the
maximum value.**

[JProfiler](http://www.ej-technologies.com/products/jprofiler/overview.html)
is a great tool, however under 32 bit Ubuntu you can run into the
problem of having a too low limit for open filehandles. This is a
problem for
[JProfiler](http://www.ej-technologies.com/products/jprofiler/overview.html)
because it uses temporary files to work around the address-space
limitation created by 32 bit (yeah, I know, I should upgrade to 64 bit -
but 32 bit works great for now...)

To raise the maximum filehandle limit, do the following:

    sudo gedit /etc/security/limits.conf
    # add the following two lines before the # End of file marker
    # yes, the initial star is also part of line, and you should add it
    *       hard    nofile  4096
    *       soft    nofile  4096
    sudo gedit /etc/sysctl.conf
    # restart your system

You can check if the changes were successful by using the ulimit
command:

    ulimit -n
    # it should print out 4096
