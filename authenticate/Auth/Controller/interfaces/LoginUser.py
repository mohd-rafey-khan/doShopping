from abc import ABC, abstractmethod


class LoginUser(ABC):

    @abstractmethod
    def login(self):
        pass