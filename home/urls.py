from . import views
from django.urls import path

# imports urls
urlpatterns = [
    path("", views.PostList.as_view(), name="home"),
]