from makalu.models import Company

def get_main_company():
    return Company.objects.get(is_active=True)


def create_or_get_main_company(fatturapa):
    try:
        company = Company.objects.get(is_active=True)
    except customer.DoesNotExist:
        company = Company.objects.create(
            is_active=True,
            name = fatturapa['header']['cedenteprestatore']['anagrafica']['denominazione'],
            address = fatturapa['header']['cedenteprestatore']['sede']['indirizzo'],
            address_number = fatturapa['header']['cedenteprestatore']['sede']['numerocivico'],
            zip_code = fatturapa['header']['cedenteprestatore']['sede']['cap'],
            city = fatturapa['header']['cedenteprestatore']['sede']['comune'],
            province = fatturapa['header']['cedenteprestatore']['sede']['provincia'],
            country = fatturapa['header']['cedenteprestatore']['sede']['nazione'],
            fiscal_code = fatturapa['header']['cedenteprestatore']['codicefiscale'],
            fiscal_type = fatturapa['header']['cedenteprestatore']['regimefiscale'],
            code=fatturapa['header']['datitrasmissione']['codicedestinatario']          
        ) 

        if fatturapa['header']['cedenteprestatore']['idfiscaleiva']['idcodice']:
            company.vat_code = fatturapa['header']['cedenteprestatore']['idfiscaleiva']['idcodice']

        if fatturapa['header']['datitrasmissione']['pecdestinatario']:
            company.pec = fatturapa['header']['datitrasmissione']['pecdestinatario']
