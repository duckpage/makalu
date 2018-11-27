from django.utils.crypto import get_random_string

from makalu.models import InvoiceUser


def get_generic_username():
    username = None
    number = 0
    Empty = True
    while(Empty==True):
        number = number + 1
        try:
            InvoiceUser.objects.get(username='user'+str(number))
        except InvoiceUser.DoesNotExist:
            username='user'+str(number)
            Empty = False

    return username


def create_or_get_user_from_code(fiscalcode):
    try:
        return InvoiceUser.objects.get(fiscal_code=fiscalcode)
    except InvoiceUser.DoesNotExist:
        user =  InvoiceUser.objects.create_user(
            get_generic_username(),
            None,
            get_random_string(16)
        )
        user.fiscal_code = fiscalcode
        user.save()
        return user
