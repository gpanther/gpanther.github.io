Title: Sending an X-Face email with Perl+GMail
Date: 2010-04-02 16:17
Author: Attila-Mihaly Balazs
Tags: email, programming, perl, google
Slug: sending-x-face-email-with-perlgmail
Status: published

In the [latest Software Freedom Law
Show](http://www.softwarefreedom.org/podcast/2010/mar/30/0x24/) Bradley
mentioned the [X-Face](http://en.wikipedia.org/wiki/X-Face) email header
and challenged listeners to send them an email containing the X-Face
header. So here is the small Perl script I’ve whipped together to send
them an email trough GMail:

    use strict;
    use warnings;
    use Net::SMTP::TLS;

    my ($from, $password) = ('...@gmail.com', 'MySuperSecretPassword');
    my $mailer = new Net::SMTP::TLS(
      'smtp.gmail.com',
      Hello => 'smtp.gmail.com',
      Port => 587,
      User => $from,
      Password => $password);

    $mailer->mail($from);
    $mailer->to('foo@example.com');

    my $data = <<'EOF';
    X-Face: "8.]Z_3ptu\NK'CA~DM>M,G.T(h=1.y9"0gXW3V91E:dw2?|&G2R(?/no'F2g4%8Fv.
     J1p5K-^1epKXxIG)mj4}nGWTi<=iz8n)bUVhLu}MXRFl9"J%'=-;IfMXcuPK>-%^;$uW87O/B
    Subject: Hello X-Faced World!

    email body.
    EOF

    $mailer->data();
    $mailer->datasend($data);
    $mailer->dataend();
    $mailer->quit();

</code>

The code is largely based on this snippet: [Sending Mail Through Gmail
with
Perl](http://www.nixtutor.com/linux/sending-mail-through-gmail-with-perl/).
The X-Face header was generated using the [Online X-Face
Converter](http://www.dairiki.org/xface/xface.php) (yes, I know that
there is a
[Image::XFace](http://search.cpan.org/~cwrl/Image-XFace-0.1/XFace.pm)
module, but it was very cryptic – it didn’t mention supported input /
output formats). One word of warning: if you are using ActivePerl under
Windows, Net::SMTP::TLS isn’t available in the default module list
(AFAIK, because of encryption restrictions), so you might need to
experiment with [alternative package
sources](http://hype-free.blogspot.com/2006/12/perl-and-windows.html) or
using Linux :-). I’ve also tested the script with an email account I
control (using Thunderbird with the
[Mnenhy](http://mnenhy.mozdev.org/customheaders.html) plugin – which can
read but not create X-Face emails) and it worked nicely.

There you have it: how to use an old (from the 1980s according to
Wikipedia) method for embedding pictures which is not supported by most
of the email clients :-)

</code>
