from django.shortcuts import render
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth import login, authenticate, logout
from main_app.froms import NewUserForm

# Create your views here.
def home(request):
    return render( request,'home.html')

def customersignup(request):
    if request.method == "POST":
        form = NewUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, "Registration successful.")
            return redirect("home")
        messages.error(request, "Unsuccessful registration. Invalid information.")
    form = NewUserForm()
    return render(request=request, template_name="customersignup.html", context={"register_form": form})