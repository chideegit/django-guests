from django.urls import path 
from .views import * 

urlpatterns = [
    path('add-guest/', add_guest, name='add-guest'), 
    path('update-guest/<int:pk>/', update_guest, name='update-guest'), 
    path('signed-in-guests/', signed_in_guests, name='signed-in-guests'), 
    path('signed-out-guests/', signed_out_guests, name='signed-out-guests'), 
    path('guest-sign-out/<int:pk>/', guest_sign_out, name='guest-sign-out')
]