import json
import os

class Storage:
    @staticmethod
    def save_to_file(data, filename):
        """
        Save data to a file in JSON format.

        :param data: Data to be saved
        :param filename: Name of the file
        """
        try:
            with open(filename, 'w') as file:
                json.dump(data, file)
        except Exception as e:
            print(f"Error saving to file: {e}")

    @staticmethod
    def load_from_file(filename):
        """
        Load data from a file in JSON format. Create the file if it does not exist.

        :param filename: Name of the file
        :return: Loaded data
        """
        if not os.path.exists(filename):
            with open(filename, 'w') as file:
                file.write('[]')
            return []
        try:
            with open(filename, 'r') as file:
                return json.load(file)
        except json.JSONDecodeError:
            print("Error decoding JSON from file.")
            return []
