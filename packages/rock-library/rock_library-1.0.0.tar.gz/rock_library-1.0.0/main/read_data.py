# my_library/read_data.py

class DataReader:
    def __init__(self, source):
        self.source = source
    
    def read(self):
        print(f"Reading data from {self.source}")
        # Implement actual read logic here
        data = [{'id': 1, 'name': 'Alice'}, {'id': 2, 'name': 'Bob'}]
        return data
