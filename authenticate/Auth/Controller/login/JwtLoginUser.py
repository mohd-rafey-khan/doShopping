from django.contrib.auth import authenticate, login
from rest_framework.response import Response
from ..interfaces.LoginUser import LoginUser

class JwtLoginUser(LoginUser):
    
    _user = None
    request = None

    def __init__(self, *args, **kwargs) -> None:
        # Check if request is passed as a keyword argument
        self.request = kwargs.pop('request', None)

        if args:
            self.__class__._user = args[0]
        elif kwargs:
            self.__class__._user = kwargs
        else:
            self.__class__._user = None

    def login(self):
        user_login_details = self.__class__._user

        print("Authenticating user...", user_login_details)

        # Authenticate user
        user = authenticate(username=user_login_details['username'], password=user_login_details['password'])
        return user
