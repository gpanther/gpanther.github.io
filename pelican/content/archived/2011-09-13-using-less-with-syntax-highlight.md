Title: Using less with syntax highlight
Date: 2011-09-13 19:14
Author: Attila-Mihaly Balazs
Tags: ubuntu, linux, cli
Slug: using-less-with-syntax-highlight
Status: published

You can use vim as your pager and obtain two benefits: syntax highlight
and access to all the advanced commands (like search). You can do this
under ubuntu by adding the following line to your `~/.bashrc`:

    alias less='/usr/share/vim/vimcurrent/macros/less.sh'

</code>

Note:

-   You have to have vim installed (which doesn't come by default, but
    it is as simple as `sudo apt-get install vim-nox`)
-   It supports viewing directly bz2 and gz archives as well as pipe
    input from stdin (but in that case it fails sometime to highlight)
-   Edit commands (like dd) are disabled, so you can't accidentally
    modify the file you are viewing

