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
  -t TABLE, --table=TABLE
                        Table or tables to fetch (for more than one, use
                        commas without spaces, e.g. "table1,table2,table3")
  -l, --list-only       List database tables and exit.
  -n, --filename=NAME   Set exported csv filename. If ommited, will use 'query'
  -q, --query=QUERY     Executes a custom SQL query.
  --help                Show this message and exit.

Examples:
./mysql2csv -q "CALL sp_summary('5b902402c33f1bfa7e112376');" -n sp_summary
will create a file named *2019-07-05_sp_summary.csv* inside a folder *conversifi_etl*.

./mysql2csv -q "SELECT * FROM users"
will create a file named *2019-07-05_query.csv* inside a folder *conversifi_etl*.

./mysql2csv -t users
will create a file named *2019-07-05_users.csv* inside a folder *conversifi_etl*.
```

Configuration
-------------

Copy *.env.example* to *.env* and edit the file to suit your setup
```
mysql_host=mysql          #Database host name
mysql_port=3306           #Database host port
mysql_db=conversifi_etl   #Database name
mysql_user=root           #MySQL username
mysql_pass=root           #MySQL password
gdrive_folder_id=1bfhQ5TZm54CaVOBK1eYuOs_wgp2KttoO
```

Get _credentials.json_ from Google Developer Console https://console.developers.google.com/apis/ logged in as the destination drive owner
- create project
- add GDrive API Library
- generate OAuth 2.0 client id, kind: Other, then download as JSON

Get *gdrive_folder_id* from google drive destination folder share link.

Run once without parameters to generate _token.pickle_ by login in via webpage.
Subsequent execution will not require interactive login.

