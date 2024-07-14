# my_library/write_data.py

class DataWriter:
    def __init__(self, destination):
        self.destination = destination
    
    def write(self, data):
        print(f"Writing data to {self.destination}")
        # Implement actual write logic here
        for record in data:
            print(f"Writing record: {record}")
