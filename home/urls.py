from . import views
from django.urls import path

# imports urls paths
urlpatterns = [
    path("", views.PostList.as_view(), name="home"),
    path('<slug:slug>/', views.recipeDetails.as_view(), name='recipe_details'),
]