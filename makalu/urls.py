from django.urls import path, include

from makalu.views import invoice, customer, user

app_name = 'makalu'

urlpatterns = [
    
    path('invoices/', include([
        path('', invoice.dashboard, name='dashboard'),
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
        path('', customer.customer_list, name='customer-list'),
        path('delete', customer.customer_delete, name='customer-delete'),
        path('create', customer.customer_read, name='customer-create'),
        path('<uuid:uuid>', customer.customer_read, name='customer-read'),
    ])),

    path('users/', include([
        path('<str:u>', user.user_read, name='user-read'),
    ])),
]
