from abc import ABC, abstractmethod

class RegisterUser(ABC):

    @abstractmethod
    def register(self):
        pass