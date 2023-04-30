from django.shortcuts import render,redirect
from .models import *

from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
# Create your views here.


def home(request):
    views={}
    views['services'] = Services.objects.all
    views['feedbacks'] = Feedback.objects.all
    return render(request, 'index.html',views)


def about(request):
    views = {}
    views['feedbacks'] = Feedback.objects.all
    return render(request, 'about.html',views)


def contact(request):
    views={}
    views['informations'] = Information.objects.all
    if request.method == "POST":
        name = request.POST['name']
        email = request.POST['email']
        subject = request.POST['subject']
        message = request.POST['message']
        data = Contact.objects.create(
            name=name,
            email=email,
            subject=subject,
            message=message,
        )
        data.save()

    return render(request, 'contact.html',views)


def portfolio(request):
    return render(request, 'portfolio.html')


def services(request):
    views = {}
    views['services'] = Services.objects.all
    return render(request, 'services.html', views)


def price(request):
    return render(request, 'price.html')


from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login as auth_login, authenticate


def signup(request):
    if request.method == 'POST':
        name = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        confirm_password = request.POST['confirm-password']
        data= Signup.objects.create(
            name= name,
            email=email,
            password=password,
            confirm_password=confirm_password,

        )
        data.save()
    return render(request, 'signup.html')

# def login(request):
#     if request.method == 'POST':
#         form = AuthenticationForm(data=request.POST)
#         if form.is_valid():
#             user = form.get_user()
#             auth_login(request, user)
#             return redirect('home')
#     else:
#         form = AuthenticationForm()
#     return render(request, 'login.html', {'form': form})


