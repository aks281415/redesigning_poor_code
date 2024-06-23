from models import User
from storage import Storage

class UserManager:
    def __init__(self, storage_file='users.json'):
        self.storage_file = storage_file
        self.users = self.load_users()

    def load_users(self):
        """
        Load users from storage.
        """
        data = Storage.load_from_file(self.storage_file)
        return [User(**user) for user in data]

    def save_users(self):
        """
        Save users to storage.
        """
        data = [user.__dict__ for user in self.users]
        Storage.save_to_file(data, self.storage_file)

    def add_user(self, name, user_id):
        if not name or not user_id:
            raise ValueError("Name and User ID cannot be empty.")
        
        user = User(name, user_id)
        self.users.append(user)
        self.save_users()
        print("User added.")

    def list_users(self):
        if not self.users:
            print("No users available.")
        for user in self.users:
            print(user)

    def search_user(self, attribute, value):
        if attribute not in ['name', 'user_id']:
            raise ValueError("Invalid attribute for search.")
        
        results = [user for user in self.users if getattr(user, attribute) == value]
        return results

    def delete_user(self, user_id):
        if not user_id:
            raise ValueError("User ID cannot be empty.")
        
        self.users = [user for user in self.users if user.user_id != user_id]
        self.save_users()
        print("User deleted.")
