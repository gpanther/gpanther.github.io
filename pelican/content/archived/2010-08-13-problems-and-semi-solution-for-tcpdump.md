Title: Problems (and a semi-solution) for tcpdump with DAG cards
Date: 2010-08-13 04:30
Author: Attila-Mihaly Balazs
Tags: pcap, packet capture, tcpdump, linux, tcp/ip
Slug: problems-and-semi-solution-for-tcpdump
Status: published

Documenting here for posterity, since I didn't find much information
about it on the 'net:

Disclaimer: I'm not a network head, just an amateur who dabbles with it
when he needs to fix a problem.

Given one Ninjabox (the nickname for packet capture boxes from
[Endace](http://www.endace.com/)) with a DAG card (some kind of custom
packet capture network card from the same company), you could get the
following error when trying to use tcpdump on the dag interface:

    tcpdump: dag_attach_stream: Permission denied

</p>
The problem seems to be unrelated to your privilege level (you will get
this even if you are running as root), but rather to the fact that some
other program is/was using the particular interface. You can quickly
check this by doing a `lsof | grep dag0`. In my case it was softflowd.
But even after killing the softflowd process, I was getting the same
error message. I had to reset the card using the following commands:

    /etc/init.d/dag_drivers_load stop
    /etc/init.d/dag_drivers_load start

</p>
After this tcpdump worked like a charm. Hope that this information will
save people from searching around as I had to do.

Off topic minirant: why use custom hardware / software? In my experience
they almost never deliver the performance they promise and are hard to
troubleshoot because of lack of information.
