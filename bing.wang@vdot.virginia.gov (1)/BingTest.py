# Databricks notebook source
# MAGIC %sh
# MAGIC curl https://packages.microsoft.com/keys/microsoft.asc | apt-key add -
# MAGIC curl https://packages.microsoft.com/config/ubuntu/16.04/prod.list > /etc/apt/sources.list.d/mssql-release.list
# MAGIC sudo apt-get update
# MAGIC sudo ACCEPT_EULA=Y apt-get -q -y install msodbcsql17

# COMMAND ----------

import pyodbc

driver= '{ODBC Driver 17 for SQL Server}'
host = 'sql-entlake-prd-01.1246c3081060.database.windows.net'
#host = '10.125.66.254'
database = 'sqldbavlPrd01'
user='bing.wang@vdot.virginia.gov'
password='San22yue'

cnxn = pyodbc.connect('DRIVER='+driver+';SERVER='+host+';PORT=1443;DATABASE='+database+';UID='+user+';PWD='+ password+';timeout=0;sslmode=True;Authentication=ActiveDirectoryPassword')
# cnxn = pyodbc.connect('DRIVER='+driver+';SERVER='+host+';PORT=1443;DATABASE='+database+';UID='+user+';PWD='+ password+';timeout=0;sslmode=True;Authentication=ActiveDirectoryInteractive')

# COMMAND ----------

import pandas as pd
df = pd.read_sql("SELECT top 5 * FROM [sqldbavlPrd01].[AVL].[TruckEvent];", cnxn) 
df.head()

# COMMAND ----------

import bcrypt
password=""
password = password.encode('utf-8')
hashedPassword = bcrypt.hashpw(password, bcrypt.gensalt())
print(hashedPassword)
