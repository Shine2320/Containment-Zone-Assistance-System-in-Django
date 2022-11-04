from random import choices
from django.db import models
from django.contrib.auth.models import AbstractUser
from phonenumber_field.modelfields import PhoneNumberField

# Create your models here.
class User(AbstractUser):
    NO_COVID = 0
    COVID = 1
    CONDITION = ((NO_COVID, "no covid"), (NO_COVID, "covid"))
    PENDING = 0
    ACCEPTED = 1
    REJECTED = 2
    STATUS = ((PENDING, "pending"), (ACCEPTED, "accepted"), (REJECTED, "rejected"))
    CUSTOMER = 0
    STAFF = 1
    PROVIDER = 2
    ADMIN = 3
    USER_TYPE = (
        (ADMIN, "admin"),
        (CUSTOMER, "customer"),
        (STAFF, "staff"),
        (PROVIDER, "provider"),
    )
    provider_name = models.CharField(max_length=100, null=True, blank=True)
    first_name = models.CharField(max_length=100, null=True, blank=True)
    last_name = models.CharField(max_length=100, null=True, blank=True)
    email = models.EmailField(max_length=100, null=True, blank=True)
    phone = PhoneNumberField(null=True, blank=True)
    place = models.CharField(max_length=300, null=True, blank=True)
    condition = models.SmallIntegerField(null=True, blank=True, choices=CONDITION)
    status = models.SmallIntegerField(null=True, blank=True, choices=STATUS)
    user_type = models.SmallIntegerField(null=True, blank=True, choices=USER_TYPE)

class Service(models.Model):
     MEDICINE = 0
     GROCERY = 1
     ELECTRONICS = 2
     FOODS = 3
     DRINKS = 4
     SERVICES = (
          (MEDICINE,"medicine"),
          (GROCERY,"grocery"),
          (ELECTRONICS,"electronics"),
          (FOODS,"foods"),
          (DRINKS,"drinks"),
     )
     service = models.SmallIntegerField(choices=SERVICES,null=True, blank=True)

class MyService(models.Model):
     service =models.ForeignKey(Service,on_delete=models.CASCADE,null=True,blank=True)
     provider =models.ForeignKey(User,on_delete=models.CASCADE,null=True,blank=True)
