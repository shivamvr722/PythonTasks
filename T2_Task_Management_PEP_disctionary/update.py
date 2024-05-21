from data_dictionary import update, update_multiple, get_data
from create import check_date, check_empty, allowed_priorities, allowed_status, check_greter_date

def ask_confirm(msg):
    ask = input(msg).lower()
    return ask == "y"

def update_task():
    id = None
    dbedate = None
    dbsdate = None
    datas = get_data()
    keys = datas[0].keys()

    try:
        id = int(input("\tEnter id of the task to update: ").strip(" "))
    except Exception as e:
        print("Enter Only Numeric Id")

    if(not check_empty(id)): return

    id = str(id)
    
    for data in datas:
        if(str(data["id"]) == id):
            dbedate = data["end_date"]
            dbsdate = data["start_date"]
            print("\n\t| {:<5} | {:<17} | {:<17} | {:<17} | {:<17} | {:<17} | {:<8} |\n".format('id', 'Task Name', 'Description', 'Status', "Start Date", "End Date", "Priority"))
            id, name, desc, statuss, sdate, edate, priority = data.values()
            print("\t| {:<5} | {:<17} | {:<17} | {:<17} | {:<17} | {:<17} | {:<8} |\n".format(id, name, desc, statuss, sdate, edate, priority))     

    field = input("\tEnter field of the task to update: ").strip(" ")
    
    if(not check_empty(field)): return
    
    if(field not in keys):
        print("\n!!Unknown Field!!\n")
        return False
    
    if(field == "id"):
        print("\nID not allowed to update\n")
        return False

    value = input("\tEnter value of the task to update: ").strip(" ")

    if(not check_empty(value)): return

    if(field == "status"):
        if(not allowed_status(value)): 
            print("Enter The Allowed Status from (Pending, Assinged, Done): ") 
            return

    if(field == "priority"):
        if(not allowed_priorities(value)): 
            print("Enter The Allowed Status from (1,2 or 3): ") 
            return
    
    if(field == "start_date" or field == "end_date"):
        if check_date(value):
            sedate = value
        if(field == "start_date"):
            if not check_greter_date(sedate, dbedate): return False
        elif(field == "end_date"):
            if not check_greter_date(dbsdate ,sedate): return False
        else: 
            return

    if(ask_confirm("\tAre you sure you want to update this column? y/n: ")):
        update(id,field, value)
    else:
        return 

def update_multi_col():
    dbedate = None
    dbsdate = None
    datas = get_data()
    keys = datas[0].keys()
    id = None

    try:
        id = int(input("\n\tEnter id of the task to update example: ").strip(" "))
    except Exception as e:
        print("Enter Only Numeric ID")

    if(not check_empty(id)): return
    id = str(id)

    for data in datas:
        if(str(data["id"]) == id):
            dbedate = data["end_date"]
            dbsdate = data["start_date"]
            print("\n\t| {:<5} | {:<17} | {:<17} | {:<17} | {:<17} | {:<17} | {:<8} |\n".format('id', 'Task Name', 'Description', "Start Date", "End Date", 'Status', "Priority"))
            id, name, desc, statuss, sdate, edate, priority = data.values()
            print("\t| {:<5} | {:<17} | {:<17} | {:<17} | {:<17} | {:<17} | {:<8} |\n".format(id, name, desc, statuss, sdate, edate, priority))

    field = input("\tEnter field of the task to update example = (field1, field2,...): ").strip(" ")
    if(not check_empty(id)): return

    fields = field.split(",")
    flag = True

    for f in fields:
        if (f.strip(" ") in keys):
            flag = False
        else:
            flag = True

    if flag:  
        print("\n!!Please Enter Valid Fields!!\n")
        return False
         
    if("id" in fields):
        print("\nID not allowed to update\n")
        return False

    value = input("\tEnter value of the task to update example = (value1,value2,...): ").strip(" ")
    if(not check_empty(value)): return
    values = value.split(",")

     # check status
    if("status" in fields):
        flag = False
        allowed = ("pending", "assinged", "done")

        for x in allowed:
            if x in value:
                flag = True

        if(not flag):
            print("Enter The Allowed Status from (pending, assinged, done)") 
            return
    
    # check priority
    if("priority" in fields):
        flag = False
        allowed = ("1", "2", "3")

        for x in allowed:
            if x in value:
                flag = True

        if(not flag):
            print("Enter The Allowed Priority from (1,2 or 3)") 
            return

  # check Date
    if(("start_date" in fields) or ("end_date" in fields)):
        datex = None
        for date in values:
            if(check_date):
                datex = date

        if check_date(datex):
            sedate = value
        if(field == "start_date"):
            if not check_greter_date(sedate, dbedate): return False
        elif(field == "end_date"):
            if not check_greter_date(dbsdate ,sedate): return False
        else: 
            return

    if(ask_confirm("\tAre you sure you want to update this column? y/n: ")):
        update_multiple(id, fields, values)
