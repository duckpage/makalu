from django.contrib.auth.models import User

from django.db import models

from uuid import uuid4


class Registry(models.Model):
    uuid = models.UUIDField(default=uuid4, editable=False)
    legal_name = models.CharField(max_length=250, blank=True, null=True)
    first_name = models.CharField(max_length=100, blank=True, null=True)
    last_name = models.CharField(max_length=100, blank=True, null=True)
    fiscal_type = models.CharField(max_length=50, default='RF01')
    address = models.CharField(max_length=250)
    address_number = models.CharField(max_length=60)
    zip_code = models.CharField(max_length=50)
    city = models.CharField(max_length=250)
    province = models.CharField(max_length=5)
    country = models.CharField(max_length=5)
    fiscal_code = models.CharField(max_length=25)
    vat_code = models.CharField(max_length=25, blank=True, null=True)
    code = models.CharField(max_length=7)
    pec = models.EmailField(blank=True, null=True)

    class Meta:
            app_label = 'makalu'


class Customer(Registry):
    pass

    class Meta:
            app_label = 'makalu'

class Company(Registry):
    is_active = models.BooleanField(default=False)

    class Meta:
            app_label = 'makalu'
    


'''
STATUS

0 - Trasmitted
1 - Created


'''

class Invoice(models.Model):
    uuid = models.UUIDField(default=uuid4, editable=False)
    status = models.IntegerField(default=1)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    commissioned = models.ForeignKey(Customer, on_delete=models.CASCADE, blank=True, null=True)
    number = models.CharField(max_length=25, blank=True, null=True)
    invoice_type = models.CharField(max_length=50, default='TD01')
    date = models.DateField()
    currency = models.CharField(max_length=5, default='EUR')
    transmission_country = models.CharField(max_length=5, blank=True, null=True)
    transmission_progressive = models.IntegerField()
    transmission_date = models.DateField(blank=True, null=True)
    transmission_format = models.CharField(max_length=50, default='FPR12')

    class Meta:
            app_label = 'makalu'
    
    

class InvoiceRow(models.Model):
    uuid = models.UUIDField(default=uuid4, editable=False)
    invoice = models.ForeignKey(Invoice, on_delete=models.CASCADE)
    number = models.IntegerField()
    description = models.TextField()
    quantity = models.FloatField()
    unit_price = models.FloatField()
    total_price = models.FloatField()
    tax_rate = models.FloatField() 

    class Meta:
            app_label = 'makalu'