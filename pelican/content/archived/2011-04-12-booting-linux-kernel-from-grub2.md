Title: Booting the Linux Kernel from Grub2
Date: 2011-04-12 18:59
Author: Attila-Mihaly Balazs
Tags: grub, linux, troubleshooting, grub2
Slug: booting-linux-kernel-from-grub2
Status: published

Recently a good friend of mine managed to uninstall all the kernels from
his Ubuntu machine (what can I say - Monday morning and no coffee is a
deadly combination). Luckily he had the install CD on hand so we did the
following:

1.  Boot from the CD (we had Internet connection)
2.  Mount the Linux partition and chroot into it
3.  Reinstall the kernel with aptitude
4.  Reboot and go into Grub2 command mode
5.  Now do the following (commands need to be adjusted to match your
    partition - also, tab completion works, so you don't have to guess)

        insmod part_msdos
        insmod ext2
        set root=(hd0,3)
        linux /boot/vmlinuz-2.6.32.38-generic root=/dev/sda3 ro
        initrd /boot/initrd.img-2.6.38-6-686
        boot

It seems that most of the examples on the 'net are for Grub 1 and little
is out there for Grub 2. I found the following three: [How to use Grub2
to boot Linux
manually](http://www.justlinux.com/forum/showthread.php?threadid=152790),
[The Grub 2 Guide](http://ubuntuforums.org/showthread.php?t=1195275),
[GRUB 2 bootloader - Full
tutorial](http://www.dedoimedo.com/computers/grub-2.html#mozTocId584691).
Also, I didn't perform steps 4-5 because he just reinstalled Ubuntu (it
was a fresh install anyway), but I tried it out separately on my laptop
and it works.

HTH
