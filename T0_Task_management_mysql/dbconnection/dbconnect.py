import mysql.connector 

def connect_db():    
  return mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "Dev@123",
  )


def connect_database(dbname):
  if(not dbname):
    return "Please provide database name"
  return mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "Dev@123",
    database = dbname
  )




def create_database(database_name, connection_object):
  try:
    sql_db = f"CREATE DATABASE IF NOT EXISTS {database_name}"
    connection_object.execute(sql_db)
    return True
  except:
    return False



def create_table(table_name, column, cursor_con_object):
  col = ""
  if(len(column)):
    s1 = f"CREATE TABLE IF NOT EXISTS {table_name} ("
    for c in column:
      col += f"{c},"
    endB = ")"
  col = col.rstrip(",")
  sql = s1 + col + endB

  try:
    cursor_con_object.execute(sql)
    return True
  except cursor_con_object.error as e:
    print(e)
    return False
# table_creator ends

