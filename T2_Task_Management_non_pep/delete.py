from data_dictionary import delete_data

def detete_task(id):
  if(delete_data(id)):
    return True
  else:
    return False

# def delete_all():
#   datas = get_data()
#   del datas[0]
#   print("\nAll Record Deleted Successfully!!\n")