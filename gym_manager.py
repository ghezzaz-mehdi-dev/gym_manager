import os
import time

def clear_terminal():
    os.system("cls" if os.name == "nt" else "clear")

class User:
    def __init__(self, first_name, last_name, id_, status="inactive"):
        self.first_name = first_name
        self.last_name = last_name
        self.id_ = id_
        self.status = status

    def display(self):
        print(f"\nFirst name: {self.first_name}")
        print(f"Last name: {self.last_name}")
        print(f"ID: {self.id_}")
        print(f"Status: {self.status}\n")
        

def create_user():
    first = input("Enter your first name: ")
    last = input("Enter your last name: ")
    id_ = input("Enter membership ID: ")
    status = input("Enter membership status (leave empty if inactive): ")

    if status.lower() == "active":
        return User(first, last, id_, status="active")
    else:
        return User(first, last, id_)

# Search function
def search(users):
    clear_terminal()
    print("\nSearch by:\n")
    print("1. Membership ID")
    print("2. First name")
    print("3. Membership status\n")

    choice = input("Enter your choice: ")
    found_members = []

    if choice == "1":
        search_id = input("Enter the membership ID to search: ")
        for x in users:
            if x.id_ == search_id:
                found_members.append(x)
                break
    elif choice == "2":
        search_name = input("Enter the first name to search: ")
        for x in users:
            if x.first_name.lower() == search_name.lower():
                found_members.append(x)
    elif choice == "3":
        search_status = input("Enter the member status (active/inactive): ")
        for x in users:
            if x.status.lower() == search_status.lower():
                found_members.append(x)
    else:
        print("Please enter 1, 2 or 3 to continue!")
        time.sleep(2)
        return

    if found_members:
        clear_terminal()
        print("Member(s) found:\n")
        for x in found_members:
            x.display()
            time.sleep(3)
    else:
        print("No member found!")
        time.sleep(2)

# Main program
users = []

while True:
    clear_terminal()
    print("Welcome to Gym Membership Management!\n")
    print("Choose an action:\n")
    print("1. Add new member")
    print("2. Display all members")
    print("3. Search for a member")
    print("4. Exit\n")

    choice = input("Enter your choice: ")

    if choice == "1":
        users.append(create_user())
        print("User added successfully!")
        time.sleep(2)

    elif choice == "2":
        clear_terminal()
        if users:
            print("Displaying all members...\n")
            for user in users:
                user.display()
            time.sleep(4)
        else:
            print("Sorry, no users found.")
            time.sleep(3)

    elif choice == "3":
        if users:
            search(users)
        else:
            print("No members to search.")
            time.sleep(2)

    elif choice == "4":
        print("Please wait 2 seconds to exit...")
        time.sleep(2)
        break

    else:
        print("Invalid choice. Please enter 1, 2, 3 or 4.")
        time.sleep(2)

