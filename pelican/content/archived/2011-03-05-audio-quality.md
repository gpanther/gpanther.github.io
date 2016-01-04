Title: Audio quality
Date: 2011-03-05 09:39
Author: Attila-Mihaly Balazs
Tags: audio, audacity, audio processing
Slug: audio-quality
Status: published

This is just one of those topics which comes up from time to time in my
life (probably because I consume a lot of media). I was recently
watching the [Jim Zemlin interviewed by Jeremy
Allison](http://www.youtube.com/watch?v=VVUHaC1somA) (Jim Zemlin is the
Executive Director of the Linux Foundation) on the [Google Open Source
YouTube channel](http://www.youtube.com/user/googleOSPO) and was
frustrated by the background noise and low audio volume, since the topic
was really interesting to me. So I decided to look into the problem and
see if the audio quality could have been easily improved. I [covered the
topic](http://hype-free.blogspot.com/2009/07/basic-multi-media-postprocessing.html)
a couple of years so I won’t go into details, rather just give a 10 000
foot view of the process. Please read [the original
post](http://hype-free.blogspot.com/2009/07/basic-multi-media-postprocessing.html)
for more details, since everything in it still applies.

Step 1: download the YouTube video. [VLC](http://www.videolan.org/vlc/)
natively supports YouTube playback, so exporting the sound to a FLAC
file (you should always use lossless codecs during processing!) was just
a matter of a couple of clicks and one or two minutes.

![export\_youtube\_vlc](http://lh6.ggpht.com/_hrvCBhtWhJ4/TXHosoGuYVI/AAAAAAAADVQ/ebhm_f4Ay2Q/export_youtube_vlc%5B5%5D.png?imgmax=800 "export_youtube_vlc")

Step 2: load up in [Audacity](http://audacity.sourceforge.net/) and
remove the noise. The loading of the FLAC file is a little buggy (the
progress bar keeps jumping between 0 and 100% and the time estimation is
useless, but it loaded in under a minute). As you can see in the
screenshot below, the volume is really low, but there are the occasional
spikes, so plain normalization wouldn’t help you here. On the upside,
there is no clipping which would result in a hard (impossible?) to
repair artifacts.

![audacity\_interview\_pre](http://lh4.ggpht.com/_hrvCBhtWhJ4/TXHotLl-BAI/AAAAAAAADVU/n_6FaZpcjYA/audacity_interview_pre%5B5%5D.png?imgmax=800 "audacity_interview_pre")

After noise removal and keeping only one channel (no need for stereo
here – we would add it back in the last step if we would to publish it
since some devices can’t handle mono and the overhead with joint stereo
is almost zero) the file was exported into WAV and fed into the
[Levelator](http://www.conversationsnetwork.org/levelator). Here is the
end result:

[![audacity\_interview\_post](http://lh4.ggpht.com/_hrvCBhtWhJ4/TXHouYC1SAI/AAAAAAAADVc/r7fvY3mZKGE/audacity_interview_post_thumb%5B2%5D.png?imgmax=800 "audacity_interview_post")](http://lh4.ggpht.com/_hrvCBhtWhJ4/TXHot4oDY7I/AAAAAAAADVY/p1cHEUkeet4/s1600-h/audacity_interview_post%5B4%5D.png)

As you can see, we have *much* better volume resulting in a *much*
improved experience for the consumer, all this with a couple of minutes
of work while browsing [Hacker News](http://news.ycombinator.com/) and
with free (and mostly open-source) cross platform tools.

Content publishers of the world: please take a couple of minutes of your
time after editing to do a proper post-production! Thank you.

*Update*: YouTube downloading is broken in the current VLC release but
it will be fixed in the next version (1.1.12). Until then you can use
the [nighly builds](http://nightlies.videolan.org/).
