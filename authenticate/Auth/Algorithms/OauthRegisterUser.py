from .interfaces.RegisterUser import RegisterUser

class OauthRegisterUser(RegisterUser):

    def register(self):
        print("Oauth Register User")