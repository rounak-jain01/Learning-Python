from pathlib import Path
import os
import shutil

def createfolder():
    try:
        name = input("Tell Your Folder Name: ")
        p = Path(name)
        p.mkdir()
        print("Folder Created Successfully.")
    except Exception as err:
        print(f"An error occured as {err}")

def readfolderandfile():
    try:
        path = Path('')
        items = list(path.rglob('*'))
        print(items)
        count = 1
        for i in items:
            print(f"{count}: {i}")
            count += 1
    except Exception as err:
        print(f"An error occured as {err}")

def updatefolder():
    readfolderandfile()
    try:
        name = input("Tell Your Folder Name: ")
        path = Path(name)
        if path.exists():
            new_name = input("Tell Your New Folder Name: ")
            new_path = Path(new_name)
            path.rename(new_path)
            print("Folder Updated Successfully.")
        else:
            print("Folder does not exist.")
    except Exception as err:
        print(f"An error occured as {err}")

def deletefolder():
    readfolderandfile()
    try:
        name = input("Tell Your Folder Name: ")
        path = Path(name)
        if path.exists():
            c = input(f"Are you sure you want to delete the folder '{name}'? (Y/N): ")
            if c.lower() == 'y':
                #path.rmdir() #Delete only if the folder is empty
                #if i want to delete a folder having some files then use shutil
                shutil.rmtree(path)
                print("Folder Deleted Successfully.")
            elif c.lower() == 'n':
                return
            else:
                print("Invalid input. Please enter 'Y' or 'N'.")
        else:
            print("Folder does not exist.")
    except Exception as err:
        print(f"An error occured as {err}")

def createfiles():
    try:
        name = input("Enter File name: ")
        path = Path(name)
        if not path.exists():
            with open(path, 'w') as fs:
                data = input("Write in Your File: ")
                fs.write(data)
        else:
            print("File name already exists.")
    except Exception as err:
        print(f"An error occured as {err}")

def readfile():
    readfolderandfile()
    try:
        name = input("Which file you want to read: ")
        path = Path(name)
        if path.exists():
            with open(path, 'r') as fs:
                print("Your file content is:")
                print(fs.read())
        else:
            print("Sorry, no such file exists.")
    except Exception as err:
        print(f"An error occured as {err}")

def updatefile():
    readfolderandfile()
    try:
        name = input("Which file you want to update: ")
        path = Path(name)
        if path.exists():
            print("Press 1 -> Update the name of your file")
            print("Press 2 -> Append content to your file")
            print("Press 3 -> Overwrite content in your file")
            response = int(input("Tell Your Response: "))

            if response == 1:
                name2 = input("Tell the new name: ")
                path2 = Path(name2)
                path.rename(path2)

            elif response == 2:
                with open(path, 'a') as fs:
                    data = input("What you want to append:\n")
                    fs.write(" " + data)

            elif response == 3:
                with open(path, 'w') as fs:
                    data = input("What you want to write:\n")
                    fs.write(data)
        else:
            print("File does not exist.")
    except Exception as err:
        print(f"An error occured as {err}")

def deletefile():
    readfolderandfile()
    try:
        name = input("Which file you want to delete: ")
        path = Path(name)
        if path.exists():
            os.remove(path)
            print("File Deleted Successfully.")
        else:
            print("No such file exists.")
    except Exception as err:
        print(f"An error occured as {err}")


while True:
    print("Press 1 for Creating a Folder")
    print("Press 2 for Reading a Folder")
    print("Press 3 for Updating a Folder")
    print("Press 4 for Deleting a Folder")
    print("Press 5 for Creating a File")
    print("Press 6 to Read a File")
    print("Press 7 to Update a File")
    print("Press 8 to Delete a File")

    check = int(input("Please Tell Your Response: "))

    if check == 1:
        createfolder()
    elif check == 2:
        readfolderandfile()
    elif check == 3:
        updatefolder()
    elif check == 4:
        deletefolder()
    elif check == 5:
        createfiles()
    elif check == 6:
        readfile()
    elif check == 7:
        updatefile()
    elif check == 8:
        deletefile()
    elif check == 0:
        break

