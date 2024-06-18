from datetime import datetime
from data_dictionary import task_data_insert

# check the empty value 
def check_empty(value):
  if value:
    return True
  else:
    print("\n!!Empty Inputs Not Allowed!!\n")
    return False

# check the date 
def check_greter_date(date1, date2):
  if(date2 <= date1):
    print("\n !!Task Start Date Must Be Priovous Then Task End Date!! \n")
    return False
  else:
    return True

# varify the date
def check_date(date_time):
  date_formate = "%Y-%m-%d %H:%M"
  try:
    return datetime.strptime(date_time, date_formate)
  except Exception as e:
    print("\nEnter Valid Date Time Formate")
    return False

# create dictionary
def create_dictionary(keys, values):
  task_dict = dict()
  if(len(keys) == len(values)):  
    for key, value in zip(keys, values):
      task_dict[key] = value
  return task_dict

# check allowed priorities
def allowed_priorities(priority):
  allowed = ("1","2","3")
  return priority in allowed
  
def allowed_status(status):
  allowed = ("pending", "done", "assinged")
  return status in allowed
  
  
def create_task():
  sdate = None
  edate = None
  print("\n--------------------------------------- CREATE TASK ---------------------------------------\n")
  name = input("Enter Task Name: ").strip(" ")
  if not check_empty(name): return False

  desc = input("Task Description: ").strip(" ")
  if not check_empty(desc): return False

  start_date = input("Start Date FORMATE(YYYY-MM-DD HH:MM): ").strip(" ")
  if not check_empty(start_date): return False
  if check_date(start_date):
    sdate = start_date
  else:
    return False

  end_date = input("Ends  Date FORMATE(YYYY-MM-DD HH:MM): ").strip(" ")
  if not check_empty(end_date): return False
  if check_date(end_date):
    edate = end_date
  else: 
    return False
  if not check_greter_date(sdate, edate): return False
  
  status = None
  status = input("Enter Task Status from (pending, assinged, done): ").strip(" ")
  
  if not allowed_status(status):
    print("\n!!Enter Only Allowed Status (pending, assinged, done)!!\n")
    while not allowed_status(status):
      status = input("Enter Task Status from (pending, assinged, done): ").strip(" ")
  if not check_empty(status): return False

  # print(status)
  priority = None
  priority = input("Enter Task Priority from (1,2 or 3): ").strip(" ")
  if not allowed_priorities(priority):
    print("\n!!Enter Allowed Priorites (1,2 or 3)!!\n")
    while not allowed_priorities(priority):
      priority = input("Enter Task Status from (1,2 or 3): ").strip(" ")


  if not check_empty(priority): return False


  id = None
  keys = ("id","name", "description", "start_date", "end_date", "status", "priority")
  task = (id ,name, desc, start_date, end_date, status, priority)
  

  task_dict = create_dictionary(keys, task)
  task_insert = task_data_insert(task_dict)

  if(task_insert):
    last_id = task_insert[0]
    total = task_insert[1]
    print("last id => ", last_id, "total => ", total)
    return task_insert
  else:
    return False



  print("\n--------------------------------------- CREATE TASK ---------------------------------------\n")


