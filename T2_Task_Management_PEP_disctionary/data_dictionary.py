id_counter = 10
tasks = []
tasks2 = [
    {'id': 1, 'name': 'test1', 'description': 'tests', 'start_date': '2024-01-01 10:10', 'end_date': '2024-01-01 10:11', 'status': 'pending', 'priority': '1'},
    {'id': 2, 'name': 'test2', 'description': 'test2 desc', 'start_date': '2023-01-01 10:10', 'end_date': '2023-01-02 10:12', 'status': 'done', 'priority': '2'},
    {'id': 3, 'name': 'test3', 'description': 'test3 desc', 'start_date': '2024-01-02 11:10', 'end_date': '2024-01-04 11:12', 'status': 'done', 'priority': '3'},
    {'id': 4, 'name': 'test4', 'description': 'test4 desc', 'start_date': '2024-01-03 12:10', 'end_date': '2024-01-04 12:12', 'status': 'assinged', 'priority': '3'},
    {'id': 5, 'name': 'test5', 'description': 'test5 desc', 'start_date': '2024-01-04 12:10', 'end_date': '2024-01-05 14:12', 'status': 'assinged', 'priority': '1'},
    {'id': 6, 'name': 'test6', 'description': 'test6 desc', 'start_date': '2024-01-04 13:10', 'end_date': '2024-01-03 13:12', 'status': 'done', 'priority': '1'},
    {'id': 7, 'name': 'test7', 'description': 'test7 desc', 'start_date': '2024-01-06 11:10', 'end_date': '2024-01-07 11:12', 'status': 'pending', 'priority': '2'},
    {'id': 8, 'name': 'test8', 'description': 'test8 desc', 'start_date': '2024-01-07 10:10', 'end_date': '2024-01-02 12:12', 'status': 'pending', 'priority': '2'},
    {'id': 9, 'name': 'test9', 'description': 'test9 desc', 'start_date': '2024-01-03 13:10', 'end_date': '2024-01-01 19:12', 'status': 'pending', 'priority': '3'},
    {'id': 10, 'name': 'test10', 'description': 'test10 desc', 'start_date': '2024-03-01 10:10', 'end_date': '2024-03-09 10:12', 'status': 'assinged', 'priority': '3'}
]

# for inserting the data
def task_data_insert(task_dict):
	try:
		blen = len(tasks2)
		global id_counter
		id_counter += 1
		task_dict["id"] = id_counter
		tasks2.append(task_dict)
		llen = len(tasks2)

		if(blen < llen):
			print("\nRecord Inserted Successfully\n")
			last_inserted_id = id_counter
			total_records = llen
			return (last_inserted_id, total_records)
		else:
			print("\n\n!! Failed To Insert Record\n\n")
		
	except Exception as e:
		print("\n!!Error While Inserting!!\n")

# for show the data

def get_data():
  	return tasks2


def delete_data(id):
	if(id):
		for data in tasks2:
			if(str(id) == str(data["id"])):
				tasks2.remove(data)
				print("\nRecord Deleted Successfully\n")
		return True
	else:
		print("\nProvide the id to delete!!\n")  
		return False
  

def update(id, field, value):
	if(id and field and value):
		for data in tasks2:
			if(str(id) == str(data["id"])):
				data[field] = value
				print("\nRecord Updated Successfully\n")
		return True
	else:
		print("\nProvide the id to update!!\n")  
		return False


def update_multiple(id, field, value):
	fields = []
	values = []

	if(id and (len(field) and len(value))):
		# remove the extra space
		for f, v in zip(field, value):
			f = f.strip(" ")
			v = v.strip(" ")
			fields.append(f)
			values.append(v)

		for data in tasks2:
			if(str(id) == str(data["id"])):
				for field, value in zip(fields, values):
					data[field] = value
				print("\nRecord Updated Successfully\n")
				return True
		
	else:
		print("\nProvide the id to delete!!\n")  
		return False