Title: Remote debugging with Java
Date: 2011-01-25 15:35
Author: Attila-Mihaly Balazs
Tags: debug, networking, java
Slug: remote-debugging-with-java
Status: published

Sometimes you have the situation that an issue is only occurring on
certain machines or only at a certain time of day. There are a couple of
possible methods to investigate such an issue (like: adding extra
logging), however I would like to add an other one: remote debugging
trough TCP/IP.

To do this, start your java program with the following jvm paramters:

    -Xdebug -Xrunjdwp:transport=dt_socket,server=y,suspend=n,address=23334

The meaning of the parameters is as follows:

-   `server=y` – this application will act as a TCP/IP server
    (“acceptor”) and wait for incoming connections rather than trying to
    connect to you
-   `suspend=n` – the server will not suspend on startup (alternatively
    you can set it to “y” in which case it will pause and wait for the
    debugger to connect – useful if you need to debug issues occurring
    at startup)
-   `address=23334` – the port on which the debugger will listen. Keep
    in mind that only one program can listen on a given port on a
    machine and if the given port is not available, the given program
    will not start

After the program has started open your Eclipse, go to Debug
configrations, Remote Java application, create a new entry and set
"Host" to the machine name or IP and "Port" to 23334 (or whatever other
port you've set up). Connect to it and off you go. The configuration
steps for IntelliJ can be found
[here](http://www.javaranch.com/journal/200408/DebuggingServer-sideCode.html)
(I didn’t check it, but they seem right). A couple of final thoughts:

-   If your sources are not in sync with the remote jars, you will see
    weird stuff (like breakpoints not triggering, triggering and the
    “wrong” line, etc), so you should make sure that you have the same
    sources as the jar does. If you still get into the situation where
    the sources are different from the classfiles, I found that setting
    breakpoints on "method entry" works as expected (ie. it breaks even
    if the method in the classfile is on a different line)
-   You can "detach" from a certain process and it keeps running (and
    later on you can re-attach to it)
-   This method is of low bandwidth / overhead, so it can be used to
    debug servers in remote locations
-   Never, ever do this in production! unless you are absolutely, 100%
    certain that you know what you are doing.

