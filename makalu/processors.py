
from makalu.fixtures.default import TAX_RATE
from makalu.models import Customer
from makalu.helpers.invoice import get_invoices

def revenue(request):
    main_total = 0
    invoices = get_invoices()
    for invoice in invoices:
        main_total = main_total + invoice['total']

    return {
        'maintotal': main_total,
        'taxrates': TAX_RATE,
        'customers': Customer.objects.all()
    }
