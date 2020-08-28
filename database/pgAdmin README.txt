#Steps to install and configure pgAdmin4

1 - Update the system
	
  $ sudo apt-get update
	
2 - Install required packages

  $ sudo apt-get install build-essential libssl-dev libffi-dev libgmp3-dev virtualenv python-pip libpq-dev python-dev
	
3 - Create virtual environment

  $ mkdir pgAdmin4
  $ cd pgAdmin4
  $ virtualenv pgAdmin4

4 - Activate virtual environment

 $ cd pgAdmin4
 $ source bin/activate
 
5 - Download pgAdmin 4

  $ wget https://ftp.postgresql.org/pub/pgadmin/pgadmin4/v4.25/pip/pgadmin4-4.25-py3-none-any.whl
  
6 - Install pgAdmin 4

  $ pip3 install pgadmin4-4.25.py3-none-any.whl
  
7 - Configure and run pgAdmin 4

  $ nano lib/python3.8/site-packages/pgadmin4/config_local.py
  
8 - Add the following content in config_local.py.

  import os
  DATA_DIR = os.path.realpath(os.path.expanduser(u'~/.pgadmin/'))
  LOG_FILE = os.path.join(DATA_DIR, 'pgadmin4.log')
  SQLITE_PATH = os.path.join(DATA_DIR, 'pgadmin4.db')
  SESSION_DB_PATH = os.path.join(DATA_DIR, 'sessions')
  STORAGE_DIR = os.path.join(DATA_DIR, 'storage')
  SERVER_MODE = False
  
9 - Run pgAdmin4 
  
  $ python3 lib/python3.8/site-packages/pgadmin4/pgAdmin4.py

  Note: If any flask-htmlmin module error appears then run the following commands to install the module and then run the server.
  
  $ pip3 install flask-htmlmin
  $ python3 lib/python3.8/site-packages/pgadmin4/pgAdmin4.py
  
10 - Using pgAdmin4

  Before using pgAdmin, you need to confirm that the latest version of PostgreSQL is installed on your operating system. Run the following command to install postgres package for PostgreSQL and contrib package for taking additional functionalities related to PostgreSQL.
  
  $ sudo apt-get install postgresql postgresql-contrib
  $ sudo -u postgres psql postgres
  $ \password postgres
  
PostgreSQL is now ready to use. Go to the pgAdmin browser and click on the ‘Add New Server’ option.

There are four tabs in ‘Creat-Server’ dialog box. In General tab, type the name for the new server. Here, ‘TestDB’ is set as server name. Setting background and foreground colors are optional. Make Connect now option checked.

Click on the Connection tab and type Host name/address. Here, localhost is used as host name. By default port is 5432 and keep it unchanged now. postgres is set as maintenance database by default. Default username of this database is also set as postgres which is created earlier. Type the password for postgres user that you have created before. Make Save password option on. The other two tabs of this dialog box, SSL and Advanced are used for advanced setting which are omitted in this tutorial. Click on the Save button to create the TestDB server.

When you expand TestDB server, the following screen will appear. Three sections will appear in the left side of the browser. These are Databases, Login/Group Roles and Tablespaces.

There is only one database exists named postgres in Databases part. If you want then you can  create new database from this section and after creation the database will be added in this section.
  
  
  
