from data_dictionary import delete_data_category_permenent, delete_data_category, delete_data_list_items, delete_data_items_permenent, delete_data_list_permenent, delete_data_list

def remove_category():
    id = input("Enter Id To Remove Category: ").strip(" ")
    ask = input("Do you want to remove? (y/n): ").strip(" ")
    if(ask == "y"):
        delete_data_category(id)
    else:
        return

def remove_category_permenantly():
    id = input("Enter Id To Remove Category: ").strip(" ")
    ask = input("Do you want to remove? (y/n): ").strip(" ")
    if(ask == "y"):
        delete_data_category_permenent(id)
    else:
        return


def remove_list():
    id = input("Enter Id To Remove list: ").strip(" ")
    ask = input("Do you want to remove? (y/n): ").strip(" ")
    if(ask == "y"):
        delete_data_list(id)
    else:
        return

def remove_list_permenantly():
    id = input("Enter Id To Remove list: ").strip(" ")
    ask = input("Do you want to remove? (y/n): ").strip(" ")
    if(ask == "y"):
        delete_data_list_permenent(id)
    else:
        return

def remove_items():
    id = input("Enter List Id To Remove Item: ").strip(" ")
    item_id = input("Enter Item Id To Remove Item: ").strip(" ")
    ask = input("Do you want to remove? (y/n): ").strip(" ")
    if(ask == "y"):
        delete_data_list_items(id, item_id)
    else:
        return

def remove_items_permenantly():
    id = input("Enter List Id To Remove Item: ").strip(" ")
    item_id = input("Enter Item Id To Remove Item: ").strip(" ")
    ask = input("Do you want to remove? (y/n): ").strip(" ")
    if(ask == "y"):
        delete_data_items_permenent(id, item_id)
    else:
        return  