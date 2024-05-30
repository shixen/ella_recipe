from django.urls import path
from . import views
from forms import views

urlpatterns = [
    path('contact/',views.ContactForm,name='contact_form'),
]