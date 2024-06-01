from datetime import datetime

data_list = [{'id': 1, 'version': '1.1', 'category': 'watches', 'name': 'watch buy', 'status': 'incomplete', 'items': [{'id': 1, 'item_name': 'rado', 'item_status': 'incomplete', 'created_at': '2024-05-22 17:16:10', 'updated_at': "None"}, {'id': 2, 'item_name': 'titan', 'item_status': 'incomplete', 'created_at': '2024-05-22 17:16:15', 'updated_at': "None"}, {'id': 3, 'item_name': 'rolex', 'item_status': 'incomplete', 'created_at': '2024-05-22 17:16:23', 'updated_at': "None"}, {'id': 4, 'item_name': 'casio', 'item_status': 'incomplete', 'created_at': '2024-05-22 17:16:32', 'updated_at': "None"}]},{'id': 2, 'version': '1.1', 'category': 'fruits', 'name': 'buy fruits', 'status': 'incomplete', 'items': [{'id': 1, 'item_name': 'apple', 'item_status': 'incomplete', 'created_at': '2024-05-22 17:19:24', 'updated_at': "None"}, {'id': 2, 'item_name': 'oranges', 'item_status': 'incomplete', 'created_at': '2024-05-22 17:19:29', 'updated_at': "None"}, {'id': 3, 'item_name': 'banana', 'item_status': 'incomplete', 'created_at': '2024-05-22 17:19:32', 'updated_at': "None"}, {'id': 4, 'item_name': 'grapes', 'item_status': 'incomplete', 'created_at': '2024-05-22 17:19:35', 'updated_at': "None"}]},{'id': 3, 'version': '3.1', 'category': 'appliences', 'name': 'buy appliences', 'status': 'incomplete', 'items': [{'id': 1, 'item_name': 'refrigerator', 'item_status': 'incomplete', 'created_at': '2024-05-22 17:23:53', 'updated_at': "None"}, {'id': 2, 'item_name': 'washing machine', 'item_status': 'incomplete', 'created_at': '2024-05-22 17:24:01', 'updated_at': "None"}, {'id': 3, 'item_name': 'microwave oven', 'item_status': 'incomplete', 'created_at': '2024-05-22 17:24:08', 'updated_at': "2024-05-22 17:24:12"}, {'id': 4, 'item_name': 'fan', 'item_status': 'incomplete', 'created_at': '2024-05-22 17:24:11', 'updated_at': "2024-05-22 17:24:14"}]}]

category_list = [{'id': 1, 'name': 'fruits', 'created_at': '2024-05-22 16:19:05', 'updated_at': '2024-05-22 16:19:09'}, {'id': 2, 'name': 'cars', 'created_at': '2024-05-22 16:19:13', 'updated_at': "None"}, {'id': 3, 'name': 'watches', 'created_at': '2024-05-22 16:19:20', 'updated_at': "None"}, {'id': 4, 'name': 'shoes', 'created_at': '2024-05-22 16:19:28', 'updated_at': "2024-05-22 16:19:30"}]

deleted_category_lists = []
deleted_data_lists = []

lis_counter = 3
cat_counter = 5

def create_category_data_list(newcategory):
    global cat_counter
    cat_counter += 1
    newcategory["id"] = cat_counter
    category_list.append(newcategory)
    return cat_counter

def show_data_category():
    if len(category_list):
        return category_list
    else:
        return False

def update_data_category():
    pass

def delete_data_category(id):
    flag = True
    for category in category_list:
        if str(category["id"]) == id:
            index = category_list.index(category)
            category_pop = category_list.pop(index)
            category_pop["deleted_at"] =  datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            deleted_category_lists.append(category_pop)
            if(category_pop):
                print("\n Recored Deleted Successfully!\n")
                flag = True
            break
        else:
            flag = False
    
    if not flag:
        print("\n!Failed To Delete Record or No Recored with given id!\n")

def delete_data_category_permenent(id):
    flag = True
    for category in category_list:
        if str(category["id"]) == id:
            category_list.remove(category)
            print("\n Recored Deleted Successfully!\n")
            flag = True
            break
        else:
            flag = False
    if not flag:
        print("\n!Failed To Delete Record or No Recored with given id!\n")

def show_deleted_categories_data():
    if len(deleted_category_lists):
        return deleted_category_lists
    else:
        return False

def show_deleted_list():
    if len(deleted_data_lists):
        return deleted_data_lists
    else:
        return False

def create_data_list(newlist):
    global lis_counter
    lis_counter += 1
    version = 1
    newlist["id"] = lis_counter
    newlist["version"] = f"{lis_counter}.{version}"
    data_list.append(newlist)
    return lis_counter

def create_data_version_list(todolist):
    pass

def show_data_list():
    if len(data_list):
        return data_list
    else:
        False

def update_data_list(list):
    pass


def delete_data_list(id):
    flag = True
    for data in data_list:
        if str(data["id"]) == id:
            index = data_list.index(data)
            data_pop = data_list.pop(index)
            data_pop["deleted_at"] =  datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            print(data_pop)
            deleted_data_lists.append(data_pop)
            if(data_pop):
                print("\n Recored Deleted Successfully!\n")
                flag = True
            break
        else:
            flag = False
    
    if not flag:
        print("\n!Failed To Delete Record or No Recored with given id!\n")

def delete_data_list_permenent(id):
    flag = True
    for data in data_list:
        if str(data["id"]) == id:
            data_list.remove(data)
            print("\n Recored Deleted Successfully!\n")
            flag = True
            break
        else:
            flag = False
    if not flag:
        print("\n!Failed To Delete Record or No Recored with given id!\n")


# data list items 
def delete_data_list_items(id, item_id):
    pass

def delete_data_items_permenent(id, item_id):
    flag = True
    for data in data_list:
        if str(data["id"]) == id:
            for item in data["items"]:
                print(item)
                if str(data["id"]) == item_id:
                    data['items'].remove(item)
                    print("\n Recored Deleted Successfully!\n")
                    flag = True
                    break
                else:
                    flag = False
    if not flag:
        print("\n!Failed To Delete Record or No Recored with given id!\n")