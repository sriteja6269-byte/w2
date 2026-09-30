# Contact Book using Dictionary

contacts = {}

while True:
    print("\n===== CONTACT BOOK =====")
    print("1. Add Contact")
    print("2. Search Contact")
    print("3. Update Contact")
    print("4. Delete Contact")
    print("5. View All Contacts")
    print("6. Exit")

    choice = input("Enter your choice: ")

    # Add Contact
    if choice == "1":
        name = input("Enter contact name: ")
        phone = input("Enter phone number: ")

        contacts[name] = phone
        print("Contact added successfully!")

    # Search Contact
    elif choice == "2":
        name = input("Enter contact name to search: ")

        if name in contacts:
            print("Name:", name)
            print("Phone:", contacts[name])
        else:
            print("Contact not found!")

    # Update Contact
    elif choice == "3":
        name = input("Enter contact name to update: ")

        if name in contacts:
            phone = input("Enter new phone number: ")
            contacts[name] = phone
            print("Contact updated successfully!")
        else:
            print("Contact not found!")

    # Delete Contact
    elif choice == "4":
        name = input("Enter contact name to delete: ")

        if name in contacts:
            del contacts[name]
            print("Contact deleted successfully!")
        else:
            print("Contact not found!")

    # View All Contacts
    elif choice == "5":
        if len(contacts) == 0:
            print("No contacts available.")
        else:
            print("\n--- All Contacts ---")
            for name, phone in contacts.items():
                print(name, ":", phone)

    # Exit
    elif choice == "6":
        print("Thank you for using Contact Book!")
        break

    else:
        print("Invalid choice! Please try again.")