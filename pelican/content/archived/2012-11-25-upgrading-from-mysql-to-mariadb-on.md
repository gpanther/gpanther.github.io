Title: Upgrading from MySQL to MariaDB on Ubuntu
Date: 2012-11-25 11:14
Author: Attila-Mihaly Balazs
Tags: database, mysql, ubuntu, mariadb
Slug: upgrading-from-mysql-to-mariadb-on
Status: published

So you decided that Oracle doesn't know its left foot from the back of
his neck when it comes to open source (how's that for a mixed metaphor),
but you are not ready just yet to migrate over to PostgreSQL? Consider
[MariaDB](https://en.wikipedia.org/wiki/MariaDB). Coming from Monty
Widenius, the original author of MySQL, it aims to be 100% MySQL
compatible while also being truly open-source.

Give that it's 100% MySQL compatible, you can update in-place
(nevertheless it is recommended that do a backup of your data first).
The steps are roughly adapted from
[here](http://www.sagetree.com/sage-advice/christoph-weber/replace-mysql-mariadb-ubuntu-1204-lts).

1.  Go to the [MariaDB repository configuration
    tool](https://downloads.mariadb.org/mariadb/repositories/) and
    generate your .list file (wondering what's up with the 5.5 vs 10.0
    version? See [this short
    explanation](https://en.wikipedia.org/wiki/MariaDB#Versioning)). You
    don't know the exact Ubuntu version you're running? Just use
    `lsb_release -a`.
2.  Save the generated file under `/etc/apt/sources.list.d/MariaDB.list`
    as recommended and do an `sudo aptitude update`. You should see an
    output complaining about some public keys.
3.  Do
    `sudo apt-key adv --recv-keys --keyserver keyserver.ubuntu.com 0xCBCB082A1BB943DB`
    to add those keys (replace the last number with the one you saw in
    the previous output).
4.  Issue `sudo apt-cache policy mysql-common` and you should see
    mariadb as an upgrade option.
5.  Finally do `sudo aptitude upgrade mysql-common libmysqlclient18` and
    watch your MySQL database being transformed into a MariaDB one and
    all keeping chugging along just as usual!

