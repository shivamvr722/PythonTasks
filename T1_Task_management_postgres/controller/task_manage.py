import sys
sys.path.insert(0, "/home/shivam-rana/python/T1_Task_management/")
from dbconnection.dbconnect import create_connection
connection = create_connection()
cursor = connection.cursor()

try:
    # creating table for the task management
    table_task = """
    create table tasks(
    id SERIAL PRIMARY KEY,
    task_name varchar(50) not null,
    description text, 
    starttime date,
    deadline date, 
    priority int,
    status varchar(50))"""

    cursor.execute(table_task)
    connection.commit()
    
except cursor.error as e:
    print("something went wrong => \n" + e)

