Title: Integrating Maven with Ivy
Date: 2011-10-11 11:18
Author: Attila-Mihaly Balazs
Tags: dependency management, ivy, maven, java
Slug: integrating-maven-with-ivy
Status: published

*This post was originally published on the [Transylvania JUG
blog](http://www.transylvania-jug.org/archives/272).*

The problem: you have some resources in an Ivy repository (and only
there) which you would like to use in a project based on Maven. Possible
solutions:

-   Migrate the repository to Maven (Nexus for example) since Ivy can
    easily use Maven-style repositories (so your Ivy clients can
    continue to use Ivy with some slight configuration changes and Maven
    clients will also work – also the push-to-repo process needs to be
    changed)
-   Try JFrog Artifactory since it [reportedly can serve the same
    resources to both Ivy and
    Maven](http://blogs.jfrog.org/2010/03/building-enterprise-repository-with.html)
    (disclaimer: I haven’t tried to use it actually and I don’t know if
    the Open Source version includes this feature or not)
-   or read on…

My goal for the solution (as complex as it may be) was:

-   It should be as simple and self-explanatory as possible
-   It should respect the DRY principle (Don’t Repeat Yourself)
-   It shouldn’t have other dependencies than Maven itself

The solution looks like the following (for the full source check out
[the
code-repo](http://code.google.com/p/hype-free/source/browse/trunk/java-maven-ivy/pom.xml)):

Have two Maven profiles: `ivy-dependencies` activates when the
dependencies have already been downloaded and `ivy-resolve` when there
are yet to download. This is based on checking the directory where the
dependencies are to be copied ultimately:

    ...
    ivy-dependencies

    false

    ${basedir}/ivy-lib


    ...
    ivy-resolve

    false

    ${basedir}/ivy-lib


    ...

Unfortunately there is a small repetition here, since Maven doesn’t seem
to expand user-defined properties like `${ivy.target.lib.dir}` in the
profile activation section. The profiles also serve an other role: to
avoid the consideration of the dependencies until they are actually
resolved.

When the build is first run, it creates the target directory, writes the
files needed for an Ivy build there (`ivy.xml`, `ivysettings.xml` and
`build.xml` – for this example I’ve used some parts from corresponding
files of [the Red5
repo](http://code.google.com/p/red5/source/browse/java/server/trunk/)),
runs the build and tries to clean up after itself. It also creates
a`dependencies.txt` file containing the chunck of text which needs to be
added to the dependencies list. Finally, it bails out (fails)
instructing the user to run the command again.

On the second (third, fourth, etc) run the dependencies will already be
present, so the resolution process won’t be run repeteadly. This
approach was chosen instead of running the resolution at every build
because – even though the resolution process is quick quick – it can
take tens seconds in some more complicated cases and I didn’t want to
slow the build down.

And, Ivy, the Apache BSF framework, etc are fetched from the Maven
central repository, so they need not be preinstalled for build to
complete successfully.

A couple of words about choosing `${ivy.target.lib.dir}`: if you choose
it inside your Maven tree (like it was chose in the example), you will
receive warnings from Maven that this might not be supported in the
future. Also, be sure to add the directory to the ignore mechanism of
your VCS (`.gitignore`, `.hgignore`, `.cvsignore`, `svn:ignore`, etc),
as to avoid accidentally committing the libraries to VCS.

If you need to add a new (Ivy) dependency to the project, the steps are
as follows:

-   Delete the current `${ivy.target.lib.dir}` directory
-   Update the part of your `pom.xml` which writes out the `ivy.xml`
    file to include the new dependency
-   Run a build and watch the new dependency being resolved
-   Update the dependencies section of the `ivy-dependencies` profile to
    include the new dependency (possibly copying from
    `dependencies.txt`)

One drawback of this method is the fact that advanced functionalities of
systems based on Maven will not work with these dependencies (for
example dependency analisys / graphing plugins, automated downloading of
sources / javadocs, etc). A possible workaround (and a good idea in
general) is to use this method for the minimal subset – just the jars
which can’t be found in Maven central. All the rests (even if they are
actually dependencies of the code fetched from Ivy) should be declared
as a normal dependency, to be fetched from the Maven repository.

Finally I would like to say that this endeavour once again showed me how
flexible both Maven and Ivy/Ant can be and clarified many cornercases
(like how we escape `]]` inside of CDATA – we split it in two). And it
can also be further tweaked (for example: adding a clean target to the
ivy-resolve profile, so you can remove the directory with
`mvn clean -P ivy-resolve` or re-jar-ing all the downloaded jars into a
single one for example [like
this](http://stackoverflow.com/questions/1821803/creating-a-bundle-jar-with-ant),
thus avoiding the need to modify the pom file every time the list of Ivy
dependencies gets changed – then again signed JARs can’t be re-jarred so
it is not an universal solution either).
