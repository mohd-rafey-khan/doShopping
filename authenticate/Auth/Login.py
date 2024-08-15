
from .Controller.interfaces.LoginUser import LoginUser

class Login:

    def login(self,login_instance: LoginUser):
        return login_instance.login()