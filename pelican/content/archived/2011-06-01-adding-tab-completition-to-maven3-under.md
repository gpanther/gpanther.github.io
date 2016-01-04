Title: Adding tab completition to Maven3 under Ubuntu
Date: 2011-06-01 20:10
Author: Attila-Mihaly Balazs
Tags: ubuntu, bash, maven, java
Slug: adding-tab-completition-to-maven3-under
Status: published

</p>
Maven 3 was released recently (depending on your definition of recent),
but is not yet packaged for Ubuntu. This is generally not a problem,
since the [installation
instructions](http://maven.apache.org/download.html) are easy to follow
(alternatively
[here](http://www.sonatype.com/books/mvnex-book/reference/installation-sect-maven-install.html#installation-sect-maven-linux)
are the installation instructions from the Sonatype maven book), but you
don’t get tab completion in your terminal, which is quite a bummer,
since I don’t know how to write correctly without a spellchecker.

Fortunately the steps to add it are simple:

-   [Download](http://packages.ubuntu.com/natty/all/maven2/download) an
    older Maven2 package
-   Extract from it the `/etc/bash_completion.d/maven2` file (take care
    *not* to install the package by mistake)
-   Put the extracted file into `/etc/bash_completion.d/maven3`
-   Restart your terminal

These steps should also work with other Linux distributions if they have
[bash-completion](http://bash-completion.alioth.debian.org/) installed.

*This is a cross-post from the [Transylvania-JUG
blog](http://www.transylvania-jug.org/archives/218).*
