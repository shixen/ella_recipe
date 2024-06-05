from . import views
from django.urls import path
from .views import PostList, RecipeDetails, CommentEdit, CommentDelete

# urls paths
urlpatterns = [
    path("", views.PostList.as_view(), name="home"),
    path('<slug:slug>/', views.RecipeDetails.as_view(), name='recipe_detail'),
    path('recipe/<slug:slug>/comment/<int:comment_id>/edit/', CommentEdit, name='comment_edit'),
    path('recipe/<slug:slug>/comment/<int:comment_id>/delete/', CommentDelete, name='comment_delete'),
]