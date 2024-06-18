import sys
sys.path.insert(0, "/home/shivam-rana/python/T1_Task_management/")

from dbconnection.dbconnect import create_connection
from create_task import insert_tasks
from show_tasks import showAll, showPending, showFinished, showAssinged, highPriority, lowPriority, mediumPriority, showFiledWise
from delete_task import delete_task
from update_task import update_tasks

print("\033[0;32;40m\n")
conn = create_connection()
cursor = conn.cursor()

def create_task():
    rows = insert_tasks()
    if(rows):
        print("\nThe Row Incerted Succefully\n")
    else:
        print("Failed To Inserte Row")
        return False
  

def delete_tasks(id):
    rows = delete_task(id)
    if(rows):
        print("The Row Deleted Succefully")
    else:
        print("Failed To Delete Row")
        return False


def update_task(id, field, value):
    rows = update_tasks(id, field, value)  
    if(rows):
        print("Record Updated Successfully")
    else:
        print("Failed to Update the record")
        return False


print("\nWELCOME TO THE TASK MANAGEMENT GRID")
print("WE WOULD LOVE TO MANAGE YOUT TASK\n\n\n")


show_task = True
while show_task:
    print("\nSELECT OPTION YOU WANT TO DO\n")
    print("\n1. Create Task\n2. Show Tasks\n3. Update Tasks\n4. Delete Task\n5. Exit\n")
    select_operation = input("\nSelect Task Operation: ")
    if select_operation == "1":
        create_task()
    elif select_operation == "2":
        print("\n Select Option To See \n 1. Show All \n 2. Select Field Wise\n 3. See Finished Task \n 4. See Assinged Task \n 5. See Pending Task \n 6. See High Priority Task  \n 7. See Medium Priority Task \n 8. See Low Priority Task\n")
        option = input("\nEnter option to see: ")
        print("\n")
        if option == "1":
            showAll()
        elif option == "2":
            fields = input("Enter field of the task to see seprated by commna (field1, field2): ")
            fieldsList = fields.split(",")
            showFiledWise(fieldsList)
        elif option == "3":
            showFinished()
        elif option == "4":
            showAssinged()
        elif option == "5":
            showPending()
        elif option == "6":
            highPriority()
        elif option == "7":
            mediumPriority()
        elif option == "8":
            lowPriority()
        else:
            print("select approprite option!!!")
        
    elif select_operation == "3":
        id = input("Enter id of the task to update: ")
        field = input("Enter field of the task to update: ")
        value = input("Enter value of the task to update: ")

        ask = input("Are you sure you want to update this column y/n: ").lower()
        if(ask == "y"):
            update_task(id, field, value)
        else:
            pass

    elif select_operation == "4":
        id = input("Enter id of the task to delete: ").strip(" ")
        ask = input("Are you sure you want to delete this row y/n: ").lower().strip(" ")
        if(ask == "y"):
            delete_tasks(id)
        else:
            pass

    elif select_operation == "5":
        print("Exit")
        show_task = False
    else:
        print("\n !!!!! Enter Valid Task Operation Here !!!!!\n")