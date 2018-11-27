from django import forms

class InvoiceUserForm(forms.Form):
    username = forms.CharField()
    fiscal_code = forms.CharField()
    password = forms.CharField(required=False)
    first_name = forms.CharField()
    last_name = forms.CharField(required=False)
    email = forms.EmailField()
    staff = forms.BooleanField(required=False)
    avatar = forms.ImageField(required=False)
