Title: Updating the root certificates for Java
Date: 2011-10-20 15:36
Author: Attila-Mihaly Balazs
Tags: ssl, java
Slug: updating-root-certificates-for-java
Status: published

One usually thinks of SSL in the context of HTTPS, but there are also
other protocols which rely on it to provide security. See [this
link](http://www.google.com/url?q=https%3A%2F%2Fssl.trustwave.com%2Fsupport%2Fsupport-how-ssl-works.php&sa=D&sntz=1&usg=AFrqEzcSKxikCOveGBqInQtKlIeQDxQh1A)
for a short overview of SSL – it only mentions HTTPS, but the same
applies for IMAPS, FTPS, etc – SSL is independent of the wrapped
protocol. You can have issues with your Java programs in where the party
you are communicating with provider changes their certificate and the
program rejects it as invalid. The exception is something like:

    javax.net.ssl.SSLHandshakeException: sun.security.validator.ValidatorException: 
        PKIX path building failed: sun.security.provider.certpath.SunCertPathBuilderException: 
        unable to find valid certification path to requested target

One cause of the problem can be that the server uses an SSL provider
which is based on a root certificate that wasn’t included with the
particular version of Java you are using (this is especially true for
really old versions like Java 1.5). The issue can be solved by updating
to the latest version, but it might be that this isn't an option.
Fortunately I found the following article: [No more ‘unable to find
valid certification path to requested
target’](http://www.google.com/url?q=http%3A%2F%2Fblogs.sun.com%2Fandreas%2Fentry%2Fno_more_unable_to_find&sa=D&sntz=1&usg=AFrqEzeLX1QgwCxBswOU7p3Y6eb8qpF_0g)

How to use it:

-   Compile the program `javac InstallCert.java`
-   Run it with the target host/port. For example in our case it would
    be: `java InstallCert imap.mailprovider.com:993` (993 is the port
    for IMAPS)
-   navigate trough the menus and select which certificate to import
-   now you have a file called `jssecacerts`. You need to copy this to
    `$JAVA_HOME/jre/lib/security/cacerts` (**back up the existing file
    first!**)
-   Now the root certificate is imported (you can confirm this by
    rerunning InstallCert)

HTH
