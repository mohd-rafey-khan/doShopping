from .interfaces.RegisterUser import RegisterUser

class JwtRegisterUser(RegisterUser):

    # Constructor
    _user = None

    def __init__(self, *args, **kwargs):
        if args:
            self.__class__._user = args[0]
        elif kwargs:
            self.__class__._user = kwargs
        else:
            self.__class__._user = None

    def register(self):
        user = self.__class__._user
        # use this user details to register in doShopping
        print("JWT registering user: ", user)
        print(user['username'])
        print(user['password'])
        print(user['role'])
