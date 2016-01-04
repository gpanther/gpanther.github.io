Title: How to generate a stackdump with GDB
Date: 2009-10-30 17:29
Author: Attila-Mihaly Balazs
Tags: debug, linux, stacktrace, gdb
Slug: how-to-generate-stackdump-with-gdb
Status: published

[![4054760074\_609af75332\_o](http://lh4.ggpht.com/_hrvCBhtWhJ4/SusGSK3A40I/AAAAAAAACBU/DYg-8FCkbxw/4054760074_609af75332_o_thumb.gif?imgmax=800 "4054760074_609af75332_o")](http://lh4.ggpht.com/_hrvCBhtWhJ4/SusGRj3WkMI/AAAAAAAACBQ/1x-Ca2yjupg/s1600-h/4054760074_609af75332_o2.gif)
I’m not a big GDB guy, but [Google always
helps](http://forums13.itrc.hp.com/service/forums/questionanswer.do?admit=109447627+1256915915603+28353475&threadId=1005951):

-   Create a textfile with the following content:

        set height 0
        thread apply all bt
        detach
        quit

-   Run the following command:

        gdb $EXE -pid $PID -command $TEXTFILE > $OUTPUTFILE

    where:

    -   \$EXE is the path to the executable
    -   \$PID is the PID it is running under
    -   \$TEXTFILE is the file where your've saved the previous commands
    -   \$OUTPUTFILE is the file where you would like your stackdump to
        be saved.

The cool little crawling logo was taken from
[HiR](http://www.h-i-r.net/2009/10/hack-o-lantern.html), head over there
for an explanation.
