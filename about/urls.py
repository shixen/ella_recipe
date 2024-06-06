from django.urls import path
from django.views.generic.base import TemplateView


urlpatterns = [
    path('about/', TemplateView.as_view(template_name='about_me.html'), name='about'),
]