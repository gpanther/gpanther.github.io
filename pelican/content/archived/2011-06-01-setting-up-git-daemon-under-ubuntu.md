Title: Setting up git-daemon under Ubuntu
Date: 2011-06-01 20:19
Author: Attila-Mihaly Balazs
Tags: ubuntu, git, git-daemon
Slug: setting-up-git-daemon-under-ubuntu
Status: published

The scenario is the following: inside a (somewhat) trusted LAN you would
like to set up git-daemon so that your coworkers can access your
repositories. This solution is not appropriate in cases where you want
to share with random people on the interwebs. This short description is
based loosely on [this blogpost](http://rockfloat.com/blog/?id=40) and
it was updated to contain more details and tested with Ubuntu 11.04.

-   install the git-daemon-runit package:
    `sudo apt-get install git-daemon-runit`
-   decide where you would like to keep your git repositories - it can
    be your home folder, if it's not encrypted (if it's encrypted it
    won't work because it only gets decrypted once you log in, so the
    git repositories won't be available unless you log in). Lets say
    that you've decided it to be `/var/git`. Create it:  
   `sudo mkdir /var/git        sudo chown $USER /var/git`
-   Now edit the file `/etc/sv/git-daemon/run` and make it like the
    following (bold marks the spots which were changed):  
   `#!/bin/sh        exec 2>&1         echo 'git-daemon starting.'         exec chpst -ugitdaemon \           "$(git --exec-path)"/git-daemon --verbose --export-all --base-path=/var/git /var/git`
-   Restart the service:  
   `sudo sv restart git-daemon`
-   Enable it from the firewall:  
   `sudo ufw allow 9418/tcp`

That's it. Now every subdirectory from /var/git which "looks like" a git
repo (has a .git subdirectory) will be available over the git protocol.
Alternatively, you can remove the "--export-all" option and create a
"git-daemon-export-ok" file in each subdirectory you would like to
export: touch /var/git/core/git-daemon-export-ok

You can symlink the directory to your home folder for your convenience:  
`ln -s /var/git ~/projects/git`
