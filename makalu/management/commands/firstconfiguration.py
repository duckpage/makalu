from django.core.management.base import BaseCommand, CommandError

from makalu.models import Company

class Command(BaseCommand):
    help = 'Update Data in Cloud from WebSite'

    def add_arguments(self, parser):
        pass

    def handle(self, *args, **options):   
        try:     
            company_name = input('Company Name: ')
            address = input('Address: ')
            address_number = input('Address Number: ')
            zip_code = input('Zip Code: ')
            city = input('City: ')
            province = input('Province: ')
            fiscal_code = input('Fiscal Code: ')
            vat_code = input('VAT: ')
            pec = input('PEC: ')

            company = Company.objects.create(
                name=company_name,
                primary=True,
                address=address,
                address_number=address_number,
                zip_code=zip_code,
                city=city,
                province=province,
                country='IT',
                fiscal_code=fiscal_code,
                vat_code=vat_code,
                pec=pec
            )

            self.stdout.write(self.style.SUCCESS('Configuration done!'))
 
        except KeyboardInterrupt:
            self.stdout.write(self.style.WARNING('\nInterupted by user'))