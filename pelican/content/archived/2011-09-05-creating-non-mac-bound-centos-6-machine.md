Title: Creating a non-MAC bound CentOS 6 machine
Date: 2011-09-05 10:04
Author: Attila-Mihaly Balazs
Tags: virtualbox, centos, linux, networking, vagrant, virtualization
Slug: creating-non-mac-bound-centos-6-machine
Status: published

I was building VMs to be deployed with [Vagrant](http://vagrantup.com/)
/ [Virtualbox](http://www.virtualbox.org/) for our QAs and discovered
that on new instantiations of the machine the networking interface
wasn't coming up. The problem was that Virtualbox was assigning a random
MAC address to the NIC (and rightly so, to avoid conflicts). I used the
following steps to solve this:

1.  Remove the HWADDR line from
    `/etc/sysconfig/network-scripts/ifcfg/eth0`
2.  Delete the file `/etc/udev/rules.d/70-persistent-net.rules` ([hat
    tip](http://bachem.wordpress.com/2010/08/27/udev-renamed-network-interface-eth0-to-eth5/))

These two steps are specific to CentOS 6 (on 5.x the first step is
sufficient). Also, the second if is recreated at the next boot, thus
after rm-ing it, you should shut down the machine and package it (not
start it again, or if you do, you should remove the file again).
