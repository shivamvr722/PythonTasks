from datetime import datetime
from data_dictionary import show_data_category, create_category_data_list, create_data_list, show_data_list

def check_empty(value):
    if value == "":
        print("\n!!Empty Value Not Allowed!!\n")
        return False
    else:
        return True

def check_available_category_list(category_list, func_cat_list, cat_list):
    flag = True
    while flag:
        if func_cat_list():
            for available in func_cat_list():
                if available["name"] == category_list:
                    flag = True
                    category_list = input(f"Enter {cat_list} Name: ").strip(" ")
                    print(f"\n{cat_list} Already Exists! Please Enter A New {cat_list} Name\n")
                    break
                else:
                    flag = False
                    return category_list
        else:
            return category_list

def create_category():
    new_cat_dict = dict()
    new_cat_dict["id"] = None

    category = input("\nEnter Category Name: ").strip(" ")
    new_cat_name = check_available_category_list(category, show_data_category, "Category")
    new_cat_dict["name"] = new_cat_name
    new_cat_dict["created_at"] = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    new_cat_dict["updated_at"] = "None"
    # creating new category
    last_id = create_category_data_list(new_cat_dict)
    if last_id:
        print(f"\n Record Inserted Successfully id = {last_id}\n")
        return last_id
    else:
        print("\n !Failed To Create Category! \n")
        return False


def new_item():
    items_list = list()
    new_item = True
    item_count = 0
    while new_item:
        item_dict = dict()
        item_count += 1
        item_dict["id"] = item_count
        item_name = input("\nEnter New Item: ").strip(" ")
        item_dict["item_name"] = item_name
        item_dict["item_status"] = "incomplete"
        item_dict["created_at"] = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        item_dict["updated_at"] = "None"
        items_list.append(item_dict)
        ask = input("\n Do you want to add more items? (y/n): ").strip(" ").lower()
        if ask == "n":
            return items_list
        

def create_list():
    new_dict = dict()
    new_dict["id"] = None
    new_dict["version"] = None

    def new_category():
        new_category_id = create_category()
        for category in show_data_category():
            if category["id"] == new_category_id:
                new_dict["category"] = category["name"]
                break


    # create category
    categories = show_data_category()
    print(" {:>6} {:>19} ".format("ID", "Name"))
    for category in categories:
        id = category["id"]
        name = category["name"]
        print(" {:>5} {:>19} ".format(id, name))


    print("\nSelect Category From the Above List or Create New Category")
    print("\n 1. Select From Above list\n 2. Create New Category ")
    option = input("\nSelect Option: ").strip(" ")
    if option == "1":
        if show_data_category():
            flag = True
            while flag:
                cat_name = input("Enter Category id: ").strip(" ")
                for cat in show_data_category():
                    if str(cat["id"]) == cat_name:
                        print("category seleted:", cat["name"])
                        new_dict["category"] = cat["name"]
                        flag = False
                        break
                    else:
                        flag = True
        else:
            print("\n There is no category available to select please create new!\n")
            ask = input(" Do You want to create new? (y/n): ").strip(" ").lower()
            print("\n")
            if ask == "y":
                new_category()
            else:
                return False
        

    elif option == "2":
        new_category()
        

    else:
        print("\n Select from given option")
        return False

    # create list name
    list_name = input("\nEnter The List Name: ").strip(" ")
    new_list_name = check_available_category_list(list_name, show_data_list, "List")
    new_dict["name"] = new_list_name

    # create list status 
    new_dict["status"] = "incomplete"

    # enter tasks
    new_dict["items"] = new_item()

    # create data list
    last_id = create_data_list(new_dict)
    if(last_id):
        print(f"\n Record Inserted Successfully = {last_id}\n")
    else:
        print("\n !Failed To Insert Record! \n")





# def new_item():
#     items_list = list()
#     new_item = True
#     item_count = 0
#     while new_item:
#         item_dict = dict()
#         item_count += 1
#         item_dict["id"] = item_count
#         item_name = input("\nEnter New Item: ").strip(" ")
#         item_dict["item_name"] = item_name
#         item_status = input("\nEnter Item Status \n 1. Complete\n 2. Incomplete: \n Enter Status: ").strip(" ")
#         while item_status != "1" or item_status != "2":
#             if item_status == "1":
#                 item_dict["item_status"] = "complete"
#                 break
#             elif item_status == "2":
#                 item_dict["item_status"] = "incomplete"
#                 break
#             else:
#                 print("Enter From given option only\n")
#                 item_status = input("\nEnter Item Status \n 1. Complete\n 2. Incomplete: \n Enter Status: ").strip(" ")

#         items_list.append(item_dict)
#         ask = input("\n Do you want to add more items? (y/n): ").strip(" ").lower()
#         if ask == "n":
#             return items_list