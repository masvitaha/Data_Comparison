import os.path


class TxtFileConnector():
    textfile = input("Enter the text File Path: ")

    if os.path.isfile(textfile):
        pass
    else:
        print("File Doesn't Exists")
        exit(0)