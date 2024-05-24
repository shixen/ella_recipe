from django.shortcuts import render, get_object_or_404
from django.views import generic, View
from .models import Post


class PostList(generic.ListView):
    model = Post
    queryset = Post.objects.filter(status=1)
    template_name = 'index.html'

# gets specific recipe to read larger post
class recipeDetails(View):

    def get(self, request, slug, *args, **kwargs):
        queryset = Post.objects.filter(status=1)
        post = get_object_or_404(queryset, slug=slug)
        comments = post.comments.filter(approved=True). order_by('created_on')

  # renders view to html page
        return render(
            request,
            "recipe_detail.html",
            {
                "post": post,
                "comments": comments,
            }
        )