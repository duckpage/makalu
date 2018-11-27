from django.urls import path, include

from makalu.views import invoice, auth, company, user

app_name = 'makalu'

urlpatterns = [
    path('', invoice.dashboard, name='dashboard'),


    path('invoice/', include([
        path('upload', invoice.invoice_upload, name='invoice-upload'),
        path('transmit', invoice.invoice_transmit, name='invoice-transmit'),
        path('create', invoice.invoice_create, name='invoice-create'),
        path('<uuid:uuid>', invoice.invoice_read, name='invoice-read'),
        path('<uuid:uuid>/article/create', invoice.invoice_row_create, name='invoice-row-create'),
        path('<uuid:uuid>/article/delete', invoice.invoice_row_delete, name='invoice-row-delete'),
        path('<uuid:uuid>/xml', invoice.invoice_xml, name='invoice-xml'),
        path('<uuid:uuid>/print', invoice.invoice_print, name='invoice-print'),
        
    ])),

    path('customers/', include([
        path('', company.company_list, name='company-list'),
        path('delete', company.company_delete, name='company-delete'),
        path('create', company.company_read, name='company-create'),
        path('<uuid:uuid>', company.company_read, name='company-read'),
    ])),

    path('users/', include([
        path('', user.user_list, name='user-list'),
        path('delete', user.user_delete, name='user-delete'),
        path('create', user.user_read, name='user-create'),
        path('<str:u>', user.user_read, name='user-read'),
    ])),

    path('login', auth.user_login, name='user-login'),
    path('logout', auth.user_logout, name='user-logout'),
]
