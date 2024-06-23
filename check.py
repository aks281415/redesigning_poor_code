from storage import Storage

class CheckoutManager:
    def __init__(self, storage_file='checkouts.json'):
        self.storage_file = storage_file
        self.checkouts = self.load_checkouts()

    def load_checkouts(self):
        """
        Load checkouts from storage.
        """
        return Storage.load_from_file(self.storage_file)

    def save_checkouts(self):
        """
        Save checkouts to storage.
        """
        Storage.save_to_file(self.checkouts, self.storage_file)

    def checkout_book(self, user_id, isbn):
        if not user_id or not isbn:
            raise ValueError("User ID and ISBN cannot be empty.")
        
        self.checkouts.append({"user_id": user_id, "isbn": isbn})
        self.save_checkouts()
        print("Book checked out.")

    def list_checkouts(self):
        if not self.checkouts:
            print("No checkouts available.")
        for checkout in self.checkouts:
            print(checkout)

    def checkin_book(self, user_id, isbn):
        if not user_id or not isbn:
            raise ValueError("User ID and ISBN cannot be empty.")
        
        self.checkouts = [checkout for checkout in self.checkouts if not (checkout["user_id"] == user_id and checkout["isbn"] == isbn)]
        self.save_checkouts()
        print("Book checked in.")
