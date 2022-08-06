from abc import ABC, abstractclassmethod

class Tires(ABC):
    @abstractclassmethod
    def needs_service():
        pass