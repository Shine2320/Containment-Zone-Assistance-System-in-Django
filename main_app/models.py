from random import choices
from django.db import models
from django.contrib.auth.models import AbstractUser
from phonenumber_field.modelfields import PhoneNumberField
# Create your models here.
class User(AbstractUser):
    CONDITION=(("no covid","no covid"),("covid","covid"))
    STATUS = (("pending","pending"),("accepted","accepted"),("rejected","rejected"))
    USER_TYPE = (("customer","customer"),("staff","staff"),("provider","provider"),("admin","admin"))
    provider_name = models.CharField(max_length=100,null=True,blank=True)
    first_name = models.CharField(max_length=100,null=True,blank=True)
    last_name = models.CharField(max_length=100,null=True,blank=True)
    email = models.EmailField(max_length=100,null=True,blank=True)
    phone = PhoneNumberField(null=True,blank=True)
    place = models.CharField(max_length=300,null=True,blank=True)
    condition = models.CharField(max_length=100,null=True,blank=True,choices=CONDITION)
    status = models.CharField(max_length=100,null=True,blank=True,choices=STATUS)
    user_type = models.CharField(max_length=100,null=True,blank=True,choices=USER_TYPE)
