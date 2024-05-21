import os as os
import shutil

def check_empty(value):
    if value:
        return True
    else:
        print("\n!! Empty path not allowed !!\n")
        return False


def check_directory(path):
    try:
        if(not os.path.isfile(path)):
            return True
        else:
            print("\n! You Entered The File Path, Please Enter The Directory name !\n")
            return False

    except Exception as e:
        print("\n!!Something Went Wrong While Cheking The Directory!!\n")
        # print(e)


def check_path(path):
    try:
        if(os.path.exists(path)):
            return True
        else:
            print("\n!! Path Not Exists !!\n")
            return False

    except Exception as e:
        print("\n!!Something Went Wrong While Cheking The Directory!!\n")
        # print(e)


def select_single_multiple():
    print("\n Select Option: \n 1. For Sinlge Files\n 2. For All Files")
    option = input("\nSelect Option: ").strip(" ")
    if option == "1" or option == "2":
        return option
    else:
        print("\nEnter Valid Option!\n")
        return False


def move_files(source_path, destination_path, filenames):
    if not check_path(source_path): return False
    if not check_path(destination_path): return False
    try:
        # files = os.listdir(source_path)
        files = filenames
        for file in files:
            src_path = os.path.join(source_path, file)
            dst_path = os.path.join(destination_path, file)
            os.rename(src_path, dst_path)
        print("\n File Moved Successfully \n")
        
    except Exception as e:
        print("\nSomething Went Wrong While Movie Files!\n")
        # print(e)

def dir_move(path, destination, filenames):
    dir_name = input("\nEnter The Directory Name To Create: ").strip(" ")
    try:
        new_path = os.path.join(destination, dir_name)
        os.mkdir(new_path)
        print("Directory Created Successfully on Path: ", new_path)
        move_files(path, new_path, filenames)

    except Exception as e:
        print("Something Went Wrong!")


def copy_files(spath, dpath, filenames):
    try:
        if not check_path(spath): return False
        if not check_path(dpath): return False

        if(filenames):
            for file in filenames:
                if os.path.isfile(os.path.join(spath, file)):
                    source = os.path.join(spath, file)
                    desination = os.path.join(dpath, file)
                    shutil.copy(source, desination)
            print("\n Files Copied Successfully \n")
        else:
            print("\nNo Records To Copy\n")
    except Exception as e:
        print("Something Went Wrong!")
        print(e)


def dir_copy(path, destination, filenames):
    dir_name = input("\nEnter The Directory Name To Create: ").strip(" ")
    try:
        new_path = os.path.join(destination, dir_name)
        os.mkdir(new_path)
        print("Directory Created Successfully on Path: ", new_path)
        copy_files(path, new_path, filenames)

    except Exception as e:
        print("Something Went Wrong!")


def rename_files(paths, file_name, new_name):
    try:
        os.rename(os.path.join(paths, file_name), os.path.join(paths, new_name))
        print("\nRename Done Successfully!\n")
    except Exception as e:
        print("something went wrong while rename!!\n")


def delete_files(path):
    try:
        if(os.path.exists(path)):
            for file in os.listdir(path):
                if(not os.path.isfile(path)):
                    shutil.rmtree(os.path.join(path, file))
                else:
                    os.remove(os.path.join(path, file))
            print("File/Directory Deleted Successfully")
    except Exception as e:
        print("Something Went Wrong While Deleting Files!")


def delete_file(path):
    try:
        os.remove(path)
        print("File Deleted Successfully!")
    except Exception as e:
        print("Something Went Wrong While Deleting Files!")


def create_file(path, file):
    try:
        with open(os.path.join(path, file), 'w') as fp:
            print("\nFile Is Created Successfully\n")
    except Exception as e:
        print("Something Went Wrong While Creating File")


def update_file(path, file):
    try:
        with open(os.path.join(path, file), 'a+') as fs:
            text = input("Enter Text TO Update File Here: ")
            fs.write(f" {text}")
            print("file updated Successfully!")

    except Exception as e:
        print("Something Went Wrong While Update File")


def remove_file(path):
    try:
        os.remove(path)
    except Exception as e:
        print(e)
        print("Something Went Wrong While Creating File")


def create_directory(path):
    dir_name = input("\nEnter The Directory Name To Create: ").strip(" ")
    try:
        if not check_path(path): return False
        if check_directory(path):
            new_path = os.path.join(path, dir_name)
            os.mkdir(new_path)
            print("Directory Created Successfully on Path: ", new_path)

    except Exception as e:
        print("Something Went Wrong While Creating Directory!")


def remove_directory(path):
    dir_name = input("\nEnter The Directory Name To Remove: ").strip(" ")
    try:
        if not check_path(path): return False
        if check_directory(path):
            shutil.rmtree(os.path.join(path, dir_name))
            print("Directory Deleted Successfully on Path")

    except Exception as e:
        print("Something Went Wrong While Deleting Directory!")


def select_opeation(path, filenames):
    print("\n Select The Operation You Want To Perform \n")
    print("\n 1. Move \n 2. Copy \n 3. Rename \n 4. Delete \n 5. Create Directory And Move \n 6. Create Directory And Copy \n 7. Create File \n 8. Update File \n 9. Create Directory \n 10. Remove Directory") 
    option = input("\nSelect Option: ").strip(" ")
    if option == "1":
        destination_path = input("\nEnter The Destination Path: ")
        if not check_path(destination_path): return False
        move_files(path, destination_path, filenames)

    elif option == "2":
        destination_path = input("\nEnter The Destination Directory Path: ").strip(" ")
        if not check_path(destination_path): return False
        if not check_directory(destination_path): return False
        copy_files(path, destination_path, filenames)

    elif option == "3":
        f_path = input("\nEnter The Path To Rename: ").strip(" ")
        fd_name = input("Enter The Old File/Directory to Rename: ").strip(" ")
        fd_name_new = input("Enter The New File/Directory to Rename: ").strip(" ")
        if not check_path(f_path): return False
        rename_files(f_path, fd_name, fd_name_new)

    elif option == "4":
        delete_path = input("\nEnter The Path To Delete: ").strip(" ")
        if not check_path(delete_path): return False
        delete_file(delete_path)

    elif option == "5":
        destination_path = input("\nEnter The Destination Path: ").strip(" ")
        if not check_path(destination_path): return False
        dir_move(path, destination_path, filenames)

    elif option == "6":
        destination_path = input("\nEnter The Destination Directory Path: ").strip(" ")
        if not check_path(destination_path): return False
        if not check_directory(destination_path): return False
        dir_copy(path, destination_path, filenames)
    
    elif option == "7":
        f_path = input("\nEnter Directory Path To Create File: ").strip(" ").strip(" ")
        if not check_path(f_path): return False
        if not check_directory(f_path): return False
        file_name = input("Enter The File Name: ").strip(" ")
        create_file(f_path, file_name)

    elif option == "8":
        f_path = input("\nEnter Directory Path To Update File: ").strip(" ")
        if not check_path(f_path): return False
        if not check_directory(f_path): return False
        file_name = input("Enter The File Name To Update: ").strip(" ")
        update_file(f_path, file_name)

    elif option == "9":
        create_directory(path)

    elif option == "10":
        remove_directory(path)

    else:
        print("\nSelect Valid Option\n")


def get_files_by_name(path, filename):
    filesArr = []
    try:
        flag = False
        files = os.listdir(path)
        count = 1
        for file in files:
            if filename in file:
                filesArr.append(file)
                flag = True
                print(f"\t {count}. ", file)
                count += 1

        if(os.listdir(path)):
            ask = input("\nDo You Want To Perform Operations? y/n: ").strip(" ").lower()
            if(ask == "y"):
                option = select_single_multiple()
                if option == "1":
                    farr = []
                    filename = input("Enter File Name and for multiple(file1,file2,..): ").strip(" ").split(",")
                    farr = [f.strip(" ") for f in filename]
                    select_opeation(path, farr)
                elif option == "2":
                    select_opeation(path, filesArr)
                else:
                    print("Select from give option!")
            else:
                return False

        if not flag:
            print("No Record Found\n")

    except Exception as e:
        print("\n!!Something Went Wrong While Listing The Directory!!\n")
        print(e)


def get_file_by_size(path, size):
    filesizeArr = []
    def get_file_only(file):
        if(os.path.isfile(os.path.join(path, file))):
            return os.path.isfile(os.path.join(path, file))
        else:
            print("\nThere Are Directories!\n")
            return False
    
    flist = filter(get_file_only, os.listdir(path))
    file_with_size = [(f,os.stat(os.path.join(path, f)).st_size) for f in flist]
    
    print(" {:<50} {:<7}".format("File Name", "File Size"))
    for f,s in file_with_size:
        if(round(s/(1000),2)  <= size):
            filesizeArr.append(f)
            print(" {:<50} {:<7}kb".format(f, round(s/(1000),2)))

    if(filesizeArr):
        ask = input("\nDo You Want To Perform Operations? y/n: ").strip(" ").lower()
        if(ask == "y"):
            option = select_single_multiple()
            if option == "1":
                farr = []
                filename = input("Enter Files Name and for multiple(file1,file2,..): ").strip(" ").split(",")
                farr = [f.strip(" ") for f in filename]
                select_opeation(path, farr)
            elif option == "2":
                select_opeation(path, filesizeArr)
            else:
                print("Select from give option!")
        else:
            return False
                

def get_files(path):
    try:
        files = os.listdir(path)
        count = 1
        for file in files:
            print(f"\t {count}. ", file)
            count += 1
        
        if(os.listdir(path)):
            ask = input("\nDo You Want To Perform Operations? y/n: ").strip(" ").lower()
            if(ask == "y"):
                option = select_single_multiple()
                if option == "1":
                    farr = []
                    filename = input("Enter File Name and for multiple(file1,file2,..): ").strip(" ").split(",")
                    farr = [f.strip(" ") for f in filename]
                    select_opeation(path, farr)
                elif option == "2":
                    select_opeation(path, os.listdir(path))
                else:
                    print("Select from give option!")
            else:
                return False
        else:
            print("\nThere is No File or Directory\n")

    except Exception as e:
        print("\n!!Something Went Wrong While Listing The Directory!!\n")
        print(e)


def get_files_by_extension(path, extension):
    try:
        if(extension == "."):
            extension = ""
        filter_files = []
        files = os.listdir(path)
        if(files):
            count = 1
            for file in files:
                if os.path.splitext(file)[1] == extension:
                    print(f"\t {count}. ", file)
                    filter_files.append(file)
                    count += 1

            if(filter_files):
                ask = input("\nDo You Want To Perform Operations? y/n: ").strip(" ").lower()
                if(ask == "y"):
                    option = select_single_multiple()
                    if option == "1":
                        farr = []
                        filename = input("Enter Files Name and for multiple(file1,file2,..): ").strip(" ").split(",")
                        farr = [f.strip(" ") for f in filename]
                        select_opeation(path, farr)
                    elif option == "2":
                        select_opeation(path, filter_files)
                    else:
                        print("Select from give option!")
                else:
                    return False
            else:
                print("\nThere is No File Matched with extension\n")
        else:
            print("\n No Record Files \n")
    except Exception as e:
        print("\n!!Something Went Wrong While Listing The Directory!!\n")
        print(e)


# filter files 
def filter_files():
    path = input("\nEnter The Directory Path To Filter Files: ").strip(" ")
    if not check_empty(path): return False
    if not check_path(path): return False
    if not check_directory(path): return False

    try:
        os.chdir(path)
        print("\nCurrent Directory: ",  os.getcwd())
    except Exception as e:
        print("Something Went Wrong")
        print(e)
        return

    show_option = True
    while show_option:
        print("\nSelect The Option From The Below\n")
        print(" \n 1. Show All File \n 2. Filter File by Name \n 3. Filter File by Size \n 4. Filter File by Extension \n 5. Main Menu")

        option = input("\nEnter Option: ").strip(" ")

        if option == "1":
            get_files(path)
        elif option == "2":
            file_name = input("\nEnter File Name: ").strip(" ")
            print("\n")
            get_files_by_name(path, file_name)
        elif option == "3":
            try:
                size = int(input("Enter The Max File Size You Want in KB: ").strip(" "))
                get_file_by_size(path, size)
            except Exception as e:
                print("Enter Only Numeric Values")
        elif option == "4":
            extension = input("Enter The File Extension: ").strip(" ")
            extension = extension.strip(".")
            extension = f".{extension}"
            get_files_by_extension(path, extension)
        elif option == "5":
            show_option = False
        else:
            print("Please Select The Valid Option")

def ask_path():
    path = input("enter file path: ").strip(" ")
    if not check_empty(path): return False
    if not check_path(path): return False
    if not check_directory(path): return False
    return path

print("Wecome To The File Management")
show_option = True
while show_option:
    print("\nSelect The Option From The Below\n")

    print("\n 1. Show and Filter Files \n 2. Show File Operations \n 3. Exit")

    option = input("\nEnter Option: ").strip(" ")

    if option == "1":
        filter_files()
    elif option == "2":
        farr = []
        path = ask_path()
        if(path):
            filename = input("Enter File Name and for multiple(file1,file2,..): ").strip(" ").split(",")
            farr = [f.strip(" ") for f in filename]
            select_opeation(path, farr)
    elif option == "3":
        break
    else:
        print("Please Select The Valid Option")