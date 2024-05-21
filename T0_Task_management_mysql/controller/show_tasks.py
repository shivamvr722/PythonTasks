import sys
sys.path.insert(0, "/home/shivam-rana/python/task1_Task_management/")

from dbconnection.dbconnect import connect_database

# creating the connection object
connection = connect_database("task_management")
cursor = connection.cursor()



def show_tasks_result():
  
  def query_creator(table):
    sql = f"SELECT * FROM {table}"
    return sql


  def show_results():
    sql = query_creator("tasks")

    cursor.execute(sql)
    results = cursor.fetchall()

    for result in results:
      for i in range(len(result)):
        print(result[i], end=" ")
      print()

  show_results()


  