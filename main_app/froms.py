
from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User


class NewCustomerForm(UserCreationForm):
    class Meta:
        model = User
        fields = ("username", "password1", "password2",'first_name', 'last_name', 'email', 'phone', 'place', 'condition')

    def save(self, commit=True):
        user = super(NewCustomerForm, self).save(commit=False)
        user.user_type = User.CUSTOMER
        user.status = User.PENDING
        if commit:
            user.save()
        return user

class NewStaffForm(UserCreationForm):
    class Meta:
        model = User
        fields = ("username", "password1", "password2", 'first_name', 'last_name', 'email', 'phone', 'place', 'condition')

    def save(self,commit=True):
        user = super(NewStaffForm, self).save(commit=False)
        user.user_type = User.STAFF
        user.status = User.PENDING
        if commit:
            user.save()
        return user

class NewProviderForm(UserCreationForm):
    class Meta:
        model = User
        fields = ("username", "password1", "password2", 'provider_name', 'email', 'phone', 'place')
    def save(self,commit=True):
        user = super(NewProviderForm, self).save(commit=False)
        user.user_type = User.PROVIDER
        user.status = User.PENDING
        if commit:
            user.save()
        return user
