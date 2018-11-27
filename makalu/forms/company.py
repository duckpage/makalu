from django import forms

class CompanyForm(forms.Form):
    name = forms.CharField()
    fiscal_type = forms.CharField()
    address = forms.CharField()
    address_number = forms.CharField()
    zip_code = forms.CharField()
    city = forms.CharField()
    province = forms.CharField()
    country = forms.CharField()
    fiscal_code = forms.CharField()
    vat_code = forms.CharField()
    code = forms.CharField(required=False)
    pec = forms.EmailField()