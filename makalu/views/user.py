from django.shortcuts import render, HttpResponseRedirect, HttpResponse, Http404
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.utils.translation import ugettext as _
from django.contrib import messages
from django.urls import reverse
from django.contrib.auth.models import User

from makalu.models import Invoice


@login_required
def user_read(request, u):
    invoiceuser = None
    try:
        invoiceuser = User.objects.get(username=u)

    except User.DoesNotExist:
        messages.success(request, _('Questo Utente non esiste.'))
    
    return render(request, 'makalu/user/read.html', {
        'invoiceuser': invoiceuser
    })
