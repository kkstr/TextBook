#!/usr/bin/env python3

import webbrowser
import os
import zipfile


def check():
    with open('cfg.txt', 'r') as f:
        contents = f.read()
        print(contents)
        if contents == '0':
            with open('cfg.txt', 'w') as f:
                f.write('1')
            unzip()
        if contents == '1':
            pass


def main():
    check()
    path = os.path.dirname(os.getcwd())
    print(path)
    try:
        os.remove("C:\VSC\PyText\init.py")
    except:
        Exception
    pass
    print("Select Book: \n\n1: Chemistry 1/2 \n2: Chemistry 3/4  \n3: Physics 1/2 \n4: Physics 3/4 \n5: Methods 1/2 \n6: Methods 3/4 \n7: Specialist 3/4 \n8: Business Management 1/2 \n9: Exit")
    print()
    choice = input("Enter your choice >")
    if choice == "1":
        print("Chemistry 1/2")
        webbrowser.open(path+"\PyText\data\c1\c1.pdf")
        clearOs()
        main()
    if choice == "2":
        print("Chemistry 3/4")
        webbrowser.open_new(path+"\PyText\data\c2\c2.pdf")
        clearOs()
        main()
    if choice == "3":
        print("Physics 1/2")
        webbrowser.open(path+"\PyText\data\p1\p1.pdf")
        clearOs()
        main()
    if choice == "4":
        print("Physics 3/4")
        webbrowser.open(path+"\PyText\data\p2\p2.pdf")
        clearOs()
        main()
    if choice == "5":
        print("Methods 1/2")
        webbrowser.open(path+"\PyText\data\m1\m1.pdf")
        clearOs()
        main()
    if choice == "6":
        print("Methods 3/4")
        webbrowser.open(path+"\PyText\data\m2\m2.pdf")
        clearOs()
        main()
    if choice == "7":
        print("Specialist 3/4")
        webbrowser.open(path+"\PyText\data\s\s.pdf")
        clearOs()
        main()
    if choice == "8":
        print("Business Management 1/2")
        webbrowser.open(path+"\PyText\data\y1\y1.pdf")
        clearOs()
        main()
    elif choice == "9":
        exit()
    else:
        clearOs()
        main()


def cleanUp():
    print("Cleaning up...")
    try:
        os.remove(path+"\PyText\data\c2.zip")
        print("Removed Chemistry 1/2")
        os.remove(path+"\PyText\data\c1.zip")
        print("Removed Chemistry 3/4")
        os.remove(path+"\PyText\data\s.zip")
        print("Removed Specialist 3/4")
        os.remove(path+"\PyText\data\p1.zip")
        print("Removed Physics 1/2")
        os.remove(path+"\PyText\data\p2.zip")
        print("Removed Physics 3/4")
        os.remove(path+"\PyText\data\y1.zip")
        print("Removed Business 1/2")
        print("Removed Methods 1/2")
        os.remove(path+"\PyText\data\m2.zip")
        print("Removed Methods 3/4")
    finally:
        print("\nSuccess!")
        clearOs()


def unzip():
    choice = input("Initialize Program? (y/n) >")
    if choice == "y" or 'Y':
        print("Unzipping...")
        global path
        path = os.path.dirname(os.getcwd())
        print("Initializing...")
        print("Extracting files...")
        print("Initializing done.")
        with zipfile.ZipFile(str(path)+"\PyText\data\c1.zip", "r") as zip_ref:
            zip_ref.extractall(str(path)+"\PyText\data\c1")
            print("Extracted Chemistry 1/2")
        with zipfile.ZipFile(str(path)+"\PyText\data\c2.zip", "r") as zip_ref:
            zip_ref.extractall(str(path)+"\PyText\data\c2")
            print("Extracted Chemistry 3/4")
        with zipfile.ZipFile(str(path)+"\PyText\data\m1.zip", "r") as zip_ref:
            zip_ref.extractall(str(path)+"\PyText\data\m1")
            print("Extracted Methods 1/2")
            with zipfile.ZipFile(str(path)+"\PyText\data\m2.zip", "r") as zip_ref:
                zip_ref.extractall(str(path)+"\PyText\data\m2")
            print("Extracted Methods 3/4")
            with zipfile.ZipFile(str(path)+"\PyText\data\s.zip", "r") as zip_ref:
                zip_ref.extractall(str(path)+"\PyText\data\s")
            print("Extracted Specialist 3/4")
            with zipfile.ZipFile(str(path)+"\PyText\data\p1.zip", "r") as zip_ref:
                zip_ref.extractall(str(path)+"\PyText\data\p1")
            print("Extracted Physics 1/2")
            with zipfile.ZipFile(str(path)+"\PyText\data\p2.zip", "r") as zip_ref:
                zip_ref.extractall(str(path)+"\PyText\data\p2")
            print("Extracted Physics 3/4")
            with zipfile.ZipFile(str(path)+"\PyText\data\y1.zip", "r") as zip_ref:
                zip_ref.extractall(str(path)+"\PyText\data\y1")
            print("Extracted Business 1/2")
            cleanUp()
            print("Done.")
    if choice == "n" or 'N':
        main()
    else:
        print("Invalid input.")
        main()


def clearOs():
    command = 'clear'
    if os.name in ('nt', 'dos'):
        command = 'cls'
    os.system(command)


def exit():
    quit


if __name__ == "__main__":
    main()
