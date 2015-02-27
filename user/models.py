from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    """User model. It will manage the user name, email, profile and whatever
    is needed. At the moment, it has the basic options by default.
    """

    pass
