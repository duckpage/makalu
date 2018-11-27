from django.contrib.auth.models import AbstractUser

from django.db import models

from uuid import uuid4

class InvoiceUser(AbstractUser):
    fiscal_code = models.CharField(max_length=25)
    avatar = models.ImageField(upload_to='uploads/users/avatars', blank=True)

    class Meta:
            app_label = 'makalu'


class Company(models.Model):
    uuid = models.UUIDField(default=uuid4, editable=False)
    name = models.CharField(max_length=250)
    primary = models.BooleanField(default=False)
    fiscal_type = models.CharField(max_length=50, default='RF01')
    address = models.CharField(max_length=250)
    address_number = models.CharField(max_length=50)
    zip_code = models.CharField(max_length=50)
    city = models.CharField(max_length=250)
    province = models.CharField(max_length=5)
    country = models.CharField(max_length=5)
    fiscal_code = models.CharField(max_length=25)
    vat_code = models.CharField(max_length=25)
    code = models.CharField(max_length=7, default='0000000')
    pec = models.EmailField(blank=True, null=True)

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
    user = models.ForeignKey(InvoiceUser, on_delete=models.CASCADE)
    commissioned = models.ForeignKey(Company, on_delete=models.CASCADE, blank=True, null=True)
    number = models.CharField(max_length=25, blank=True, null=True)
    invoice_type = models.CharField(max_length=50, default='TD01')
    date = models.DateField()
    currency = models.CharField(max_length=5, default='EUR')
    tax_rate = models.FloatField(blank=True, null=True)
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