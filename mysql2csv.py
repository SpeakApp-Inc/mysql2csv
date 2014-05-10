#!/usr/bin/env python
'''Mysql database to csv exporter'''

import sys, os, datetime
import MySQLdb
import csv
import click

@click.command()
@click.option('-h', '--hostname', default="127.0.0.1", help='Hostname')
@click.option('-u', '--user', help='MySQL username', required=True)
@click.option('-p', '--password', default="", help='MySQL password', required=True)
@click.option('-d', '--dbname', help='Database name', required=True)
@click.option('-t', '--table', help='Table or tables to fetch (for many tables, use commas without spaces, e.g. "table1,table2,table3")', required=False)
def export(hostname, user, password, dbname, table):
    '''Export a database into csv files.'''
  
    # prompt for password if not specified
    if not password:
        import getpass
        password = getpass.getpass("Enter your password:")
    
    # create the dir to place the CSV files in
    if not os.path.isdir(dbname):
        os.mkdir(dbname)

    # connect to the database
    db = MySQLdb.connect(hostname, user, password, dbname)

    # check if table argument was specified
    if table:
        if len(table.split(',')) == 1:
            # only one table to fetch
            tables = [table]
        else:
            # multiple tables requested, make the tables list and go on
            tables = table.split(",")
    else:
        # get all tables
        tables = db.cursor()
        tables.execute('SHOW TABLES')

    for table in tables:
        print "Converting table %s...." % table
        f = csv.writer(open(os.path.join(dbname, "%s.csv" % table),'w'))
        colnames = db.cursor()
        colnames.execute('DESCRIBE %s' % table)
        f.writerow([i[0] for i in colnames])
        rows = db.cursor()
        rows.execute('SELECT * FROM %s' % table)
        f.writerows(rows)
    
if __name__=="__main__":
    export()

