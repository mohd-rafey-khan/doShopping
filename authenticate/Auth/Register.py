from .Algorithms.interfaces.RegisterUser import RegisterUser

class Register:

    def register(self,registerType :RegisterUser):
        registerType.register()