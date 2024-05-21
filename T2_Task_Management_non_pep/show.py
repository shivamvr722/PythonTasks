from data_dictionary import get_data

def show_all():
  datas = get_data()
  datas_sort = sorted(datas, key = lambda d: d["end_date"])
  datas = datas_sort
  
  if(len(datas)):
    print("| {:<5} | {:<17} | {:<17} | {:<17} | {:<17} | {:<17} | {:<8} |\n".format('id', 'Task Name', 'Description', "Start Date", "End Date", 'Status', "Priority"))
    for data in datas:
      id, name, desc, status, sdate, edate, priority = data.values()
      print("| {:<5} | {:<17} | {:<17} | {:<17} | {:<17} | {:<17} | {:<8} |".format(id, name, desc, status, sdate, edate, priority))
      print("\n")
  else:
    print("No Record Found :(")
    


def show_field(keys):
  newKeys = []
  try:
    if(len(keys)):
      for key in keys:
        newKeys.append(key.strip(" "))

      datas = get_data()
      
      for data in datas:
        print(end="  |")
        for key in newKeys:
          print(data.get(key), end="  |  ")
        print("")

    else:
      print("\nNo Record Found :(\n")

  except Exception as e:
    print("\n!!!Something Went Wrong!!!\n" + e)



# functions for priority
def show_priority(priority):
  
  datas = get_data()
  datas_sort = sorted(datas, key = lambda d: d["end_date"])
  datas = datas_sort

  if(len(datas)):
    print("| {:<5} | {:<17} | {:<17} | {:<17} | {:<17} | {:<17} | {:<8} |\n".format('id', 'Task Name', 'Description', 'Status', "Start Date", "End Date", "Priority"))
    for data in datas:
      if(data["priority"] == priority):
        id, name, desc, status, sdate, edate, priority = data.values()
        print("| {:<5} | {:<17} | {:<17} | {:<17} | {:<17} | {:<17} | {:<8} |".format(id, name, desc, status, sdate, edate, priority))
        print("\n")
  else:
    print("No Record Found :(")

# function calling for priority
def show_high_priority():
  show_priority("1")
def show_medium_priority():
  show_priority("2")
def show_low_priority():
  show_priority("3")



# functions for the status
def show_status(status):
  datas = get_data()
  datas_sort = sorted(datas, key = lambda d: d["end_date"])
  datas = datas_sort
  if(len(datas)):
    print("| {:<5} | {:<17} | {:<17} | {:<17} | {:<17} | {:<17} | {:<8} |\n".format('id', 'Task Name', 'Description', 'Status', "Start Date", "End Date", "Priority"))
    for data in datas:
      if data["status"] == status:
        id, name, desc, statuss, sdate, edate, priority = data.values()
        print("| {:<5} | {:<17} | {:<17} | {:<17} | {:<17} | {:<17} | {:<8} |\n".format(id, name, desc, statuss, sdate, edate, priority))
  else:
    print("No Record Found :(")

# functions calling for the status
def show_pending():
  show_status("pending")
def show_asssinged():
  show_status("assinged")
def show_finished():
  show_status("done")
