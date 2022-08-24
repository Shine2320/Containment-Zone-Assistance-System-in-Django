from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth import login, authenticate, logout
from main_app.froms import NewCustomerForm, NewProviderForm, NewStaffForm

# Create your views here.
def home(request):
    return render( request,'home.html')

def customer_signup(request):
    data={}
    if request.method == "POST":
        form = NewCustomerForm(request.POST)
        
        print(request.POST)
        if form.is_valid():
            print("here2")
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
            print("here2")
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
            print("here2")
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