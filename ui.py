import encryption
import database

def display_menu():
    print("\nPassword Manager")
    print("1. Add Password")
    print("2. Retrieve Password")
    print("3. Delete Password")
    print("4. Exit")

def add_password(key):
    service = input("Enter the service name: ")
    username = input("Enter the username: ")
    password = input("Enter the password: ")

    encrypted_password = encryption.encrypt_data(password, key)
    database.add_password(service, username, encrypted_password)
    print("Password added successfully!")

def retrieve_password(key):
    service = input("Enter the service name: ")
    result = database.get_password(service)
    if result:
        username, encrypted_password = result
        decrypted_password = encryption.decrypt_data(encrypted_password, key)
        print(f"Service: {service}")
        print(f"Username: {username}")
        print(f"Password: {decrypted_password}")
    else:
        print("Service not found.")

def delete_password():
    service = input("Enter the service name: ")
    database.delete_password(service)
    print("Password deleted successfully!")
