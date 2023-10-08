# Import the necessary modules
import json
import os

# Define the data file to store contacts
DATA_FILE = "contacts.json"

# Check if the data file exists and load the contacts
if os.path.exists(DATA_FILE):
    with open(DATA_FILE, "r") as file:
        contacts = json.load(file)
else:
    contacts = []


# Function to save the contacts to the data file
def save_contacts():
    with open(DATA_FILE, "w") as file:
        json.dump(contacts, file)


# Main menu loop
while True:
    print("╔══════════════════════════════════════════╗")
    print("║       CONTACT MANAGEMENT APPLICATION     ║")
    print("╚══════════════════════════════════════════╝")

    print("Select an option:")
    print("1) Add Contact")
    print("2) View Contact List")
    print("3) Search Contact")
    print("4) Update Contact")
    print("5) Delete Contact")
    print("6) Exit")

    choice = input("Enter the option number: ")

    if choice == "1":
        # Add Contact
        name = input("Enter the contact's name: ")
        phone = input("Enter the contact's phone number: ")
        email = input("Enter the contact's email: ")
        address = input("Enter the contact's address: ")

        contact = {"name": name, "phone": phone, "email": email, "address": address}
        contacts.append(contact)
        save_contacts()
        print("Contact added successfully!")

    elif choice == "2":
        # View Contact List
        print("CONTACT LIST:")
        for i, contact in enumerate(contacts, start=1):
            print(f"{i}. Name: {contact['name']}, Phone: {contact['phone']}")

    elif choice == "3":
        # Search Contact
        search_term = input("Enter the name or phone number to search: ")
        results = []
        for contact in contacts:
            if search_term.lower() in contact['name'].lower() or search_term in contact['phone']:
                results.append(contact)
        if results:
            print("SEARCH RESULTS:")
            for i, result in enumerate(results, start=1):
                print(f"{i}. Name: {result['name']}, Phone: {result['phone']}")
        else:
            print("No contacts found for the given search term.")

    elif choice == "4":
        # Update Contact
        contact_index = int(input("Enter the index of the contact to update: ")) - 1
        if 0 <= contact_index < len(contacts):
            name = input("Enter the updated name: ")
            phone = input("Enter the updated phone number: ")
            email = input("Enter the updated email: ")
            address = input("Enter the updated address: ")

            contacts[contact_index] = {
                "name": name,
                "phone": phone,
                "email": email,
                "address": address
            }
            save_contacts()
            print("Contact updated successfully!")
        else:
            print("Invalid contact index.")

    elif choice == "5":
        # Delete Contact
        contact_index = int(input("Enter the index of the contact to delete: ")) - 1
        if 0 <= contact_index < len(contacts):
            del contacts[contact_index]
            save_contacts()
            print("Contact deleted successfully!")
        else:
            print("Invalid contact index.")

    elif choice == "6":
        # Exit
        print("Goodbye!")
        break

    else:
        print("Invalid choice. Please select a valid option.")
