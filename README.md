mysql2csv
=========

Simple command line tool to convert some or all tables in a MySQL database into CSV files.

Usage
-----

```
# python mysql2csv.py --help
Usage: mysql2csv.py [OPTIONS]

  Export some or all tables in a MySQL database into CSV files.

Options:
  -h HOSTNAME, --hostname=HOSTNAME
                        Database host name
  -u USER, --user=USER  MySQL username  [required]
  -p PASSWORD, --password=PASSWORD
                        MySQL password  [required]
  -d DBNAME, --dbname=DBNAME
                        Database name  [required]
  -t TABLE, --table=TABLE
                        Table or tables to fetch (for more than one, use
                        commas without spaces, e.g. "table1,table2,table3")
  -l, --list-only       List database tables and exit.
  --help                Show this message and exit.
```

