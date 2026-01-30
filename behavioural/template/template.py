from abc import ABC, abstractmethod
#abstract base class
class ExportBase(ABC):
    def export_report(self, data, file_path):
        self.prepare_data(data)
        self.open_file(file_path)
        self.write_header(data)
        self.write_data(data)
        self.write_footer(data)
        self.close_file(file_path)

    def prepare_data(self, data):
        print("Preparing data for export...")
    
    def open_file(self, file_path):
        print(f"Opening file at {file_path}...")
    
    @abstractmethod
    def write_header(self, data):
        pass

    @abstractmethod
    def write_data(self, data):
        pass

    def write_footer(self, data):
        print("Writing footer...")
    
    def close_file(self, file_path):
        print(f"Closing file at {file_path}...")


class CSVExport(ExportBase):
    def write_header(self, data):
        print("Writing CSV header...")
    
    def write_data(self, data):
        print("Writing CSV data...")

class PDFExport(ExportBase):
    def write_header(self, data):
        print("Writing PDF header...")
    
    def write_data(self, data):
        print("Writing PDF data...")
