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
    return render(request, 'services.html')


def price(request):
    return render(request, 'price.html')



def signup(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        if not User.objects.filter(username=username).exists():
            # Create a new user with the given username and password
            user = User.objects.create_user(username=username, password=password)
            # Authenticate the user and log them in
            user = authenticate(username=username, password=password)
            login(request, user)
            # Redirect to the login page
            return redirect('login')
        else:
            # If the username is already taken, return an error message
            return render(request, 'signup.html', {'error': 'Username already taken.'})
    else:
        # If the request is not a POST request, just render the empty form
        return render(request, 'signup.html')


def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            # Redirect to the home page
            return redirect('home')
        else:
            # If the username and password don't match, return an error message
            return render(request, 'login.html', {'error': 'Invalid username or password.'})
    else:
        # If the request is not a POST request, just render the empty form
        return render(request, 'login.html')