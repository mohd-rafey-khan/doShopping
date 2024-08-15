from ..interfaces.RegisterUser import RegisterUser
from django.contrib.auth.models import User



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
        user__details = self.__class__._user
        # use this user details to register in doShopping

        # Create and save the User
        user = User.objects.create(
            username=user__details['username'],
            email=user__details['username'],
            is_active=True,
            is_staff=True
        )

        user.set_password(user__details['password'])

        user.save()
