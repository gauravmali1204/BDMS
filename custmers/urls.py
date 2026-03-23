from django.urls import path
from . import views


urlpatterns = [
    path('',views.custmer_list,name='custmer_list'),
    path('add/',views.custmer_create,name='custmer_add'),
    path('edit/<int:pk>/',views.custmer_update,name='custmer_edit'),
    path('delete/<int:pk>/',views.custmer_delete,name='custmer_delete'),
]