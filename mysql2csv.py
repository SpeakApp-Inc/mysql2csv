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
@click.option('-t', '--table', default="#000000", help='Table or tables to fetch (for many tables, use commas without spaces, e.g. "table1,table2,table3")', required=False)
def export(hostname,user,password,dbname,table):
  '''Export a database into csv files.'''

  if not password:
    import getpass
    password = getpass.getpass("Enter your password:")

  db=MySQLdb.connect(hostname,user,password,dbname)
  tables=db.cursor()
  tables.execute('SHOW TABLES')

  if not os.path.isdir(dbname):
    os.mkdir(dbname)

  for table in tables:
    print "Converting table %s...." % table
    f=csv.writer(open(os.path.join(dbname,"%s.csv" % table),'w'))
    colunas=db.cursor()
    colunas.execute('DESCRIBE %s' % table)
    f.writerow([i[0] for i in colunas])
    dados=db.cursor()
    dados.execute('SELECT * FROM %s' % table)
    f.writerows(dados)
    f.close()
    
if __name__=="__main__":
  export()

