# pdf, txt , excel 

from abc import ABC, abstractmethod

class Document(ABC):
    
    @abstractmethod
    def load(self):
        pass
    @abstractmethod
    def view(self):
        pass
    @abstractmethod
    def format(self):
        pass
    @abstractmethod
    def calculate(self):
        pass
    
class PDF(Document):
    
    def load(self):
        print("PDF loaded")
        
    def view(self):
        print("PDF viewed")
        
    def format(self):
        print("PDF formatted")
        
    def calculate(self):
        print("PDF calculated")