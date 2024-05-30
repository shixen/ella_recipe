from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from .models import ContactForm
# Create your views here.

# gets info from form and saves in database
def ContactForm(request):
    if request.method == 'POST':
        fname = request.POST.get('name')
        femail = request.POST.get('email')
        description = request.POST.get('desc')
        query=ContactForm(name=fname, email=femail, description=desc)
        query.save()
        messages.info(request, 'Thanks for ordering!')
        return redirect('/contact')
    return render(request,'contact.html')
