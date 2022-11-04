from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth import login, authenticate, logout
from main_app.froms import NewCustomerForm, NewProviderForm, NewStaffForm
from django.contrib.auth.forms import AuthenticationForm
from .models import *
# Create your views here.
def home(request):
    return render( request,'home.html')

def customer_signup(request):
    data={}
    if request.method == "POST":
        form = NewCustomerForm(request.POST)
        
        print(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, "Registration successful.")
            return redirect("home")
        print("here3")
        messages.error(request, "Unsuccessful registration. Invalid information.")
    else:
        form = NewCustomerForm()
    data['register_form'] = form
    return render(request,"customersignup.html",data)

def staff_signup(request):
    data={}
    if request.method == "POST":
        form = NewStaffForm(request.POST)
        
        print(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, "Registration successful.")
            return redirect("home")
        print("here3")
        messages.error(request, "Unsuccessful registration. Invalid information.")
    else:
        form = NewStaffForm()
    data['register_form'] = form
    return render(request,"staffsignup.html",data)

def provider_signup(request):
    data={}
    if request.method == "POST":
        form = NewProviderForm(request.POST)
        
        print(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, "Registration successful.")
            return redirect("home")
        print("here3")
        messages.error(request, "Unsuccessful registration. Invalid information.")
    else:
        form = NewProviderForm()
    data['register_form'] = form
    return render(request,"providersignup.html",data)

def login_request(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                if user.status == User.ACCEPTED:
                    
                    messages.info(request, f"You are now logged in as {username}.")
                    return redirect("home")
                elif user.status == User.PENDING:
                    messages.info(request, f"Your register request has been processed")
                    return redirect("login")
                elif user.status == User.REJECTED:
                    messages.info(request, f"Your register request has been rejected")
                    return redirect("login") 
            else:
                messages.error(request, "Invalid username or password.")
        else:
            messages.error(request, "Invalid username or password.")
    form = AuthenticationForm()
    return render(request=request, template_name="login.html", context={"login_form": form})