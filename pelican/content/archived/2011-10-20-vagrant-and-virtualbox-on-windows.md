Title: Vagrant and VirtualBox on Windows
Date: 2011-10-20 15:27
Author: Attila-Mihaly Balazs
Tags: virtualbox, windows, vagrant, virtualization
Slug: vagrant-and-virtualbox-on-windows
Status: published

[Vagrant](http://vagrantup.com/) is a collection of scripts written in
Ruby to manage VirtualBox images in a shared environment (like the QA
boxes inside a company): install them, update them, etc. Unfortunately
installing it under Windows is not as straight forward as one would
want, so here are some useful tips:

-   Read the [Windows setup
    page](http://vagrantup.com/docs/getting-started/setup/windows.html)
    and the [Windows x64 setup
    page](http://vagrantup.com/docs/getting-started/setup/windows_x64.html)
    (if you are on 64 bit)

If you are on a 64 bit Windows install:

-   Check out [this
    post](http://hype-free.blogspot.com/2011/09/running-jruby-on-64-bit-windows.html)
    if your JRuby is using the 32 bit JVM on a x64 Windows setup
-   You need to use version 4.0 of VirtualBox (rather than the latest).
    You can get it from
    [here](https://www.virtualbox.org/wiki/Download_Old_Builds_4_0)
-   You need to use an older version of Vagrant: ` `

        jgem install jruby-openssl jruby-win32ole
        jgem install --version '=0.7.8' vagrant

-   If the vagrant box download stops around 4G, check that you have a
    NTFS filesystem (rather than FAT) and deactivate any "network"
    scanning capabilities of installed security software (I had problems
    with NOD32 particularly)

HTH
