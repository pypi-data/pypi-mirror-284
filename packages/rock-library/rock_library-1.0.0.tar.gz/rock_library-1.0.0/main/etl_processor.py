# my_library/etl_processor.py
from .read_data import DataReader
from .write_data import DataWriter

class ETLProcessor:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination
        self.reader = DataReader(self.source)
        self.writer = DataWriter(self.destination)
    
    def perform_etl(self):
        data = self.reader.read()
        transformed_data = self.transform_data(data)
        self.writer.write(transformed_data)
    
    def transform_data(self, data):
        return [{'id': d['id'], 'name': d['name'].upper()} for d in data]
