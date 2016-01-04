Title: On benchmarks
Date: 2014-03-28 09:17
Author: Attila-Mihaly Balazs
Tags: rant, performance
Slug: on-benchmarks
Status: published

Numbers every programmer should know and their impact on benchmarks
-------------------------------------------------------------------

Disclaimer: I don't mean to be picking on the particular organizations /
projects / people who I'll mention below. They are just examples of a
larger trend I observed.

Sometimes (most of the times?) we forget just how powerful the machines
in our pockets / bags / desks are and accept the inefficiencies of the
software running on them. When we start to celebrate those
inefficiencies, a line has to be drawn though. Two examples:

In 2013 Twitter claimed [a record Tweets Per
Second](https://blog.twitter.com/2013/new-tweets-per-second-record-and-how)
(TPS - cute :-)) of \~143k. Lets round that up to 150k and do some
back-of-the envelope calculations:

-   Communication between the clients and Twitter: a tweet is 140 bytes
    (240 if we allow for unicode). Lets multiple the 150k number by 10
    (just to be generous - remember that 143k was already a big blip) -
    we get a bandwidth requirement of 343 MB/sec. Because tweets are
    going over TCP presumably and \~20% of a TCP connection is overhead,
    you would need 428 MB/s of bandwidth, about 3.5 gigabit or less than
    0.5 of a 10 gigabit connection.
-   On the backend: lets assume we want triple redundancy (1 master + 2
    replica) and that the average tweet goes out to 9 subscribers. This
    means that internally we need to write each tweet 30 times (we
    suppose a completely denormalized structure, we need to write the
    tweet to the users timeline also and do all this thrice for
    redundancy). This means 10 GB/sec of data (13 if we're sending it
    over the network using TCP).
-   Thus \~100 servers would be able to easily handle the load. And
    remember this is *10x* of the *peak* traffic they experienced.

So why do the have [20 to 40 times that many
servers](http://www.quora.com/How-many-servers-does-Twitter-have)? This
means that less than 10% (!) of their server capacity is actually used
for business functions.

Second example: Google with DataStax came out with [a
blogpost](http://googlecloudplatform.blogspot.ro/2014/03/cassandra-hits-one-million-writes-per-second-on-google-compute-engine.html)
about benchmarking a 300 node Cassandra cluster on Google Compute
Engine. They claim a peak of 1.2M messages per second. Again, lets do
some calculations:

-   The messages were 170 bytes in size. They were written to 2+1 nodes
    which would mean \~600 MB/s of traffic (730 MB/s if over the network
    using TCP).
-   They used 300 servers but were also testing the resiliency by
    removing 1/3 of the nodes, so lets be generous and say that the
    volume was divided over 100 servers.

This means that per server we use 7.3 MB/s network traffic and 6 MB/s
disk traffic or 6% or a Gigabit connection and about 50% of medium
quality spinning rust HDD.

My challenge to you is: next time you see such benchmarks do a quick
back-of-the envelope calculation and if it uses less than 60% of the
available throughput, call the people on it!
