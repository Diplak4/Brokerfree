from .views import *
from django.urls import path
from . import views
urlpatterns = [
       path('', home, name='home'),
       path('about', about, name='about'),
       path('contact', contact, name='contact'),
       path('portfolio', portfolio, name='portfolio'),
       path('price', price, name='price'),
       path('services', services, name='services'),
       path('signup/', views.signup, name='signup'),
]
