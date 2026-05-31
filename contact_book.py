contacts = []

while True:
    print("\n***** CONTACT BOOK *****")
    print("1. Add Contact")
    print("2. View Contacts")
    print("3. Search Contact")
    print("4. Delete Contact")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        n = int(input("How many contact you want to add:  "))
        for i in range(0,n):
            name = input("Enter Name: ")
            phone = input("Enter Phone Number: ")
            contact = {
                  "name": name,
                  "phone": phone
              }

            contacts.append(contact)
            print("Contact Added Successfully!")

    elif choice == "2":
        if len(contacts) == 0:
            print("No Contacts Found!")
        else:
            print("\nContacts:")
            for contact in contacts:
                print(f"Name: {contact['name']}, Phone: {contact['phone']}")

    elif choice == "3":
        search_name = input("Enter Name to Search: ")
        found = False

        for contact in contacts:
            if contact["name"].lower() == search_name.lower():
                print(f"Name: {contact['name']}")
                print(f"Phone: {contact['phone']}")
                found = True
                break

        if not found:
            print("Contact Not Found!")

    elif choice == "4":
        delete_name = input("Enter Name to Delete: ")
        found = False

        for contact in contacts:
            if contact["name"].lower() == delete_name.lower():
                contacts.remove(contact)
                print("Contact Deleted Successfully!")
                found = True
                break

        if not found:
            print("Contact Not Found!")

    elif choice == "5":
        print("Thank You for Using Contact Book!")
        break

    else:
        print("Invalid Choice! Please Try Again.")