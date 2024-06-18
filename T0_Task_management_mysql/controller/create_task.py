import sys
sys.path.insert(0, "/home/shivam-rana/python/task1_Task_management/")
from dbconnection.dbconnect import connect_database
from datetime import datetime


connection  = connect_database("task_management")
cursor = connection.cursor()
date_formate = "%Y-%m-%d %H:%M:%S"

def insert_tasks():


  def insert_task(*args):
    task_sql  = "INSERT INTO tasks(task_name, description, starttime, deadline, priority, status) VALUES(%s, %s, %s, %s, %s, %s)"
    cursor.execute(task_sql, args)
    connection.commit()
    if(cursor.lastrowid):
      return cursor.lastrowid
    else:
      return False



  add_one = True
  while add_one:
    #create the task 
    task = input("Taks Name: ").strip(" ")
    description = input("Task Desciption: ")
    starttime = input("Task Start Time (YYYY-MM-DD hh:mm:ss): ").strip(" ")
    deadline = input("Task Deadline (YYYY-MM-DD hh:mm:ss): ").strip(" ")

    try:
      sdate = datetime.strptime(starttime, date_formate)
      ddate = datetime.strptime(deadline, date_formate)
      if sdate >= ddate:
        print("Deadline can not be small then Startime!!!")
        break

    except ValueError as v:
      print("enter valid date as per formate!!!")
      break
      # starttime = input("Task Start Time (YYYY-MM-DD hh:mm:ss): ")


    priority = int(input("Task Priority: "))
    status = input("Task Status: ").strip(" ")

    # statuses = ("pending", "assinged", "working in progress", "finished")

    # calling function to insert the record into the database
    insert = insert_task(task, description, starttime, deadline, priority, status)

    # recored insertion error
    if(insert):
      print(f"Record Added Successfully! id:{insert}")
    else:
      print("something went wrong while inserting the record!!")
      break

    # ask the user to add more tasks
    taskA = input("Do you want to add more ? Y/N:").lower()
    if(taskA == "n"):
      add_one = False
  