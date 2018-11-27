from makalu.models import Company

def create_or_get_company(fatturapa):

    try:
        company = Company.objects.get(pec=fatturapa['header']['datitrasmissione']['pecdestinatario'] , primary=False)
    except Company.DoesNotExist:
        company = Company.objects.create(
            name = fatturapa['header']['cessionariocommittente']['anagrafica']['denominazione'],
            address = fatturapa['header']['cessionariocommittente']['sede']['indirizzo'],
            address_number = fatturapa['header']['cessionariocommittente']['sede']['numerocivico'],
            zip_code = fatturapa['header']['cessionariocommittente']['sede']['cap'],
            city = fatturapa['header']['cessionariocommittente']['sede']['comune'],
            province = fatturapa['header']['cessionariocommittente']['sede']['provincia'],
            country = fatturapa['header']['cessionariocommittente']['sede']['nazione'],
            vat_code = fatturapa['header']['cessionariocommittente']['idfiscaleiva']['idcodice'],
            code = fatturapa['header']['datitrasmissione']['codicedestinatario'],
            pec = fatturapa['header']['datitrasmissione']['pecdestinatario'],
        )

    return company


def get_company_from_uuid(uuid):
    try:
        return Company.objects.get(uuid=uuid)
    except Company.DoesNotExist:
        return None


def create_or_get_primary_company(fatturapa):
    try:
        company = Company.objects.get(primary=True)
    except Company.DoesNotExist:
        company = Company.objects.create(
            primary=True,
            name = fatturapa['header']['cedenteprestatore']['anagrafica']['denominazione'],
            address = fatturapa['header']['cedenteprestatore']['sede']['indirizzo'],
            address_number = fatturapa['header']['cedenteprestatore']['sede']['numerocivico'],
            zip_code = fatturapa['header']['cedenteprestatore']['sede']['cap'],
            city = fatturapa['header']['cedenteprestatore']['sede']['comune'],
            province = fatturapa['header']['cedenteprestatore']['sede']['provincia'],
            country = fatturapa['header']['cedenteprestatore']['sede']['nazione'],
            vat_code = fatturapa['header']['cedenteprestatore']['idfiscaleiva']['idcodice'],
            fiscal_code = fatturapa['header']['cedenteprestatore']['codicefiscale'],
            fiscal_type = fatturapa['header']['cedenteprestatore']['regimefiscale']            
        ) 