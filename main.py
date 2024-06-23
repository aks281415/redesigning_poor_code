from book import BookManager
from user import UserManager
from check import CheckoutManager
import os

def initialize_files():
    """
    Ensure the storage files exist.
    """
    storage_files = ['books.json', 'users.json', 'checkouts.json']
    for file in storage_files:
        if not os.path.exists(file):
            with open(file, 'w') as f:
                f.write('[]')

def main_menu():
    """
    Display the main menu and get the user's choice.
    """
    print("\nLibrary Management System")
    print("1. Add Book")
    print("2. List Books")
    print("3. Add User")
    print("4. List Users")
    print("5. Checkout Book")
    print("6. Checkin Book")
    print("7. List Checkouts")
    print("8. Exit")
    choice = input("Enter choice: ")
    return choice

def main():
    initialize_files()
    book_manager = BookManager()
    user_manager = UserManager()
    checkout_manager = CheckoutManager()

    while True:
        choice = main_menu()
        try:
            if choice == '1':
                title = input("Enter title: ")
                author = input("Enter author: ")
                isbn = input("Enter ISBN: ")
                book_manager.add_book(title, author, isbn)
            elif choice == '2':
                book_manager.list_books()
            elif choice == '3':
                name = input("Enter user name: ")
                user_id = input("Enter user ID: ")
                user_manager.add_user(name, user_id)
            elif choice == '4':
                user_manager.list_users()
            elif choice == '5':
                user_id = input("Enter user ID: ")
                isbn = input("Enter ISBN of the book to checkout: ")
                checkout_manager.checkout_book(user_id, isbn)
            elif choice == '6':
                user_id = input("Enter user ID: ")
                isbn = input("Enter ISBN of the book to checkin: ")
                checkout_manager.checkin_book(user_id, isbn)
            elif choice == '7':
                checkout_manager.list_checkouts()
            elif choice == '8':
                print("Exiting.")
                break
            else:
                print("Invalid choice, please try again.")
        except ValueError as e:
            print(f"Error: {e}")

if __name__ == "__main__":
    main()
