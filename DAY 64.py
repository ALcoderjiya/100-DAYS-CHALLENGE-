#DAY 64 CONTACT BOOK
import pickle
import os

def addContact():
    name = input("Enter Name : ")
    phone = input("Enter Phone Number : ")
    data = [name,phone]
    f = open("contacts.dat","ab")
    pickle.dump(data,f)
    f.close()
    print("Added Successfully")

def display():
    f = open("contacts.dat","rb")
    print("-"*30)
    print("Name\t\tContact")
    try :
        while True:
            data = pickle.load(f)
            print(data[0]+"\t\t"+data[1])
    except EOFError:
        f.close()

def search():
    name = input("Enter name to be searched : ")
    f = open("contacts.dat","rb")
    print("-"*30)
    n = 0
    print("Name\t\tContact")
    try:
        while True:
            data = pickle.load(f)
            if data[0] == name:
                print(data[0]+"\t\t"+data[1])
                n += 1
    except:
        if n == 0:
            print("No Such Contact Found")
        f.close()

def update():
    name = input("Enter name to be updated : ")
    f = open("contacts.dat", "rb")
    g = open("temp.dat","wb")
    print("-" * 30)
    n = 0
    print("Name\t\tContact")
    try:
        while True:
            data = pickle.load(f)
            if data[0] == name:
                print(data[0] + "\t\t" + data[1])
                phone = input("Enter the Modified phone number : ")
                data[1] = phone
                n += 1
            pickle.dump(data,g)
    except:
        f.close()
        g.close()
        if n == 0:
            print("No Such Contact Found")
        else:
            os.remove("contacts.dat")
            os.rename("temp.dat","contacts.dat")

def delete():
    name = input("Enter name to be deleted : ")
    f = open("contacts.dat", "rb")
    g = open("temp.dat", "wb")
    print("-" * 30)
    n = 0
    print("\t\t\t\tName\t\tContact")
    try:
        while True:
            data = pickle.load(f)
            if data[0] == name:
                print("Deleted Record  " + data[0] + "\t\t" + data[1])
                n += 1
            else:
                pickle.dump(data, g)
    except:
        f.close()
        g.close()
        if n == 0:
            print("No Such Contact Found")
        else:
            os.remove("contacts.dat")
            os.rename("temp.dat", "contacts.dat")

while True:
    print("-" * 30)
    print("Press 1 - Add a New Contact")
    print("Press 2 - Display All Contact")
    print("Press 3 - Search a Contact ")
    print("Press 4 - Update a Contact")
    print("Press 5 - Delete a Contact")
    print("Press any other number to EXIT")
    print("-" * 30)
    choice = int(input("Enter your choice : "))
    if choice == 1:
        addContact()
    elif choice == 2:
        display()
    elif choice == 3:
        search()
    elif choice == 4:
        update()
    elif choice == 5:
        delete()
    else:
        break