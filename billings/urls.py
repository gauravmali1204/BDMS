from django.urls import path
from . import views

urlpatterns = [
    path('', views.invoice_list, name='invoice_list'),
    path('generate/<int:order_id>/',views.generate_invoice,name='generate_invoice'),
    path('invoice/<int:pk>/',views.invoice_detail,name='invoice_detail'),
    path('payment/<int:invoice_id>/',views.add_payment,name='add_payment'),
]