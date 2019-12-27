from django.shortcuts import render, HttpResponseRedirect, HttpResponse, Http404
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from django.utils.translation import ugettext as _
from django.contrib import messages
from django.urls import reverse

from makalu.fixtures.default import FISCAL_TYPE, COUNTRIES, PROVINCES
from makalu.models import Customer

from makalu.forms.customer import CustomerForm

from makalu.helpers.fatturapa import elaborate_xml, get_fatturapa_xml
from makalu.helpers.customer import get_customer_from_uuid
from makalu.helpers.invoice import get_invoices_by_customer


@login_required
def customer_list(request):
    return render(request, 'makalu/customer/list.html',{
        'customers': Customer.objects.all()
    })


@login_required
def customer_read(request, uuid=None):
    form = CustomerForm()
    customer = get_customer_from_uuid(uuid)    
    if customer:
        pass
    
    if request.method == 'POST':
        form = CustomerForm(request.POST)
        if form.is_valid():
            legal_name = form.cleaned_data['legal_name']
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            fiscal_type = form.cleaned_data['fiscal_type']
            address = form.cleaned_data['address']
            address_number = form.cleaned_data['address_number']
            zip_code = form.cleaned_data['zip_code']
            city = form.cleaned_data['city']
            province = form.cleaned_data['province']
            country = form.cleaned_data['country']
            fiscal_code = form.cleaned_data['fiscal_code']
            vat_code = form.cleaned_data['vat_code']
            code = form.cleaned_data['code']
            pec = form.cleaned_data['pec']

            if customer:
                customer.fiscal_type = fiscal_type
                customer.address = address
                customer.address_number = address_number
                customer.zip_code = zip_code
                customer.city = city
                customer.province = province
                customer.country = country
                customer.fiscal_code = fiscal_code
                customer.vat_code = vat_code
                customer.code = code
                customer.pec = pec

                if legal_name:
                    customer.legal_name = legal_name
                if first_name:
                    customer.first_name = first_name
                    customer.last_name = last_name

                customer.save()

                messages.success(request, _('Cliente aggiornato con successo.'))

                return HttpResponseRedirect(reverse('makalu:customer-list'))
            else:
                customer = Customer.objects.create(
                    fiscal_type=fiscal_type,
                    address=address,
                    address_number=address_number,
                    zip_code=zip_code,
                    city=city,
                    province=province,
                    country=country,
                    fiscal_code=fiscal_code,
                    code=code,
                )

                if legal_name:
                    customer.legal_name = legal_name
                if first_name:
                    customerfirst_name = first_name
                    customer.last_name = last_name

                if vat_code:
                    customer.vat_code = vat_code
                if pec:
                    customer.pec = pec

                customer.save()

                messages.success(request, _('Cliente creato con successo.'))
                return HttpResponseRedirect(reverse('makalu:customer-list'))
        else:
            messages.warning(request, _('Non sono stati compilati tutti i campi obblgatori'))



    return render(request, 'makalu/customer/read.html',{
        'form': form,
        'customer': customer,
        'invoices': get_invoices_by_customer(customer),
        'fiscaltypes': FISCAL_TYPE,
        'countries': COUNTRIES,
        'provinces': PROVINCES
    })


@login_required
def customer_delete(request):
    error = None
    if request.method == 'POST':
        try:
            uuid = request.POST.get('code', None)
            redirect = request.POST.get('redirect', None)
            if uuid:
                
                customer = get_customer_from_uuid(uuid)
                if customer:

                    invoices = get_invoices_by_customer(customer)
                    if not invoices:
                        customer.delete()

                        return JsonResponse({
                            'status': 0,
                            'code': uuid,
                            'type': 'companies',
                            'redirect': redirect
                        })
                    else:
                        error = _('Non e possibile eliminare questo cliente perche ci sono fatture a lui associate.')    
                else:
                    error = _('Questo cliente non e valido') 
            else:
                error = _('Il codice non e valido')

        except BaseException as e:
            error = str(e)
    else:
        error = _('Metodo non consentito') 

    return JsonResponse({
        'status': -1,
        'error': error 
    })