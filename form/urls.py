from django.urls import path
from django.contrib import admin

from .import views
urlpatterns = [

    path('contact/',views.contact, name="contact"),
    path('no/',views.homepage,name='no'),
    path('signin/',views.handle_signin,name='signup'),
    path('admin/', admin.site.urls),
    path('logout', views.Handle_logout, name='logout'),
    path('',views.Handle_login, name='signin'), 

]