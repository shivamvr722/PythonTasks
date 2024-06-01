from data_dictionary import show_data_category, show_data_list, show_deleted_categories_data, show_deleted_list

def categories_asc_decsc(sortby, asc_desc, data_category_func):
    data_list = data_category_func()
    data = sorted(data_list, key=lambda k:k[sortby], reverse=asc_desc)
    if data:
        print(" {:<6} {:<19} {:<24} {:<24} ".format("ID", "Name", "Created At", "Updated At"))
        for d in data:
            id = d["id"]
            name = d["name"]
            created_at = d["created_at"]
            updated_at = str(d["updated_at"])
            # print(id, name, created_at, updated_at)
            print(" {:<5} {:<19} {:<24} {:<24} ".format(id, name, created_at, updated_at))
    else:
        print("\ndata not found\n")


def show_category_list():
    isexit = True
    while isexit:
        print(" \n 1. Show All Categories \n 2. Categories Ascending  \n 3. Categories Descending \n 4. Created Time Filter \n 5. Updated Time Filter \n 6. Exit")
        option = input(" \n Select Option: ")
        if option == "1":
            categories_asc_decsc("id", False, show_data_category)
        elif option == "2":
            categories_asc_decsc("name", False, show_data_category)
        elif option == "3":
            categories_asc_decsc("name", True, show_data_category)
        elif option == "4":
            categories_asc_decsc("created_at", False, show_data_category)
        elif option == "5":
            categories_asc_decsc("updated_at", False, show_data_category)
        elif option == "6":
            isexit = False
        else:
            print("\n Select from given option")


def items_all():
    data_list = show_data_list()
    data = data_list
    for d in data:
        id = d["id"]
        version = d["version"]
        category = d["category"]
        name = d["name"]
        status = d["status"]
        items = d["items"]
        print(" {:<10} {:<20} ".format("Id: ", id))
        print(" {:<10} {:<20} ".format("Version: ", version))
        print(" {:<10} {:<20} ".format("Category: ", category))
        print(" {:<10} {:<20} ".format("Name: ", name))
        print(" {:<10} {:<20} ".format("Status: ", status))
        # {'id': 1, 'item_name': 'rado', 'item_status': 'incomplete', 'created_at': '2024-05-22 17:16:10', 'updated_at': None}
        print("\n")

        print(" {:<10} {:<20} {:<14} {:<24} {:<24}".format("Item Id", "Item Name", "Item Status", "Create At", "Updated At"))
        for item in items:
            item_id = item["id"]
            item_name = item["item_name"]
            item_status = item["item_status"]
            created_at = item["created_at"]
            updated_at = str(item["updated_at"])
            print(" {:<10} {:<20} {:<14} {:<24} {:<24}".format(item_id, item_name, item_status, created_at, updated_at))
        print("\n\n")

        # print(" {:>10} {:>20} ".format("items", str(items)))

    

def items_asc_desc(id, sortby, asc_desc, datafun):
    data_list = datafun()
    print(datafun())
    data = data_list
    for d in data:
        if str(d["id"]) == id:
            flag = True
            id = d["id"]
            version = d["version"]
            category = d["category"]
            name = d["name"]
            status = d["status"]
            items_list = d["items"]
            print(" {:<10} {:<20} ".format("Id: ", id))
            print(" {:<10} {:<20} ".format("Version: ", version))
            print(" {:<10} {:<20} ".format("Category: ", category))
            print(" {:<10} {:<20} ".format("Name: ", name))
            print(" {:<10} {:<20} ".format("Status: ", status))
            print("\n")
            items = sorted(items_list, key=lambda k:k[sortby], reverse=asc_desc)
            print(" {:<10} {:<20} {:<14} {:<24} {:<24}".format("Item Id", "Item Name", "Item Status", "Create At", "Updated At"))
            for item in items:
                item_id = item["id"]
                item_name = item["item_name"]
                item_status = item["item_status"]
                created_at = item["created_at"]
                updated_at = str(item["updated_at"])
                print(" {:<10} {:<20} {:<14} {:<24} {:<24}".format(item_id, item_name, item_status, created_at, updated_at))
            print("\n\n")
        else:
            flag = False
    if not flag:
        print("\nRecored Not Found\n")


def archive_ascending():
    pass

def archive_descending():
    pass

def show_items_list():
    isexit = True
    while isexit:
        print(" \n 1. Show All Items \n 2. Items Acending \n 3. Item Decending \n 4. Created Time Filter \n 5. Updated Time Filter \n 6. Archived Ascending \n 7. Archived Decending\n 8. Exit" )
        option = input(" \n Select Option: ")
        if option == "1":
            items_all()
        elif option == "2":
           id = input(" Enter Item Id: ").strip(" ")
           items_asc_desc(id, "item_name", False, show_data_list)
        elif option == "3":
            id = input(" Enter Item Id: ").strip(" ")
            items_asc_desc(id, "item_name", True, show_data_list)
        elif option == "4":
            id = input(" Enter Item Id: ").strip(" ")
            items_asc_desc(id, "created_at", False, show_data_list)
        elif option == "5":
            id = input(" Enter Item Id: ").strip(" ")
            items_asc_desc(id, "updated_at", False, show_data_list)
        elif option == "6":
            archive_ascending()
        elif option == "7":
            archive_descending()
        elif option == "8":
            isexit = False
        else:
            print("\n Select from given option")


def show_deleted_categories():
    if(show_deleted_categories_data()):
        categories_asc_decsc("id", False, show_deleted_categories_data)
    else:
        print("\n There is not deleted data available \n")



def list_deleted(sortby, asc_desc, datafun):
    data_list = datafun()
    data = data_list
    for d in data:
        flag = True
        id = d["id"]
        version = d["version"]
        category = d["category"]
        name = d["name"]
        status = d["status"]
        items_list = d["items"]
        print(" {:<10} {:<20} ".format("Id: ", id))
        print(" {:<10} {:<20} ".format("Version: ", version))
        print(" {:<10} {:<20} ".format("Category: ", category))
        print(" {:<10} {:<20} ".format("Name: ", name))
        print(" {:<10} {:<20} ".format("Status: ", status))
        print("\n")
        items = sorted(items_list, key=lambda k:k[sortby], reverse=asc_desc)
        print(" {:<10} {:<20} {:<14} {:<24} {:<24}".format("Item Id", "Item Name", "Item Status", "Create At", "Updated At"))
        for item in items:
            item_id = item["id"]
            item_name = item["item_name"]
            item_status = item["item_status"]
            created_at = item["created_at"]
            updated_at = str(item["updated_at"])
            print(" {:<10} {:<20} {:<14} {:<24} {:<24}".format(item_id, item_name, item_status, created_at, updated_at))
        print("\n\n")
    else:
        flag = False
    if not flag:
        print("\nRecored Not Found\n")


def show_deleted_data_lists():
    if(show_deleted_categories_data()):
        list_deleted("item_name", True, show_deleted_list)
    else:
        print("\n There is not deleted data available \n")

