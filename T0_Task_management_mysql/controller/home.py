import sys
sys.path.insert(0, "/home/shivam-rana/python/task1_Task_management/")

from dbconnection.dbconnect import connect_database

from create_task import insert_tasks
from show_tasks import show_tasks_result
print("\033[0;32;40m\n")


connection = connect_database("task_management")
cursor = connection.cursor()


def create_task():
  insert_tasks()

def show_tasks():
  print("\n\n")
  show_tasks_result()
  print("\n\n")

def delete_task():
  pass
def update_task():
  pass


print("WELCOME TO THE TASK MANAGEMENT GRID")
print("WE WOULD LOVE TO MANAGE YOUT TASK\n\n\n")

show_task = True
while show_task:
  print("SELECT OPTION YOU WANT TO DO\n")
  print("1. Create Task\n2. Show Tasks\n3. Update Tasks\n4. Delete Task")

  select_operation = input("\nSelect Task Operation: ")

  if select_operation == "1":
    create_task()
  elif select_operation == "2":
    show_tasks()
  elif select_operation == "3":
    update_task()
  elif select_operation == "4":
    delete_task()
  else:
    # print("\033[0;32;40m\n")
    print("\n !!!!! Enter Valid Task Operation Here !!!!!\n")


  
  




