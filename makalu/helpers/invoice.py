from django.utils import timezone
from django.template.loader import render_to_string 

from weasyprint import HTML
from io import BytesIO

from makalu.models import Invoice, InvoiceRow, Company
from makalu.helpers.company import create_or_get_company, create_or_get_primary_company
from makalu.helpers.user import create_or_get_user_from_code

def create_or_get_invoice(fatturapa):
    create_or_get_primary_company(fatturapa)
    company = create_or_get_company(fatturapa)
    try:
        invoice = Invoice.objects.get(commissioned=company, number=fatturapa['body']['datigenerali']['datigeneralidocumento']['numero'])

    except Invoice.DoesNotExist:

        user = create_or_get_user_from_code(fatturapa['header']['datitrasmissione']['idcodice'])

        invoice = Invoice.objects.create(
            commissioned = company,
            user = user,
            number = fatturapa['body']['datigenerali']['datigeneralidocumento']['numero'],
            date = timezone.datetime.strptime(fatturapa['body']['datigenerali']['datigeneralidocumento']['data'], '%Y-%m-%d').date(),
            currency = fatturapa['body']['datigenerali']['datigeneralidocumento']['divisa'],
            tax_rate = fatturapa['body']['datiriepilogo']['aliquotaiva'],
            transmission_country = fatturapa['header']['datitrasmissione']['idpaese'],
            #transmission_code = fatturapa['header']['datitrasmissione']['idcodice'],
            transmission_progressive = fatturapa['header']['datitrasmissione']['progressivoinvio'],
            transmission_format = fatturapa['header']['datitrasmissione']['formatotrasmissione'],
        )

        for item in fatturapa['body']['datibeniservizi']['dettagliolinee']:
            InvoiceRow.objects.create(
                invoice = invoice,
                number = item['numerolinea'],
                description = item['descrizione'],
                quantity = item['quantita'],
                unit_price = item['prezzounitario'],
                total_price = item['prezzototale'],
                tax_rate = item['aliquotaiva'],
            )
    

    return invoice


def get_invoice_data(invoice):
    invoice_total = 0
    invoice_rows = InvoiceRow.objects.filter(invoice=invoice)
    for invoice_row in invoice_rows:
        invoice_total = invoice_total + invoice_row.total_price

    return {
        'model': invoice,
        'uuid': invoice.uuid,
        'status': invoice.status,
        'number': invoice.number,
        'commissioned': invoice.commissioned,
        'user': invoice.user,
        'date': invoice.date,
        'total': invoice_total,
        'rows': invoice_rows,
        'invoice_type': invoice.invoice_type,
        'currency': invoice.currency,
        'tax_rate': invoice.tax_rate,
        'transmission_country': invoice.transmission_country,
        'transmission_date': invoice.transmission_date,
        'transmission_progressive': invoice.transmission_progressive,
        'transmission_format': invoice.transmission_format
    }


def get_invoices():
    invoices = []
    db_invoices = Invoice.objects.all().order_by('number')
    for db_invoice in db_invoices:
        invoices.append(get_invoice_data(db_invoice))

    return invoices

def get_invoices_by_company(company):
    invoices = []
    db_invoices = Invoice.objects.filter(commissioned=company).order_by('number')
    for db_invoice in db_invoices:
        invoices.append(get_invoice_data(db_invoice))

    return invoices


def get_invoice_from_uuid(uuid):
    try:
        db_invoice = Invoice.objects.get(uuid=uuid)
        return get_invoice_data(db_invoice)

    except Invoice.DoesNotExist:
        return None 



def get_invoice_pdf(invoice):
    invoice_bytes = BytesIO()
    invoice_html = render_to_string('makalu/invoice/print.html', { 'invoice': invoice, 'company': Company.objects.get(primary=True)})
    html = HTML(string=invoice_html)
    html.write_pdf(invoice_bytes)
    return invoice_bytes



def get_progressive_number():
    number = 0
    Empty = True
    while(Empty==True):
        number = number + 1
        try:
            Invoice.objects.get(transmission_progressive=number)
        except Invoice.DoesNotExist:
            Empty = False

    return number


def get_invoice_number():
    text = None
    number = 0
    Empty = True
    while(Empty==True):
        number = number + 1
        try:
            Invoice.objects.get(number=str(number).zfill(2))
        except Invoice.DoesNotExist:
            text=str(number).zfill(2)
            Empty = False

    return text


def get_invoice_row_number(invoice):
    number = 0
    Empty = True
    while(Empty==True):
        number = number + 1
        try:
            InvoiceRow.objects.get(number=number, invoice=invoice)
        except InvoiceRow.DoesNotExist:
            Empty = False

    return number