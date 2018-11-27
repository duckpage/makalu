from django.shortcuts import render, HttpResponseRedirect, HttpResponse, Http404
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.utils.translation import ugettext as _
from django.contrib import messages
from django.urls import reverse

from makalu.models import InvoiceUser, Invoice
from makalu.forms.user import InvoiceUserForm

@login_required
def user_list(request):
    return render(request, 'makalu/user/list.html', {
        'users': InvoiceUser.objects.all()
    })


@login_required
def user_read(request, u=None):
    invoiceuser = None
    form = InvoiceUserForm()
    try:
        if u:
            invoiceuser = InvoiceUser.objects.get(username=u)

        if request.method == 'POST':
            form = InvoiceUserForm(request.POST, request.FILES)
            if form.is_valid():
                first_name = form.cleaned_data['first_name']
                last_name = form.cleaned_data['last_name']
                fiscal_code = form.cleaned_data['fiscal_code']
                username = form.cleaned_data['username']
                email = form.cleaned_data['email']
                password = form.cleaned_data['password']
                staff = form.cleaned_data['staff']
                avatar = form.cleaned_data['avatar']

                if invoiceuser:
                    invoiceuser.first_name = first_name
                    invoiceuser.last_name = last_name
                    invoiceuser.email = email
                    invoiceuser.fiscal_code = fiscal_code
                    invoiceuser.is_staff = staff

                    if password:
                        invoiceuser.set_password(password)

                    if avatar:
                        invoiceuser.avatar = avatar
                    
                    invoiceuser.save()
                    messages.success(request, _('Utente aggiornato con successo.'))

                    return HttpResponseRedirect(reverse('makalu:user-list'))
                else:
                    if InvoiceUser.objects.filter(username=username).exists():
                        messages.warning(request, _('Questo username e gia uttilizzato.'))
                    else:
                        if password:
                            new_user = InvoiceUser.objects.create_user(
                                username,
                                email,
                                password
                            )

                            new_user.first_name = first_name
                            new_user.last_name = last_name
                            new_user.fiscal_code = fiscal_code
                            new_user.is_staff = staff

                            if avatar:
                                new_user.avatar = avatar
                            
                            new_user.save()

                            messages.success(request, _('Utente creato con successo.'))

                            return HttpResponseRedirect(reverse('makalu:user-list'))
                        else:
                            messages.warning(request, _('Il campo password e obbligatorio'))

            else:
                messages.warning(request, _('Non sono stati compilati tutti i campi obblgatori'))
        

    except InvoiceUser.DoesNotExist:
        messages.success(request, _('Questo Utente non esiste.'))

    
    return render(request, 'makalu/user/read.html', {
        'invoiceuser': invoiceuser,
        'form': form
    })


@login_required
def user_delete(request):
    error = None
    if request.method == 'POST':
        try:
            username = request.POST.get('code', None)
            redirect = request.POST.get('redirect', None)
            if username:
                if username != request.user.username:

                    invoiceuser = InvoiceUser.objects.get(username=username)
                    
                    invoices = Invoice.objects.filter(user=invoiceuser)
                    if not invoices:
                        invoiceuser.delete()

                        return JsonResponse({
                            'status': 0,
                            'code': username,
                            'type': 'users',
                            'redirect': redirect
                        })
                    else:
                        error = _('Non e possibile eliminare questo utente perche ci sono fatture a lui associate.')     
                else:
                    error = _('Non e possibile cancellare il proprio account') 
            
            else:
                error = _('Il codice non e valido')

        except BaseException as e:
            error = str(e)

        except AuthUser.DoesNotExist:
            error = _('Questo utente non esiste') 
    else:
        error = _('Metodo non consentito') 

    return JsonResponse({
        'status': -1,
        'error': error 
    })