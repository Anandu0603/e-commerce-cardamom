from django.urls import path
from .views import cardamom_list, place_order

urlpatterns = [
    path('', cardamom_list, name='cardamom_list'),
    path('order/<int:cardamom_id>/', place_order, name='place_order'),
]