import encryption
import database
import ui

def main():
    # Initialize the database and ensure the salt is present
    database.initialize_database()

    # Retrieve the salt from the database
    salt = database.get_salt()

    # Check if the master password is already set
    master_password_hash = database.get_master_password_hash()

    if master_password_hash is None:
        # Set a new master password
        print("No master password set. Please create one.")
        master_password = input("Enter a new master password: ")
        confirm_password = input("Confirm the master password: ")

        if master_password != confirm_password:
            print("Passwords do not match. Exiting.")
            return

        # Store the hashed master password
        hashed_password = encryption.derive_key(master_password, salt)
        database.store_master_password_hash(hashed_password.hex())
        print("Master password has been set.")
    else:
        # Validate the entered master password
        master_password = input("Enter your master password: ")
        hashed_password = encryption.derive_key(master_password, salt)

        if hashed_password.hex() != master_password_hash:
            print("Incorrect master password. Exiting.")
            return

    print("Access granted!")

    # Main application loop
    while True:
        ui.display_menu()
        choice = input("Choose an option: ")

        if choice == "1":
            ui.add_password(hashed_password)
        elif choice == "2":
            ui.retrieve_password(hashed_password)
        elif choice == "3":
            ui.delete_password()
        elif choice == "4":
            print("Exiting Password Manager.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
