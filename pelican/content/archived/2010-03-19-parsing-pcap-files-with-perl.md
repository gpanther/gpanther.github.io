Title: Parsing pcap files with Perl
Date: 2010-03-19 15:43
Author: Attila-Mihaly Balazs
Tags: rant, programming, perl, networking
Slug: parsing-pcap-files-with-perl
Status: published

![4175923040\_b41d970b17\_b](http://lh3.ggpht.com/_hrvCBhtWhJ4/S6N_aa3qYlI/AAAAAAAACPA/eFZ137Rrdmc/4175923040_b41d970b17_b%5B8%5D.jpg?imgmax=800 "4175923040_b41d970b17_b")
Recently I was reading the blogpost on the BrekingPoint labs log about
[parsing pcap files with
Perl](http://www.breakingpointsystems.com/community/blog/pcap-file-wireshark)
and I immediately said to myself: it is impossible that there isn’t a
module on CPAN, because [Perl is
great](http://hype-free.blogspot.com/2010/03/in-praise-of-regexpassemble.html).
Turns out I was right, there is
[Net::TcpDumpLog](http://search.cpan.org/~bdgregg/Net-TcpDumpLog-0.11/TcpDumpLog.pm)
which can be combined with the
[NetPacket](http://search.cpan.org/~yanick/NetPacket-1.1.1/lib/NetPacket.pm)
family of modules to parse the higher level protocols. Because example
code is rather sparse on the POD pages of the respective modules, here
is a small example to illustrate their use:

    use Net::TcpDumpLog;
    use NetPacket::Ethernet;
    use NetPacket::IP;
    use NetPacket::TCP;
    use strict;
    use warnings;

    my $log = Net::TcpDumpLog->new(); 
    $log->read("foo.pcap");

    foreach my $index ($log->indexes) { 
      my ($length_orig, $length_incl, $drops, $secs, $msecs) = $log->header($index); 
      my $data = $log->data($index);
      
      my $eth_obj = NetPacket::Ethernet->decode($data);    
      next unless $eth_obj->{type} == NetPacket::Ethernet::ETH_TYPE_IP;

      my $ip_obj = NetPacket::IP->decode($eth_obj->{data});
      next unless $ip_obj->{proto} == NetPacket::IP::IP_PROTO_TCP;

      my $tcp_obj = NetPacket::TCP->decode($ip_obj->{data});
      my ($sec,$min,$hour,$mday,$mon,$year,$wday,$yday,$isdst) = localtime($secs + $msecs/1000);
      print sprintf("%02d-%02d %02d:%02d:%02d.%d", 
        $mon, $mday, $hour, $min, $sec, $msecs), 
        " ", $eth_obj->{src_mac}, " -> ", 
        $eth_obj->{dest_mac}, "\n";    
      print "\t", $ip_obj->{src_ip}, ":", $tcp_obj->{src_port}, 
        " -> ", 
        $ip_obj->{dest_ip}, ":", $tcp_obj->{dest_port}, "\n";
    }

The code does the following: it opens the pcap file named “foo.pcap”,
iterates over all the packets (it assumes that they all are Ethernet
packets) and looks for TCP packets. Finally it prints out some
information about these packets (capture time, source/destination mac,
source/destination ip:port). You can customize it to fit your needs.

*Small, somewhat offtopic rant*: one should always think *at least*
twice before publishing code which does such elementary things. Find a
library and use it. If it doesn’t work, try patching it so that it works
and send back the code to the original author. Only if this fails should
you start from scratch.

Reusing existing code has many advantages: from your point of view, you
can be sure that you can get code which worked for a couple of people.
This is especially true for Perl modules which have a strong culture of
testing. Also, even these “simple” problems like parsing a TCP packet
have many corner cases which you will almost certainly miss at the first
go, and as a result, half of your time will be spent hunting them down
and only half of your time will be dedicated to solving the actual
problem (this is if you are lucky – if you are unlucky, your code will
skip over the special cases and it may make your entire analysis
irrelevant).

Looking at it from the other side we have: more concentration of the way
to do “X” means that the code will be more tested, leading it to be used
more, meaning that it will be better tested and thus creating a positive
feedback loop. Also, if you believe in the open-source ethos (and
supposedly you do, since you published your code in the first place),
you should consider maximizing the return while minimizing the effort
needed.

Picture taken from [greyloch's
photostream](http://www.flickr.com/photos/greyloch/) with permission.

*Update*: updated NetPacket link - thank you Anonymous.
