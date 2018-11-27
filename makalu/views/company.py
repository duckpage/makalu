from django.shortcuts import render, HttpResponseRedirect, HttpResponse, Http404
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from django.utils.translation import ugettext as _
from django.contrib import messages
from django.urls import reverse

from makalu.fixtures.default import FISCAL_TYPE, COUNTRIES, PROVINCES
from makalu.models import Company

from makalu.forms.company import CompanyForm

from makalu.helpers.fatturapa import elaborate_xml, get_fatturapa_xml
from makalu.helpers.company import get_company_from_uuid
from makalu.helpers.invoice import get_invoices_by_company


@login_required
def company_list(request):
    return render(request, 'makalu/company/list.html',{
        'companies': Company.objects.filter(primary=False).order_by('name')
    })


@login_required
def company_read(request, uuid=None):
    form = CompanyForm()
    company = get_company_from_uuid(uuid)    
    if company:
        pass
    
    if request.method == 'POST':
        form = CompanyForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
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

            if company:
                company.name = name
                company.fiscal_type = fiscal_type
                company.address = address
                company.address_number = address_number
                company.zip_code = zip_code
                company.city = city
                company.province = province
                company.country = country
                company.fiscal_code = fiscal_code
                company.vat_code = vat_code
                company.code = code
                company.pec = pec

                company.save()

                messages.success(request, _('Cliente aggiornato con successo.'))

                return HttpResponseRedirect(reverse('makalu:company-list'))
            else:
                company = Company.objects.create(
                    name=name,
                    fiscal_type=fiscal_type,
                    address=address,
                    address_number=address_number,
                    zip_code=zip_code,
                    city=city,
                    province=province,
                    country=country,
                    fiscal_code=fiscal_code,
                    vat_code=vat_code,
                    code=code,
                    pec=pec
                )

                messages.success(request, _('Cliente creato con successo.'))
                return HttpResponseRedirect(reverse('makalu:company-list'))
        else:
            messages.warning(request, _('Non sono stati compilati tutti i campi obblgatori'))



    return render(request, 'makalu/company/read.html',{
        'form': form,
        'company': company,
        'invoices': get_invoices_by_company(company),
        'fiscaltypes': FISCAL_TYPE,
        'countries': COUNTRIES,
        'provinces': PROVINCES
    })


@login_required
def company_delete(request):
    error = None
    if request.method == 'POST':
        try:
            uuid = request.POST.get('code', None)
            redirect = request.POST.get('redirect', None)
            if uuid:
                
                company = get_company_from_uuid(uuid)
                if company:

                    invoices = get_invoices_by_company(company)
                    if not invoices:
                        company.delete()

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