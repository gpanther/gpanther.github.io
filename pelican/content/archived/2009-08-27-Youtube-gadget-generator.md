Title: Youtube gadget generator
Date: 2009-08-27 17:43
Author: Attila-Mihaly Balazs
Slug: Youtube-gadget-generator
Status: published

Some time ago I posted about how [the Google Gadget code for Youtube
seems to be borked
up](http://hype-free.blogspot.com/2009/06/youtube-channel-embedding-being-all.html).
Now it seems that they completely removed the option from the YouTube
pages, for whatever reason, but the old code still seems functional. So
below you can find a small Javascript which generates the equivalent
code for a given Youtube user (if you are reading this in an RSS reader,
you need to click trough to the post page, since chances are that the
reader stripped out the JS for security reasons).

Of course this is an unofficial and unsupported solution, so it might
break at any time and without warning!

<p>
<script>
\<br /\> function showmethemoneyyoutube() {\<br /\> var prefix =
"\<scr" + "ipt\>\\n/\* \<![CDATA[ \*/\\n(function(){var css='\<br /\>
\<style\>table.gadget{background-position:0%;background:transparent
none;border-collapse:collapse;border:0;clear:none;float:none;font-family:arial,sans-serif;font-style:normal;font-variant:normal;height:auto;letter-spacing:normal;line-height:normal;margin:0;padding:0;text-indent:0;text-transform:none;top:auto;vertical-align:middle;white-space:normal;width:auto;word-spacing:normal;}table.gadget
span.title a:hover,table.gadget span.title a:visited,table.gadget
span.title a:active,table.gadget
span.title{font-size:12px;color:\#0000cc}table.gadget span.powered
a:hover,table.gadget span.powered a:visited,table.gadget span.powered
a:active,table.gadget
span.powered{font-size:10px;color:\#0000cc}\</style\> \<p\>';var
js='';var html='\\x3ctable class\\x3d\\x22gadget\\x22 cellspacing\\x3d0
cellpadding\\x3d0
width\\x3d320\\x3e\\x3ctr\\x3e\\x3c/tr\\x3e\\x3ctr\\x3e\\x3ctd
colspan\\x3d2\\x3e\\x3cdiv style\\x3d\\x22background:white;padding:3px;
border:1px solid \#999999;\\x22\\x3e\\x3ciframe
src\\x3d\\x22http://www.gmodules.com/ig/ifr?container\\x3dyoutube\\x26mid\\x3d1\\x26v\\x3d1d667595b6f563bb6e77ac593b4a245\\x26lang\\x3dall\\x26country\\x3dALL\\x26view\\x3dhome\\x26up\_channel\\x3d";\<br
/\> var suffix =
"\\x26url\\x3dhttp%3A%2F%2Fwww.google.com%2Fig%2Fmodules%2Fyoutube.xml\\x26source\\x3d\_\_LOCATION\_\_\\x26parent\\x3d\_\_LOCATION\_\_\\x26libs\\x3dcore%3Acore.io\\x22
width\\x3d320 height\\x3d390 style\\x3d\\x22display:block;\\x22
frameborder\\x3d0
scrolling\\x3d\\x22no\\x22\\x3e\\x3c/iframe\\x3e\\x3c/div\\x3e\\x3c/td\\x3e\\x3c/tr\\x3e\\x3ctr\\x3e\\x3ctd
style\\x3d\\x22text-align:left;vertical-align:middle;height:28px;\\x22\\x3e\\x3ca
href\\x3d\\x22http://fusion.google.com/ig/add?synd\\x3dopen\\x26source\\x3dggyp\\x26moduleurl\\x3dhttp://www.google.com/ig/modules/youtube.xml\\x22
target\\x3d\\x22\_top\\x22\\x3e\\x3cimg style\\x3d\\x22border:0;\\x22
src\\x3d\\x22http://www.gmodules.com/ig/images/plus\_google.gif\\x22\\x3e\\x3c/a\\x3e\\x3c/td\\x3e\\x3ctd
style\\x3d\\x22text-align:right;vertical-align:middle;height:28px;\\x22\\x3e\\x3cspan
class\\x3d\\x22powered\\x22\\x3e\\x3ca
href\\x3d\\x22http://www.google.com/webmasters/gadgets.html\\x22
target\\x3d\\x22\_top\\x22\\x3eGadgets\\x3c/a\\x3e powered by
Google\\x3c/span\\x3e\\x3c/td\\x3e\\x3c/tr\\x3e\\x3c/table\\x3e';html=html.replace(/\_\_LOCATION\_\_/g,
encodeURIComponent(location.href));document.write(css+js+html);})();\\n/\* \*/\\n\</p\>
