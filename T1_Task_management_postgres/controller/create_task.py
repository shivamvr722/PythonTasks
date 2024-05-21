import sys
sys.path.insert(0, "/home/shivam-rana/python/T1_Task_management/")
from dbconnection.dbconnect import create_connection
from datetime import datetime


connection = create_connection()
cursor = connection.cursor()
date_formate = "%Y-%m-%d %H:%M"

def insert_tasks():

  def insert_task(*args):
    task_sql  = "INSERT INTO tasks(task_name, description, starttime, deadline, priority, status) VALUES(%s, %s, %s, %s, %s, %s)"
    cursor.execute(task_sql, args)
    connection.commit()
    if(cursor.rowcount):
      return cursor.rowcount
    else:
      return False

  add_one = True
  while add_one:
    #create the task 
    task = input("Taks Name: ").strip(" ")  
    description = input("Task Desciption : ")
    starttime = input("Task Start Time (YYYY-MM-DD HH:MM): ").strip(" ")
    deadline = input("Task Deadline (YYYY-MM-DD HH:MM): ").strip(" ")

    try:
      sdate = datetime.strptime(starttime, date_formate)
      ddate = datetime.strptime(deadline, date_formate)
      if sdate >= ddate:
        print("\nDeadline can not be small then Startime!!!\n")
        break

    except ValueError as v:
      print("\nenter valid date as per formate!!!\n")
      break
      # starttime = input("Task Start Time (YYYY-MM-DD hh:mm:ss): ")

    try:
      priorities = (1,2,3)
      priority = int(input("Task Priority from (high=1, medium=2, low=3)(1,2 or 3): "))
      if(priority not in priorities):
        print("\nChoose Priority from 1,2,3 only!!\n")
        break
    except Exception as e:
      print("\nEnter The Numeric Value only from 1,2 or 3 allowed!!!\n")

    status = input("Task Status from (pending, assinged or finished): ").strip(" ")
    statuses = ("pending", "assinged", "finished")
    if(status not in statuses):
      print("\nselect statuses from the (pending, assinged or finished only)!!!\n")
      break


    # calling function to insert the record into the database
    insert = insert_task(task, description, starttime, deadline, priority, status)

    # recored insertion error
    if(insert):
      print(f"\nRecord Added Successfully!\n")
    else:
      print("\nsomething went wrong while inserting the record!!\n")
      break

    # ask the user to add more tasks
    taskA = input("\nDo you want to add more ? Y/N:").lower()
    if(taskA == "n"):
      add_one = False
  