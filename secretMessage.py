import os

def rename_files():
    file_list = os.listdir("/home/ashish/Downloads/prank/prank")
    saved_path = os.getcwd()
    print("current working Directory is"+ saved_path)
    os.chdir("/home/ashish/Downloads/prank/prank")
    for file_name in file_list:
        print("Old Name - "+file_name)
        print("New Name - "+file_name.translate(None,"0123456789"))
        os.rename(file_name,file_name.translate(None,"0123456789"))
    os.chdir(saved_path)

rename_files()
