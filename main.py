import encryption
import database
import ui

def main():
    # Initialize the database and ensure the salt is present
    database.initialize_database()

    # Retrieve the salt from the database
    salt = database.get_salt()

    # Prompt the user for their master password
    master_password = input("Enter your master password: ")
    key = encryption.derive_key(master_password, salt)

    while True:
        ui.display_menu()
        choice = input("Choose an option: ")

        if choice == "1":
            ui.add_password(key)
        elif choice == "2":
            ui.retrieve_password(key)
        elif choice == "3":
            ui.delete_password()
        elif choice == "4":
            print("Exiting Password Manager.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
