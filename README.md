# UpGrad-Python

# Database
  -- PostgreSQL
  -- db_name : upgrad_db
  -- myusername : tkalani
  -- mypassword : tkalani

# Requirements
  -- Python 3
  -- PostgreSQL
  
  -- run
      -- pip install psycopg2
# Mac-OS Commmands to run:
  -- $ createdb db_name
       (or $ sudo -u postgres createdb upgrad_db)
       
  -- CREATE ROLE myusername WITH LOGIN PASSWORD 'mypassword';
  -- GRANT ALL PRIVILEGES ON DATABASE db_name TO myusername;
  -- ALTER USER myusername CREATEDB;
