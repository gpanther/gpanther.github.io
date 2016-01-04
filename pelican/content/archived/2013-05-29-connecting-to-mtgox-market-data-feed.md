Title: Connecting to the MtGox market data feed using Perl
Date: 2013-05-29 17:52
Author: Attila-Mihaly Balazs
Tags: bitcoin, websockets, perl, mtgox
Slug: connecting-to-mtgox-market-data-feed
Status: published

For a recent project I needed some realistic market data for an
electronic exchange. Seeing how MtGox provides free and open access to
theirs (thank you!) I chose them. However none of the examples floating
around the internet seemed to work, so I whipped one up using
[Net::Async::WebSocket::Client](http://search.cpan.org/~pevans/Net-Async-WebSocket-0.06/lib/Net/Async/WebSocket/Client.pm).
Enjoy:

    use IO::Async::Loop;
    use Net::Async::WebSocket::Client;

    my $client = Net::Async::WebSocket::Client->new(
            on_frame => sub {
                    my ( $self, $frame ) = @_;
                    print "\n", $frame, "\n";
            },
    );

    my $loop = IO::Async::Loop->new;
    $loop->add( $client );

    $client->connect(
            host => 'websocket.mtgox.com',
            service => 80,
            url => "ws://websocket.mtgox.com:80/mtgox",
            on_connected => sub {},
            on_connect_error => sub { die "Cannot connect - $_[-1]" },
            on_resolve_error => sub { die "Cannot resolve - $_[-1]" },
    );

    $loop->loop_forever;

</code>

(it is basically the sample program for the module, with the MtGox
market data URL hardcoded).
