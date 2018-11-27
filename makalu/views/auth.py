from django.shortcuts import render, HttpResponseRedirect, HttpResponse, Http404
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.utils.translation import ugettext as _
from django.contrib import messages
from django.urls import reverse

def user_login(request):
    if request.user.is_authenticated:
        return HttpResponseRedirect(reverse('makalu:dashboard'))

    if request.method == 'POST':
        
        username = request.POST.get('username', None)
        password = request.POST.get('password', None)
        if username and password:
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return HttpResponseRedirect(reverse('makalu:dashboard'))

        messages.warning(request, _("I dati inseriti non sono corretti. Riprova."))


    return render(request, 'login.html')


@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect('/')
