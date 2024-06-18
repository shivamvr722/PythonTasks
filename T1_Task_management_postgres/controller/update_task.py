import sys
sys.path.insert(0, "/home/shivam-rana/python/T1_Task_management/")
from dbconnection.dbconnect import create_connection
from datetime import datetime

conn = create_connection()
cursor = conn.cursor()

def date_check(dvalue):
	date_formate = "%Y-%m-%d %H:%M"
	try:
		sdate = datetime.strptime(dvalue, date_formate)
		return True
	except ValueError as v:
		print("\nenter valid date as per formate (yyyy:mm:dd hh:mm)!!!\n")
		return False

def update_tasks(id, field, value):
	if(field == "startdate" or field == "deadline"):
		if(date_check(value)):
			pass
		else:
			return False
    
	elif(field == "priority"):
		priorities = ("1","2","3")
		if(value not in priorities):
			print("\nChoose Priority from 1,2,3 only!!\n")
			return False
  
	elif(field == "status"):
		statuses = ("pending", "assinged", "finished")
		if(value not in statuses):
			print("\nselect statuses from the (pending, assinged or finished only)!!!\n")
			return

	try:
		sql = f"UPDATE tasks SET {field} = %s  WHERE id = %s"
		val = (value, id)
		cursor.execute(sql, val)
		conn.commit()
		if(cursor.rowcount):
			return cursor.rowcount
		else:
			return False
	except Exception as e :
		print("Somethign went wrong \n", e)

def update_multple(id, fields, valuse):
	pass