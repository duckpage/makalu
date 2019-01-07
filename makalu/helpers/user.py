from django.contrib.auth.models import User

def get_user_from_code(fiscalcode):
    try:
        return User.objects.get(fiscal_code=fiscalcode)
    except User.DoesNotExist:
        return User.objects.all()[0]
