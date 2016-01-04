Title: Running JRuby on 64 bit Windows
Date: 2011-09-13 19:33
Author: Attila-Mihaly Balazs
Tags: ruby, windows, jruby, 64bit, java
Slug: running-jruby-on-64-bit-windows
Status: published

Usually it is as simple as: download, install, run. You can run into
problems however if you have both the 32 bit and 64 bit JVMs installed
(which is quite often) because it will try to use the 32 bit JVM. You
can check which JVM is being used from the command line:

    jruby --version
    jruby 1.6.3 (ruby-1.8.7-p330) (2011-07-07 965162f) (Java HotSpot(TM) 64-Bit Server VM 1.7.0) [Windows 7-amd64-java] # 64 bit
    jruby 1.6.3 (ruby-1.8.7-p330) (2011-07-07 965162f) (Java HotSpot(TM) Client VM 1.6.0_26) [Windows 7-x86-java] # 32 bit

</code>

To work around this issue, specify the JVM to use in your jruby.bat (or
other batch files installed by gems like vagrant.bat) explicitly.
Example jruby.bat:

    @ECHO OFF
    java -Djruby.home=C:\jruby-1.6.3 -jar  -jar "C:\jruby-1.6.3\lib\jruby.jar" %1 %2 %3 %4 %5 %6 %7 %8 %9

</code>

Example vagrant.bat

    @ECHO OFF
    java -Djruby.home=C:\jruby-1.6.3 -jar "C:\jruby-1.6.3\lib\jruby.jar" "C:/jruby-1.6.3/bin/vagrant" %1 %2 %3 %4 %5 %6 %7 %8 %9

</code>
