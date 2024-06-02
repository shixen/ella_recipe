from django.db import models


# model for contact form 
class Contact(models.Model):
    name=models.CharField(max_length=30)
    email=models.EmailField()
    phone=models.CharField(max_length=12)
    description=models.TextField(blank=True)