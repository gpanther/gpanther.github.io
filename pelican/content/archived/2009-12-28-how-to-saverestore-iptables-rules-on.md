Title: How to save/restore iptables rules on Ubuntu?
Date: 2009-12-28 13:01
Author: Attila-Mihaly Balazs
Tags: firewalls, ubuntu, linux, tcp/ip, tip
Slug: how-to-saverestore-iptables-rules-on
Status: published

This might be an obvious thing to old Linux-heads out there, but it sure
caught me off-guard, so there might be some use in spelling it out:

**`iptables-save` and `iptables-restore` do not actually save/load the
iptables rules to/from an external file. You are responsible for
redirecting the output of `iptables-save` to a file and modifying the
interface-up scripts such that it is loaded before the given interface
comes up.**

The [Ubuntu documentation tells you
how](https://help.ubuntu.com/community/IptablesHowTo#Saving%20iptables)
(although, it also was the source of my confusion) - the following
commands should be executed as root, so don't forget to `sudo su` first:

1.  Save your rules in a file: `iptables-save >/etc/iptables.rules`
2.  Edit your interfaces file (substitute your own favorite editor
    here): `nano /etc/network/interfaces`
3.  Add a pre-up command to restore the saved rule. The fully configured
    file should look similar to this (the bold line is the one added):

        auto eth0
        iface eth0 inet dhcp
          pre-up iptables-restore < /etc/iptables.rules

HTH. And remember - security is a process / mindset, not a state. Always
test the configuration changes you've done, don't just assume that
everything went ok because you didn't receive error messages.
