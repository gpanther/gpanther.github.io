Title: Capturing your screen on Ubuntu - with sound
Date: 2013-08-14 09:50
Author: Attila-Mihaly Balazs
Tags: ubuntu, screencapture, screencasts
Slug: capturing-your-screen-on-ubuntu-with
Status: published

Today I have a short script which I cobbled together from Google
searches to do screen captures / screen casts with Ubuntu (including
audio in so that you can narrate what is going on):

    #!/bin/bash
    Xaxis=$(xrandr -q | grep '*' | uniq | awk '{print $1}' |  cut -d 'x' -f1)
    Yaxis=$(xrandr -q | grep '*' | uniq | awk '{print $1}' |  cut -d 'x' -f2)
    avconv -f alsa -i pulse -f x11grab -s $(($Xaxis))x$(($Yaxis)) -i $DISPLAY.0 -r 15 -c:v libx264 -crf 0 -c:a libvo_aacenc -b:a 256k -threads 8 ~/Videos/output.mp4

</code>

I found this to work much better than gtk-recordmydesktop, which had
lags, especially when "effects" were being drawn on the screen (like
bulletpoints sliding in for a presentation or switching between
desktops).
