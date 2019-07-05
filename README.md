mysql2csv
=========

Simple command line tool to convert some or all tables in a MySQL database into CSV files.

Usage
-----

```
# python mysql2csv --help
Usage: mysql2csv [OPTIONS]

  Export some or all tables in a MySQL database into CSV files.
  Exported files names will follow this convention: YYYY-MM-DD_tablename.csv

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
  -n, --filename=NAME   Set exported csv filename. If ommited, will use 'query'
  -q, --query=QUERY     Executes a custom SQL query.
  --help                Show this message and exit.

Examples:
./mysql2csv -h db.conversifi.com -u conversifi -p <password> -d conversifi_etl -q "CALL sp_summary('5b902402c33f1bfa7e112376');" -n sp_summary
will create a file named *2019-07-05_sp_summary.csv* inside a folder *conversifi_etl*.

./mysql2csv -h db.conversifi.com -u conversifi -p <password> -d conversifi_etl -q "SELECT * FROM users"
will create a file named *2019-07-05_query.csv* inside a folder *conversifi_etl*.

./mysql2csv -h db.conversifi.com -u conversifi -p <password> -d conversifi_etl -t users
will create a file named *2019-07-05_users.csv* inside a folder *conversifi_etl*.
```