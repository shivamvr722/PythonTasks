import sys
sys.path.insert(0, "/home/shivam-rana/python/T1_Task_management/")

from dbconnection.dbconnect import create_connection

# creating the connection object
connection = create_connection()
cursor = connection.cursor()

def showFiledWise(fieldsTuple):
    fields = ""
    for field in fieldsTuple:
        f =  field.strip(" ")
        fields += f + ","

    fields = fields.rstrip(",")
    sql = f"SELECT {fields} FROM tasks"
    cursor.execute(sql)
    results = cursor.fetchall()
    if(len(results)):
        conter = 1
        for result in results:
            print( " | ",conter, " | ", end=" ")
            for i in range(len(result)):
                print("  ", result[i], end="  |")
            conter += 1
            print("\n")
    else:
        print("\nSorry No Record Found :(\n")


def showAll():
    cursor.execute("select * from tasks")
    results = cursor.fetchall()
    if(len(results)):
        conter = 1
        for result in results:
            print( " | ", conter, " | ", end=" ")
            for i in range(len(result)):
                print(" ", result[i], end="  |")
            print("\n")
            conter += 1
    else:
        print("\nSorry No Record Found :(\n")



def showStatusWise(status):
    cursor.execute(f"select * from tasks where status = '{status}'")
    results = cursor.fetchall()
    if(len(results)):
        counter = 1
        for result in results:
            print( " | ", counter, " | ", end=" ")
            for i in range(len(result)):
                print("  ", result[i] , end="  |")
            print("\n")
            counter += 1
    else:
        print("\nSorry No Record Found :(\n")


def showPending():
    showStatusWise('pending')

def showFinished():
    showStatusWise('finished')

def showAssinged():
    showStatusWise('assigned')


def showPriority(priority):
    cursor.execute(f"select * from tasks where priority = {priority}")
    results = cursor.fetchall()
    counter = 1
    for result in results:
        for i in range(len(result)):
            print(" | ", counter, result[i] , end="  |")
        print("\n")
        counter += 1 


def highPriority():
    showPriority("1")

def mediumPriority():
    showPriority("2")

def lowPriority():
    showPriority("3")
