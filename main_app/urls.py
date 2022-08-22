from django.contrib import admin
from django.urls import path,include
from .views import home,customersignup
urlpatterns = [
    # path('admin/', admin.site.urls),
    path('',home),
    path('customersignup/',customersignup,name='customersignup')
]
