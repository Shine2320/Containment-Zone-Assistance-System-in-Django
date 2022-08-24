from django.contrib import admin
from django.urls import path,include
from .views import *
urlpatterns = [
    # path('admin/', admin.site.urls),
    path('',home,name='home'),
    path('customersignup',customer_signup,name='customersignup'),
    path('staffsignup',staff_signup,name='staffsignup'),
    path('providersignup',provider_signup,name='providersignup'),
]
