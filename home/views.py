from django.shortcuts import render
from .models import *
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

