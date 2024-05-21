import sys
sys.path.insert(0, "/home/shivam-rana/python/task1_Task_management/")
from dbconnection.dbconnect import connect_db, create_database, create_table
connection = connect_db()
cursor = connection.cursor()



try:
  # creating database
  db_sql = create_database("task_management", cursor)
  if(db_sql):
    print("task_management " + "Database Created")
  else:
    print("failed to create database")
  
  
  # creating table for the task management
  tbl_sql_task = 'tasks'
  tbl_columns = ("id int not null auto_increment primary key", "task_name varchar(255) not null","description varchar(255)", "starttime datetime", "deadline datetime", "priority tinyint", "status varchar(50)", "created_at datetime default now()")


  # use the database 
  db_use = "USE task_management"
  cursor.execute(db_use)


  db_table = create_table(tbl_sql_task, tbl_columns, cursor)
  if(db_table):
    print(tbl_sql_task + " table is created")
  else:
    print("failed to create table")


except connection.error as e:
  print("something went wrong => \n" + e)

