from django.shortcuts import render, HttpResponseRedirect, HttpResponse, Http404
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.utils.translation import ugettext as _
from django.contrib import messages
from django.urls import reverse
from django.utils import timezone

from makalu.models import Invoice
from makalu.forms.invoice import InvocieRowForm, InvocieForm
from makalu.helpers.fatturapa import elaborate_xml, get_fatturapa_xml
from makalu.helpers.invoice import *
from makalu.helpers.company import get_company_from_uuid



@login_required
def dashboard(request):
    return render(request, 'makalu/home.html', {
        'invoices': get_invoices(),
        
    })

@login_required
def invoice_read(request, uuid):
    invoice = get_invoice_from_uuid(uuid)
    if invoice:

        if request.method == 'POST':
            form = InvocieForm(request.POST)
            if form.is_valid():
                number = form.cleaned_data['number']
                date = form.cleaned_data['date']
                company_uuid = form.cleaned_data['company']
                
                company = get_company_from_uuid(company_uuid)
                if company:
                    invoice['model'].number = number
                    invoice['model'].date = date
                    invoice['model'].commissioned = company
                    invoice['model'].save()

                    messages.success(request, _('Fattura aggiornata con successo.'))

                    return HttpResponseRedirect(reverse('makalu:dashboard'))
            else:
                messages.warning(request, _('Tutti i campi sono obligatori.'))


        return render(request, 'makalu/invoice/read.html',{
            'invoice': invoice,
            'form':InvocieForm(),
            'articleform': InvocieRowForm()
        })
    else:
        raise Http404()

@login_required
def invoice_create(request):
    if request.method == 'POST':
        invoice = Invoice.objects.create(
            user=request.user,
            date=timezone.now(),
            number=get_invoice_number(),
            transmission_progressive=get_progressive_number()
        )

        return HttpResponseRedirect(reverse('makalu:invoice-read', args=[ invoice.uuid ]))
    
    raise Http404()


@login_required
def invoice_upload(request):
    if request.method == 'POST':
        invoice = request.FILES.get('invoice', None)
        if invoice:
            #try:
            fatturapa = elaborate_xml(invoice)
            create_or_get_invoice(fatturapa)         
            #except BaseException as ex:
            #    messages.warning(request, '{}: {}'.format(_("Errore durante la convalida del file."), str(ex)))
        else:
            messages.warning(request, _("Il file caricato non e valido."))
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


@login_required
def invoice_xml(request, uuid):

    invoice = get_invoice_from_uuid(uuid)
    if invoice:
        stream = get_fatturapa_xml(invoice)


        response = HttpResponse(stream.getvalue(), content_type='application/xml')
        response['Content-Disposition'] = 'attachment; filename="invoice.xml"'
        response['content-length'] = stream.tell()
        return response
    else:
        raise Http404()



@login_required
def invoice_print(request, uuid):

    invoice = get_invoice_from_uuid(uuid)
    if invoice:
        stream = get_invoice_pdf(invoice)
        response = HttpResponse(stream.getvalue(), content_type='application/pdf')
        response['Content-Disposition'] = 'attachment; filename="{}.pdf"'.format(invoice['uuid'])
        response['content-length'] = stream.tell()
        return response

    else:
        raise Http404()



@login_required
def invoice_transmit(request):
    error = None
    if request.method == 'POST':
        uuid = request.POST.get('code', None)
        if uuid:
            try:
                invoice = Invoice.objects.get(uuid=uuid)
                transmit_date = request.POST.get('date', None)
                invoice.transmission_date = timezone.datetime.strptime(transmit_date, '%d/%m/%Y').date()
                invoice.status = 0
                invoice.save()
            except Invoice.DoesNotExist:
                pass

    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))



@login_required
def invoice_row_create(request, uuid):
    try:
        invoice = Invoice.objects.get(uuid=uuid)
        if request.method == 'POST':
            form = InvocieRowForm(request.POST)
            if form.is_valid():
                description = form.cleaned_data['description']
                quantity = form.cleaned_data['quantity']
                unit_price = form.cleaned_data['unit_price']
                taxrate = form.cleaned_data['taxrate']

                invoice_row = InvoiceRow.objects.create(
                    invoice=invoice,
                    number=get_invoice_row_number(invoice),
                    description=description,
                    quantity=quantity,
                    unit_price=unit_price,
                    tax_rate=taxrate,
                    total_price= unit_price + ((unit_price * taxrate) / 100) 
                )

                messages.success(request, _('Articolo aggiunto con successo.'))
    
            else:
                messages.warning(request, _('Tutti i campi sono obligatori.'))

    except Invoice.DoesNotExist:
        messages.warning(request, _('Codice fattura non valido.'))
    
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))



@login_required
def invoice_row_delete(request, uuid):
    error = None
    invoice = get_invoice_from_uuid(uuid)
    if invoice:
        if request.method == 'POST':
            try:
                row_uuid = request.POST.get('code', None)
                redirect = request.POST.get('redirect', None)
                if row_uuid:
                    try:
                        invoicerow = InvoiceRow.objects.get(uuid=row_uuid, invoice=Invoice.objects.get(uuid=uuid))
                        if not invoicerow.invoice.status == 0:
                            invoicerow.delete()
                            return JsonResponse({
                                'status': 0,
                                'code': row_uuid,
                                'type': 'invoicerows',
                                'redirect': redirect
                            })
                        else:
                            error = _('Questa fattura non e in uno stato valido')    
                    except InvoiceRow.DoesNotExist:
                        error = _('Questo fattura non e valido') 
                else:
                    error = _('Il codice non e valido')

            except BaseException as e:
                error = str(e)
        else:
            error = _('Metodo non consentito') 
    else:
        error = _('La fattura non e valida')

    return JsonResponse({
        'status': -1,
        'error': error 
    })