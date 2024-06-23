import unittest
from book import BookManager
from user import UserManager
from storage import Storage


class TestLibraryManagement(unittest.TestCase):

    def setUp(self):
        # Initialize managers
        self.book_manager = BookManager(storage_file='test_books.json')
        self.user_manager = UserManager(storage_file='test_users.json')
        
        # Ensure test files are empty or properly initialized
        Storage.save_to_file([], 'test_books.json')
        Storage.save_to_file([], 'test_users.json')
        
        # Print statements for debugging
        print("Test setup complete. Files initialized.")

    def test_add_book(self):
        try:
            # Print current state before adding book
            print("Before adding book:", self.book_manager.books)
            
            # Add the book
            self.book_manager.add_book("Harry Potter", "JK Rowling", "1234567890")
            print("Book 'Harry Potter' added.")
            
            # Print current state after adding book
            print("After adding book:", self.book_manager.books)
            
            # Verify data saved to test file matches expectations
            saved_data = Storage.load_from_file('test_books.json')
            print("Data in test_books.json after save:", saved_data)
            
            self.assertEqual(len(saved_data), 1)
            self.assertEqual(saved_data[0]['title'], "Harry Potter")
            self.assertEqual(saved_data[0]['author'], "JK Rowling")
            self.assertEqual(saved_data[0]['isbn'], "1234567890")
            
            # Additional checks on manager state
            self.assertEqual(len(self.book_manager.books), 1)
            self.assertEqual(self.book_manager.books[0].title, "Harry Potter")
        except Exception as e:
            print("Exception occurred:", e)
            raise

    def test_add_user(self):
        try:
            print("Before adding user:", self.user_manager.users)
            self.user_manager.add_user("AKS", "1001")
            print("After adding user:", self.user_manager.users)
            
            # Verify data saved to test file matches expectations
            saved_data = Storage.load_from_file('test_users.json')
            self.assertEqual(len(saved_data), 1)
            self.assertEqual(saved_data[0]['name'], "AKS")
            self.assertEqual(saved_data[0]['user_id'], "1001")
            
            # Additional checks on manager state
            self.assertEqual(len(self.user_manager.users), 1)
            self.assertEqual(self.user_manager.users[0].name, "AKS")
        except Exception as e:
            print("Exception occurred:", e)
            raise

    





if __name__ == "__main__":
    choice = input("Enter 1 for test_add_user, 2 for test_add_book: ")
    
    if choice == "2":
        unittest.main(argv=[''], defaultTest='TestLibraryManagement.test_add_book', exit=False)
    elif choice == "1":
        unittest.main(argv=[''], defaultTest='TestLibraryManagement.test_add_user', exit=False)
    else:
        print("Invalid choice. Please enter 1 or 2.")
