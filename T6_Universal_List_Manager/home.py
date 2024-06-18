from data_dictionary import show_data_category, show_data_list
from create import create_list, create_category
from show import show_category_list, show_items_list, show_deleted_categories, show_deleted_data_lists
from delete import remove_category, remove_category_permenantly, remove_items, remove_items_permenantly, remove_list_permenantly, remove_list


print("\nWelcome To Universal List Manager\n")

def list_manager():
    print("\n 1. Create New List \n 2. Show Lists \n 3. Update List \n 4. Delete List")
    option = input("\nEnter Option: ").strip(" ")
    if option == "1":
        create_list()
    elif option == "2":
        show_items_list()
    elif option == "3":
        pass
    elif option == "4":
        print("\n 1. Delete Items \n 2. Remove Items Permenantly")
        option = input("\nEnter Option: ").strip(" ")
        if option == "1":
            remove_list()
        elif option == "2":
            remove_list_permenantly()
        else:
            print("\n Select from given option")
    else:
        print("\n Select from given option")


def category_manager():
    print("\n 1. Create New Category \n 2. Show Categories \n 3. Update Category \n 4. Delete Category \n 5. Show Deleted Categories ")
    option = input("\nEnter Option: ").strip(" ")
    if option == "1":
        create_category()
    elif option == "2":
        show_category_list()
    elif option == "3": 
        pass
    elif option == "4":
        print("\n 1. Delete Category \n 2. Remove Category Permenantly")
        option = input("\nEnter Option: ").strip(" ")
        if option == "1":
            remove_category()
        elif option == "2":
            remove_category_permenantly()
        else:
            print("\n Select from given option")
    elif option == "5":
        show_deleted_categories()
    else:
        print("\n Select from given option")
    

def item_manager():
    pass

def archive():
    pass

def trash():
    print("\n 1. Deleted Categories\n 2. Deleted Lists")
    option = input("\nEnter Option: ").strip(" ")
    if option == "1":
        show_deleted_categories()
    elif option == "2":
        show_deleted_data_lists()
    else:
        print("\n Select from given option")

def version():
    pass


def main():
    show_option = True 
    while show_option:
        print("\nSelect From Below Option\n")
        print("\n 1. List Manager\n 2. Category Manager\n 3. Item/Enter Manager\n 4. Archive\n 5. Trash \n 6. Version Control\n")
        option = input("Enter Option: ").strip(" ")

        if option == "1":
            list_manager()
        elif option == "2":
            category_manager()
        elif option == "3":
            item_manager()
        elif option == "4":
            archive()
        elif option == "5":
            trash()
        elif option == "6":
            version()
        elif option == "7":
            show_option = False
        else:
            print("\n Select from given option")

if __name__ == "__main__":
    main()
