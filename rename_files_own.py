import os
def rename_files():
    #(1) get file names from a folder
    file_list = os.listdir(r"C:\Users\jbarragan\Python\message")
    print(file_list)
    saved_path = os.getcwd()
    print saved_path
    #Change directory
    os.chdir(r"C:\Users\jbarragan\Python\message")
    #(2) for each file, rename filename
    for file_name in file_list:
        print("Old filename: "+file_name)
        print("New filename: "+file_name.translate(None, "0123456789"))
        #Rename de filename - Quit the number in filename
        os.rename(file_name, file_name.translate(None, "0123456789"))
    os.chdir(saved_path)
rename_files()
