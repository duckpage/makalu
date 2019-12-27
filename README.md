# makalu
A powerful, yet easy to implement italian einvoice application for Django 2.0+
Below is a quick summary of usage.

Releases:
============

Add the folder ``makalu`` to your django project.

Add ``makalu`` to your ``INSTALLED_APPS`` setting:

    INSTALLED_APPS = (
        ...
        'makalu',
    ) 

Add ``'makalu.processors.revenue'`` to TEMPLATES -> OPTIONS in settings.py.

Add ``path('', include('makalu.urls'))`` in to urls.py.

Run ``manage.py migrate makalu``.

Run ``manage.py firstconfiguration``.

Authentication
===
If you want to use Django autentications system:

Add ``path('accounts/', include('django.contrib.auth.urls')),`` in to urls.py.

Add ``LOGIN_REDIRECT_URL = '/'`` and ``LOGOUT_REDIRECT_URL = '/'`` to settings.py
 
=======

Release 1
================
See branch release/1

