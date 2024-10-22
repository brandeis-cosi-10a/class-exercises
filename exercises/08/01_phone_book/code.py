contacts = {}

def add_contact():
    name = input("Contact name? ")
    number = input("Contact phone number? ")
    contacts[name] = number

def update_contact():
    name = input("Contact name? ")
    if name not in contacts:
        print(f"{name} not found in contacts, please enter an existing name")
        return
    number = input("New phone number? ")
    contacts[name] = number

def delete_contact():
    name = input("Contact name? ")
    if name not in contacts:
        print(f"{name} not found in contacts, please enter an existing name")
        return
    del contacts[name]

while True:
    answer = input("(a)dd a contact, (u)pdate a contact, (d)elete a contact, (q)uit")

    if answer == 'q':
        print("Bye!")
        break
    elif answer == 'a':
        add_contact()
    elif answer == 'u':
        update_contact()
    elif answer == 'd':
        delete_contact()
    else:
        print("Invalid")