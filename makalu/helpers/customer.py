from makalu.models import Customer, Company

def create_or_get_customer(fatturapa):

    try:
        customer = Customer.objects.get(pec=fatturapa['header']['datitrasmissione']['pecdestinatario'])
    except Customer.DoesNotExist:
        customer = Customer.objects.create(
            name = fatturapa['header']['cessionariocommittente']['anagrafica']['denominazione'],
            address = fatturapa['header']['cessionariocommittente']['sede']['indirizzo'],
            address_number = fatturapa['header']['cessionariocommittente']['sede']['numerocivico'],
            zip_code = fatturapa['header']['cessionariocommittente']['sede']['cap'],
            city = fatturapa['header']['cessionariocommittente']['sede']['comune'],
            province = fatturapa['header']['cessionariocommittente']['sede']['provincia'],
            country = fatturapa['header']['cessionariocommittente']['sede']['nazione'],
            code = fatturapa['header']['datitrasmissione']['codicedestinatario'],
        )

        if fatturapa['header']['cedenteprestatore']['idfiscaleiva']['idcodice']:
            customer.vat_code = fatturapa['header']['cedenteprestatore']['idfiscaleiva']['idcodice']

        if fatturapa['header']['datitrasmissione']['pecdestinatario']:
            customer.pec = fatturapa['header']['datitrasmissione']['pecdestinatario']

    return customer


def get_customer_from_uuid(uuid):
    try:
        return Customer.objects.get(uuid=uuid)
    except Customer.DoesNotExist:
        return None
