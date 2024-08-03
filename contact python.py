def display_menu():
    print("\nContact Book Menu:")
    print("1. Add Contact")
    print("2. View Contact List")
    print("3. Search Contact")
    print("4. Update Contact")
    print("5. Delete Contact")
    print("6. Exit")

def add_contact(contact_book):
    name = input("Enter name: ")
    phone = input("Enter phone number: ")
    email = input("Enter email: ")
    address = input("Enter address: ")
    
    contact_book[name] = {'phone': phone, 'email': email, 'address': address}
    print(f"Contact {name} added successfully.")

def view_contacts(contact_book):
    if not contact_book:
        print("No contacts found.")
        return
    
    print("\nContact List:")
    for name, details in contact_book.items():
        print(f"Name: {name}, Phone: {details['phone']}")

def search_contact(contact_book):
    query = input("Enter name or phone number to search: ")
    found = False
    for name, details in contact_book.items():
        if query.lower() in name.lower() or query == details['phone']:
            print(f"\nName: {name}")
            print(f"Phone: {details['phone']}")
            print(f"Email: {details['email']}")
            print(f"Address: {details['address']}")
            found = True
    if not found:
        print("Contact not found.")

def update_contact(contact_book):
    name = input("Enter the name of the contact to update: ")
    if name in contact_book:
        print(f"Current details for {name}:")
        print(f"Phone: {contact_book[name]['phone']}")
        print(f"Email: {contact_book[name]['email']}")
        print(f"Address: {contact_book[name]['address']}")
        
        phone = input("Enter new phone number (or press Enter to keep current): ")
        email = input("Enter new email (or press Enter to keep current): ")
        address = input("Enter new address (or press Enter to keep current): ")
        
        if phone:
            contact_book[name]['phone'] = phone
        if email:
            contact_book[name]['email'] = email
        if address:
            contact_book[name]['address'] = address
        
        print(f"Contact {name} updated successfully.")
    else:
        print("Contact not found.")

def delete_contact(contact_book):
    name = input("Enter the name of the contact to delete: ")
    if name in contact_book:
        del contact_book[name]
        print(f"Contact {name} deleted successfully.")
    else:
        print("Contact not found.")

def main():
    contact_book = {}
    while True:
        display_menu()
        choice = input("Enter your choice: ")
        
        if choice == '1':
            add_contact(contact_book)
        elif choice == '2':
            view_contacts(contact_book)
        elif choice == '3':
            search_contact(contact_book)
        elif choice == '4':
            update_contact(contact_book)
        elif choice == '5':
            delete_contact(contact_book)
        elif choice == '6':
            print("Exiting Contact Book. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
