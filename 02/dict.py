contacts = {"Alice": "123-456-7890", "Bob": "945-879-1230", "Carol": "136-275-2985"}

def add_contact():
    name = input("Enter the name of the new contact: ")
    number = input("Enter the phone number of the new contact: ")
    contacts[name] = number
    print("Updated contacts:", contacts)


def get_contact():
    name = input("Enter the name of the contact: ")
    if name in contacts:
        print(f"The number for {name} is {contacts[name]}")
    else:
        print(f"{name} is not in the contacts.")

while True:
    action = input("Do you want to add a new contact or retrieve a number? (add/retrieve/exit): ").lower()
    if action.lower() == "add":
        add_contact()
    elif action.lower() == "retrieve":
        get_contact()
    elif action.lower() == "exit":
        break
    else:
        print("Invalid option. Please enter 'add', 'retrieve', or 'exit'.")

# Given sets
set1 = {6, 8, 3, 5}
set2 = {1, 6, 7, 3, 4}

union_set = set1 | set2
print("Union of set1 and set2:", union_set)

intersection_set = set1 & set2
print("Intersection of set1 and set2:", intersection_set)
