from create import create_task
from update import update_task, update_multi_col
from delete import detete_task
from show import *

def ask_confirm(msg):
	ask = input(msg).lower()
	return ask == "y"


print("\nWELCOME TO THE TASK MANAGEMENT by Dictionary")
print("WE WOULD LOVE TO MANAGE YOUR TASKs\n\n\n")

show_task = True
while show_task:
	print("\nOPTION TASK MANAGEMENT\n")
	print("\n1. Create Task\n2. Show Tasks\n3. Update Tasks\n4. Delete Task\n5. Exit\n")

	select_operation = input("\nSelect Task Operation: ")
	if select_operation == "1":
		new_task = True
		while new_task:
			create_task()
			# asking to add more or not
			ask = input("\nDo You Wanted To Create Task y/n: ").strip(" ").lower()
			if(ask == "n"):
				new_task = False


	elif select_operation == "2":
		print("\n Select Option To See \n 1. Show All \n 2. Select Field Wise\n 3. See Finished Task \n 4. See Assinged Task \n 5. See Pending Task \n 6. See High Priority Task  \n 7. See Medium Priority Task \n 8. See Low Priority Task\n")

		option = input("\nEnter option to see: ")
		print("\n")
		if option == "1":
			show_all()

		elif option == "2":
			fields = input("Enter field of the task to see seprated by commna (field1, field2): ")
			fieldsList = fields.split(",")
			show_field(fieldsList)

		elif option == "3":
			show_finished()

		elif option == "4":
			show_asssinged()

		elif option == "5":
			show_pending()

		elif option == "6":
			show_high_priority()

		elif option == "7":
			show_medium_priority()

		elif option == "8":
			show_low_priority()

		else:
			print("select approprite option!!!")
		

	elif select_operation == "3":
		print("\nSelect Option To Update\n  1.Update Single Column \n  2.Update Multiple Column \n ")
		option = input("\n Enter Option To Update: ")

		if(option == "1"):
			update_task()

		elif(option == "2"):
			update_multi_col()
	
		else:
			print("\nPlease Select The Correct Option from (1 or 2)\n")


	elif select_operation == "4":
		id = input("Enter id of the task to delete: ")
		dbedate = None
		dbsdate = None
		datas = get_data()
		# keys = datas[0].keys()
		for data in datas:
			if(str(data["id"]) == str(id)):
				dbedate = data["end_date"]
				dbsdate = data["start_date"]
				print("\n\t| {:<5} | {:<17} | {:<17} | {:<17} | {:<17} | {:<17} | {:<8} |\n".format('id', 'Task Name', 'Description', 'Status', "Start Date", "End Date", "Priority"))
				id, name, desc, statuss, sdate, edate, priority = data.values()
				print("\t| {:<5} | {:<17} | {:<17} | {:<17} | {:<17} | {:<17} | {:<8} |\n".format(id, name, desc, statuss, sdate, edate, priority))

		id = int(id)
		ask = input("Are you sure you want to delete this row y/n: ").lower()
		if(ask == "y"):
			detete_task(id)
		else:
			pass

	elif select_operation == "5":
		print("Exit")
		show_task = False
	
	else:
		print("\n !!!!! Enter Valid Task Operation Here !!!!!\n")
