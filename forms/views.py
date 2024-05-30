from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from .models import ContactForm
# Create your views here.

# gets info from form and saves in database
def ContactForm(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        description = request.POST.get('description')
        query=ContactForm(name=name, email=email, description=description)
        query.save()
        messages.info(request, 'Thanks for ordering!')
        return redirect('/contact')
    return(render, request, 'contact.html')