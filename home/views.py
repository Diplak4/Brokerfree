from django.views.generic import View
from django.shortcuts import render,redirect
from .models import *
from django.contrib import messages
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



def signup(request):
    if request.method == 'POST':
        name = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        confirm_password = request.POST['confirm-password']

        if password == confirm_password:
            if User.objects.filter(username=name).exists():
                messages.error(request, 'The username is already taken')
                return redirect('/signup')
            elif User.objects.filter(email=email).exists():
                messages.error(request, 'The email is already used')
                return redirect('/signup')
            else:
                data= Signup.objects.create(
                  name= name,
                  email=email,
                  password=password,
                  confirm_password=confirm_password
                 )
                data.save()
        else:
            messages.error(request, 'The password does not match!')
            return redirect('/signup')
    return render(request, 'signup.html')


