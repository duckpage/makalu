from django import forms


class InvocieForm(forms.Form):
    number = forms.CharField()
    date = forms.DateField()
    company = forms.CharField()
    


class InvocieRowForm(forms.Form):
    description = forms.CharField()
    quantity = forms.IntegerField()
    unit_price = forms.FloatField()
    taxrate = forms.FloatField()