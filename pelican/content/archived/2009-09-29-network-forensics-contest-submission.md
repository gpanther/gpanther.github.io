Title: Network Forensics Contest submission
Date: 2009-09-29 13:26
Author: Attila-Mihaly Balazs
Tags: challenge, networking, solution
Slug: network-forensics-contest-submission
Status: published

Some time ago [I mentioned the Network Forensics
Puzzle](http://hype-free.blogspot.com/2009/08/couple-of-challenges.html).
The contest is now over and since I didn’t win, I’ll publish my
submission below – it was after all correct, but not quite what the
judges were looking for (congratulation [to the
winner](http://forensicscontest.com/)).

After validating that the MD5 sum for the downloaded file matches the
one specified on the website, I first opened it up in NetworkMiner
(<http://networkminer.sourceforge.net/>). I find the overview it gives
much easier to understand than the statistics provided by Wireshark.
Using it I identified the data stream between Ann's computer and the
unidentified laptop.

1\. What is the name of Ann’s IM buddy?  
Sec558user1 - this is tricky because the IM (which seems to be AOL - but
many other IM's behave in a similar fashion) routes chat traffic trough
central servers (64.12.24.50 in this case - which belongs to AOL, making
it even more probable that AIM was used) to make NAT traversal a
non-issue, while file transfers are done trough direct connection to
conserve bandwidth.

2\. What was the first comment in the captured IM conversation?  
Here's the secret recipe... I just downloaded it from the file server.
Just copy to a thumb drive and you're good to go \>:-)  
(actually, \> is escaped as HTML - ie \>)

3\. What is the name of the file Ann transferred?  
recipe.docx

4\. What is the magic number of the file you want to extract (first four
bytes)?  
50 4B 03 04 - Which corresponds to PK..., signaling that we are
potentially dealing with a ZIP archive here. This is further reinforced
by the filename (.docx, which is the new "open" document format from
Microsoft - basically, it consists out of a zipped XML - similarly to
the OpenOffice.org format)

5\. What was the MD5sum of the file?  
8350582774e1d4dbe1d61d64c89e0ea1

This is again tricky, because ZIP (like many other formats) admit
arbitrary data after the logical end of the file. So, using a hex
editor, we first carve the the part starting at PK in the
192.168.1.158 -\> 192.168.1.159 (be careful not to include the traffic
in the reverse direction). Then we need to convince ourselves that the
end of the file has been correctly identified at the byte level. To do
this we could study the ZIP specification
([http://www.pkware.com/index.php?option=com\_content&task;=view&id;=64&Itemid;=107](http://www.pkware.com/index.php?option=com_content&task=view&id=64&Itemid=107))
or use a more empirical level: using a hex editor (HxD for example -
<http://mh-nexus.de/en/hxd/>) eliminate the last byte of the file and
"test" the integrity of the file (using the Test option from 7-zip for
example - <http://www.7-zip.org/> - but one could use almost any
de-archiving program, since almost all of them offer a "Test" option).
The test will fail. Now add back the last byte (which is 0x00) and
perform the test again. It will succeeded. This means with a big
probability that we correctly identified the actual (logical) end of the
file.

6\. What is the secret recipe?  
The most recent version of OpenOffice.org (3.1.x) can open the docx
format, so the following can be retrieved on any platform, regardless of
whether MS Office 2007 is installed (an alternative solution would be to
use the free MS Word 2007 viewer or the import filters available for
older versions of MS Office).

The contents (sans the formatting):  
Recipe for Disaster:  
1 serving  
Ingredients:  
4 cups sugar  
2 cups water  
In a medium saucepan, bring the water to a boil. Add sugar. Stir gently
over low heat until sugar is fully dissolved. Remove  the  saucepan from
heat.  Allow to cool completely. Pour into gas tank. Repeat as
necessary.
