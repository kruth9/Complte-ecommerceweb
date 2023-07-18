
from django.urls import path
from . import views
urlpatterns = [
    path('Home/', views.Home, name="Home"),
    path('developers/', views.Developers, name="developers"),
    path('account', views.Account, name="acc"),
    path('collections/', views.Collections, name="coc"),
    path('Boys/', views.Boys, name="Boys"),
    path('Womens/', views.Womens, name="Womens"),
    path('cart/', views.cart, name='cart'),
   
   
    
]
