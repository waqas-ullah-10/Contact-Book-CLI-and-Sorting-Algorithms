# ContactBook CLI App

from collections import deque

contacts = {}
phone_numbers = set()
history = deque()


def add_contact():
    name = input("Enter Name: ").title()

    if name in contacts:
        print("Contact already exists.")
        return

    phone = input("Enter Phone Number: ")

    if phone in phone_numbers:
        print("Phone number already exists.")
        return

    contacts[name] = phone
    phone_numbers.add(phone)
    history.append(f"Added {name}")

    print("Contact added successfully.")


def view_contacts():
    if not contacts:
        print("No contacts found.")
        return

    print("\n----- Contact List -----")

    for name, phone in sorted(contacts.items()):
        print(f"{name} : {phone}")


def search_contact():
    name = input("Enter Name to Search: ").title()

    if name in contacts:
        print(f"{name} : {contacts[name]}")
    else:
        print("Contact not found.")


def update_contact():
    name = input("Enter Name to Update: ").title()

    if name not in contacts:
        print("Contact not found.")
        return

    new_phone = input("Enter New Phone Number: ")

    if new_phone in phone_numbers:
        print("Phone number already exists.")
        return

    phone_numbers.remove(contacts[name])
    contacts[name] = new_phone
    phone_numbers.add(new_phone)

    history.append(f"Updated {name}")

    print("Contact updated successfully.")


def delete_contact():
    name = input("Enter Name to Delete: ").title()

    if name not in contacts:
        print("Contact not found.")
        return

    phone_numbers.remove(contacts[name])
    del contacts[name]

    history.append(f"Deleted {name}")

    print("Contact deleted successfully.")


def show_history():
    if not history:
        print("No recent actions.")
        return

    print("\nRecent Actions:")

    for action in history:
        print(action)


def main():

    while True:

        print("\n========== CONTACT BOOK ==========")
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Search Contact")
        print("4. Update Contact")
        print("5. Delete Contact")
        print("6. View Recent Actions")
        print("7. Exit")

        choice = input("Enter Choice: ")

        if choice == "1":
            add_contact()

        elif choice == "2":
            view_contacts()

        elif choice == "3":
            search_contact()

        elif choice == "4":
            update_contact()

        elif choice == "5":
            delete_contact()

        elif choice == "6":
            show_history()

        elif choice == "7":
            print("Thank you for using Contact Book!")
            break

        else:
            print("Invalid Choice")


if __name__ == "__main__":
    main()