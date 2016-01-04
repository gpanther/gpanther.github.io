Title: Getting the most out of your audio recording with Audacity
Date: 2011-10-08 13:45
Author: Attila-Mihaly Balazs
Tags: audio, audacity, audio processing, noise removal, podcast
Slug: getting-most-out-of-your-audio
Status: published

This article aims to show you some *simple* techniques to improve the
quality of your voice recording quickly and cheaply (for free actually).
But first things first:

The best audio is the one you don’t have to improve. Some simple steps
you can perform in advance to maximize quality:

-   Use quality equipment.
    [Here](http://www.joelonsoftware.com/articles/PodcastEquipment.html)
    [are](http://twit.tv/podcastequipment)
    [some](http://www.pwop.com/podcastingkit.aspx) [articles](http://nerds-central.blogspot.com/2011/09/good-quality-youtube-posts-with-cheep.html)
    about the equipment great-sounding podcasters use. You don’t have to
    spend a lot of money, but definitely stay away from the built-in
    laptop microphone
-   Eliminate ambient noise as much as possible (close windows, draw the
    blinds, stop other electronic equipment in the room, etc)
-   Record each person on a separate channel - if possible on a computer
    local to them (avoid recording trough Skype, GoToMeeting or other
    VoIP solutions)
-   Try keeping the recording volume for each microphone at the optimal
    level – not too low, but also avoiding clipping

After you have the audio recording there is still a lot you can do, but
it is preferable to start out with the best source material. For the
example below I’ll be using the raw recordings from a recent [SE Radio
podcast](http://www.se-radio.net/):

[![tmp9FD1](http://lh6.ggpht.com/-Th92EbElRnQ/TpAppSbw3XI/AAAAAAAAEVE/SbttRJPwSPY/tmp9FD1_thumb2.png?imgmax=800 "tmp9FD1")](http://lh4.ggpht.com/-pxj_nuiaWgo/TpApn9YkG2I/AAAAAAAAEVA/m8V9P5DsdTY/s1600-h/tmp9FD15.png)

The situation with this recording is as follows:

-   There are separate audio tracks for the interviewer and interviewee
    (good)
-   There is background noise on the tracks (easily correctable)
-   Both persons were picked up by both microphones (correctable)
-   The interviewer has some clipping (partially correctable – luckily
    it’s not the interviewee who has clipping)

The steps to improve the quality of this recording are as follows:

First, install the [Noise Gate
plugin](http://wiki.audacityteam.org/wiki/Nyquist_Effect_Plug-ins#Noise_Gate)
for Audacity, since it requires program restart (under Windows you have
to copy the downloaded `noisegate.ny` to
`C:\Program Files (x86)\Audacity 1.3 Beta (Unicode)\Plug-Ins` or to a
similar location, under Linux you have to place it in
`/usr/share/audacity`). After copying the file you have to close and
restart Audacity. To verify that the plugin was properly installed check
in the Effect menu – you should see an entry title “Noise gate”.

Now that we have Audacity all set up and the plugin installed, first
split the stereo track into mono tracks, since they don’t actually
represent left-right channels but rather two speakers which will be
mixed together at the end. For this click on the arrow after the
filename in the track and select “Split Stereo to Mono”. Sidenote: some
people will prefer to mix different speakers in podcasts with different
panning (that is to the left or to the right). I would advise against
this: it is distracting if you are doing something else while listening
to the podcast (like walking / jogging / riding a bike / etc). It can
also backfire if for some reason the listening device is missing one of
the channels (the “damaged headphone” scenario).

The first thing will be to remove the constant background noise (like AC
hum for example). To do this zoom in (Ctrl + 1) and look for low volume
zones. Select those zones and go to Effects –\> Noise Removal –\> Get
Noise Profile. Now select a zone where the noise is mixed with speech
and test out the settings (Effect –\> Noise Removal –\> Ok). After the
test you can use Undo (Ctrl + Z) to roll back the changes. You should
watch for the noise being removed but also the natural sound of the
voice being preserved (too aggressive of a noise removal can lead to a
“robot voice” effect). If you are satisfied, you can go ahead and apply
it to the entire track. Also, since the noise source might change during
the recording, you should at least do a quick scroll to check for other
low-volume zones which can be a sign of noise. If you find noise from
other sources, you can use the same steps to remove it.

Now that you have removed the noise, the next step would be to remove
the voices from the channels they don’t belong to. This is where we’ll
be using the Noise Gate plugin: since there is a considerable level
difference between the wanted audio and the unwanted audio on each
channel, we can just declare everything below a certain volume “noise”
and use the plugin to silence it. A couple of tips:

-   This needs to be done separately for each channel, since the cutoff
    volume will be different
-   You can use the “Analyse Noise Level” function of the plugin to
    gauge the approximate level of the cutoff volume – this will only
    give you an estimate and you will have to play around with the
    settings a little bit to find the optimal volume
-   Use a “Level reduction” of –100 dB to completely filter out the
    sound and an “Attack/Decay” of 1000 milliseconds to avoid false
    positives
-   As with all the steps, you can experiment on a smaller portion of
    the audio file (since it is much quicker) to fine tune the settings
    by repeatedly applying the effect with different parameters and
    undoing (Ctrl+Z) the result after evaluation. When the parameters
    seem right, just select the entire track and press Ctrl+R (Repeat
    last effect)

After we’ve finished with both tracks, we have a better situation:

[![tmpA935](http://lh4.ggpht.com/-UBD2l2IuZ6M/TpApsxxchEI/AAAAAAAAEVM/OvfXFt8SFdc/tmpA935_thumb2.png?imgmax=800 "tmpA935")](http://lh6.ggpht.com/-bQuXJCuceZk/TpAprrOXcqI/AAAAAAAAEVI/8Pz8XHdC1KA/s1600-h/tmpA9355.png)

Now we will fix the clipping as much as possible (a perfect fix isn’t
possible since clipping means that information got lost and all the
plugins can do is to “guess” what the information might have looked
like). First we reduce the aplification of the second track (the one
which contains the clipping) by 10 dB as the Clip Fix plugin suggests
(Effect –\> Aplify –\> –10 dB) after which we use the Clip Fix plugin.
Unfortunately this plugin runs very slowly if we would to apply it to
the entire track at once. Fortunately we have a reasonable workaround:
select portions of the track and apply the plugin to them individually.
After the first application you can use the “Repeat last effect”
shortcut (Ctrl+R) to speed up the operation. Sidenote: it is a good
habit to use the “Find Zero Crossing” function whenever you do a
selection (the shortcut is Z – so whenever you select a portion, just
press Z afterwards). This eliminates some weird artifacts when cutting /
pasting / silencing part of the audio and it might even help when
applying different effects. The fixed audio looks like this:

[![tmpA4D3](http://lh4.ggpht.com/-Tl2basYoDrQ/TpApvWB-svI/AAAAAAAAEVU/K3KxlkOfjw0/tmpA4D3_thumb%25255B2%25255D.png?imgmax=800 "tmpA4D3")](http://lh6.ggpht.com/-OTPZJgmoVZE/TpApuBGpFbI/AAAAAAAAEVQ/R0cNJMaawGw/s1600-h/tmpA4D3%25255B5%25255D.png)

Now, that all the cleanup steps have been performed, there is one last
step which is as important as the cleanup: maximizing the audible volume
without introducing clipping. This is very important because all devices
can *reduce* volume but few of them can *increase* it (some exceptions
being: the Linux audio stack and VLC). The easiest way to do this is by
using the Levelator (note: while the Levelator is free – as in beer –
and does not restrict what you can do with the output, it is not free as
in freedom if this is a consideration for you).

To do this, export the audio to WAV (make sure that all tracks are
unmuted during export) and run the Levelator on it. The end result will
look like the following:

[![tmpC726](http://lh6.ggpht.com/-N4ISXjxSgWA/TpApxE1lutI/AAAAAAAAEVc/W1Ncs98kSmo/tmpC726_thumb%25255B2%25255D.png?imgmax=800 "tmpC726")](http://lh3.ggpht.com/-J5yUvt9KAgc/TpApwQStEeI/AAAAAAAAEVY/0weSgZTtRYc/s1600-h/tmpC726%25255B5%25255D.png)

Of course the Levelator isn’t magic pixie dust either, so here are a
couple of things to check after it has been run:

-   Did it amplify some residual noise which wasn’t available in the
    initial audio? (if so, you should remove it using the Noise Removal
    plugin)
-   Did it miss segments? (it is rare, but it happens – those segments
    need to be amplified manually)
-   It results in “weird” sounding audio if the recording has been
    preprocessed by a dynamic compressor – for example GoToMeeting has
    an option to improve sound quality which uses dynamic compression
    and thus makes the recording unsuitable for the use with Levelator

That’s it for this rather long article. Don’t be discouraged by the
length of the article: after going over the steps a couple of times, it
shouldn’t take longer than 15 minutes to process a 2 hour interview
(excluding the cutting / pasting / moving parts around) and you will
gain listeners because of the higher production value.

A final note on the output formats: while during processing you should
always use lossless formats, the final output format I recommend is: MP3
at 64 kbps CBR, Joint Stereo, 22050 MHz sampling rate. I found that this
is the best balance between quality, file size and compatibility with
the most playback devices out there.
