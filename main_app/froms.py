
from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User


class NewUserForm(UserCreationForm):
    CONDITION=[("no covid","no covid"),("covid","covid")]
    email = forms.EmailField(required=True)
    first_name = forms.CharField(required=True)
    last_name = forms.CharField(required=True)
    # username = forms.CharField(required=True)
    # password1 = forms.CharField(required=True)
    # password2 = forms.CharField(required=True)
    place = forms.CharField(required=True)
    phone = forms.IntegerField(required=True)
    condition = forms.ChoiceField(choices=CONDITION,required=True,widget=forms.RadioSelect)
    
    class Meta:
        model = User
        fields = ("username", "password1", "password2",'first_name', 'last_name', 'email', 'phone', 'place', 'condition')

    # def save(self, commit=True):
    #     user = super(NewUserForm, self).save(commit=False)
    #     user.email = self.cleaned_data['email']
    #     if commit:
    #         user.save()
    #     return user
