import encryption
import database
import ui

def main():
    encryption.generate_key()  # Generate encryption key once
    database.initialize_database()

    while True:
        ui.display_menu()
        choice = input("Choose an option: ")

        if choice == "1":
            ui.add_password()
        elif choice == "2":
            ui.retrieve_password()
        elif choice == "3":
            ui.delete_password()
        elif choice == "4":
            print("Exiting Password Manager.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
