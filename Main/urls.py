from django.urls import path
from .views import * 
urlpatterns = [
    path('',index,name = 'home'),
    path('store/',store,name = 'store'),
    path('cart/',cart,name = 'cart'),

    path('update_item/',updateItem,name = 'update_item'),
]
 