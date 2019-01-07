from django import forms

class CustomerForm(forms.Form):
    legal_name = forms.CharField(required=False)
    first_name = forms.CharField(required=False)
    last_name = forms.CharField(required=False)
    fiscal_type = forms.CharField()
    address = forms.CharField()
    address_number = forms.CharField()
    zip_code = forms.CharField()
    city = forms.CharField()
    province = forms.CharField()
    country = forms.CharField()
    fiscal_code = forms.CharField()
    vat_code = forms.CharField(required=False)
    code = forms.CharField()
    pec = forms.EmailField(required=False)