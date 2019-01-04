from django.utils.crypto import get_random_string

from django.contrib.auth.models import User


def get_generic_username():
    username = None
    number = 0
    Empty = True
    while(Empty==True):
        number = number + 1
        try:
            User.objects.get(username='user'+str(number))
        except User.DoesNotExist:
            username='user'+str(number)
            Empty = False

    return username


def create_or_get_user_from_code(fiscalcode):
    try:
        return User.objects.get(fiscal_code=fiscalcode)
    except User.DoesNotExist:
        user =  User.objects.create_user(
            get_generic_username(),
            None,
            get_random_string(16)
        )
        user.fiscal_code = fiscalcode
        user.save()
        return user
