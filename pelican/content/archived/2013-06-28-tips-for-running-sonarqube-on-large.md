Title: Tips for running SonarQube on large / legacy codebases
Date: 2013-06-28 12:49
Author: Attila-Mihaly Balazs
Tags: sonarqube, sonar, java
Slug: tips-for-running-sonarqube-on-large
Status: published

*Crossposted from [the Transylvania JUG
website](http://www.transylvania-jug.org/archives/5702).*

[SonarQube](http://www.sonarqube.org/) (previously Sonar) is a quality
management platform aimed mainly at Java (although other programming
languages are supported to a varying degree. Here are a couple of tips
to get it working on legacy projects:

-   There is an [Ant
    runner](http://docs.codehaus.org/display/SONAR/Analyzing+with+SonarQube+Ant+Task)
    and a [standalone
    runner](http://docs.codehaus.org/display/SONAR/Analyzing+with+SonarQube+Runner),
    it is not mandatory to use Maven (although it is a good idea in
    general to use it)
-   Look into [the analysis
    parameters](http://docs.codehaus.org/display/SONAR/Analysis+Parameters)
    to customize it for your code.
-   Give it space and time :-). For reference a \~2 million LOC Java
    project took 77 minutes to be analyzed on my laptop (an Intel i7)
    with 4G heap.
-   To avoid having a ton of problems reported and to focus only on new
    problems, look into [the Cutoff
    plugin](http://docs.codehaus.org/display/SONAR/Cutoff+Plugin)
-   Test and coverage reports can be reused, no need to run them twice
    (once for the CI system and then for SonarQube). Look into [reusing
    existing
    reports](http://docs.codehaus.org/display/SONAR/Code+Coverage+by+Unit+Tests+for+Java+Project).
    Also, make sure to use the latest version of JaCoCo when generating
    profile data.
-   Configure your sonar.exclusions property to ignore code you aren't
    interested in
-   Raise your sonar.findbugs.timeout property (the default of 5 minutes
    can be low for large projects)
-   Consider disabling source code related plugins (sonar.scm.enabled,
    sonar.scm-stats.enabled) if the provider for your SCM has an issue
    (HG has an issue currently for example with username containing
    spaces)

Keep your code clean!
