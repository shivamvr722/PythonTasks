import psycopg2


# forming the connection 
conn = psycopg2.connect( 
  database="task_management", 
  user='postgres', 
  password='Dev@123', 
  host='127.0.0.1', 
  port='5432'
)


# sql = "create database if not exists task_management2"
# sql = "CREATE DATABASE task_management;"

# try:
#   cursor = conn.cursor()
#   cursor.execute(sql)
# except Exception as e:
#   print("something went wrong" + e)