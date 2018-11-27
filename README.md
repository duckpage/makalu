# makalu
A powerful, yet easy to implement einvoice application for Django 2.0+
Below is a quick summary of usage.

Installation
============
Run ``pip install django-makalu``.

Add ``makalu`` to your ``INSTALLED_APPS`` setting:

    INSTALLED_APPS = (
        ...
        'makalu',
    )

Add ``AUTH_USER_MODEL = 'makalu.InvoiceUser'`` at the end of the setting file.

Add ``path('', include('makalu.urls'))`` in to urls.py.

Run ``manage.py migrate makalu``.