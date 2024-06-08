from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Contact


def contact(request):
    if request.method == 'POST':
        fname = request.POST.get('name')
        femail = request.POST.get('email')
        number = request.POST.get('phone')
        desc = request.POST.get('message')

        query = Contact(
            name=fname, email=femail, phone=number, description=desc)
        query.save()

        messages.info(request, 'Thanks for contacting us!')

        return redirect('contact')

    return render(request, 'contact.html')
