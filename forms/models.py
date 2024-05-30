from django.db import models

# Create your models here.

class ContactForm(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField()
    description = models.TextField(blank=True)