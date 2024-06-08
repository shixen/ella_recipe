from django.shortcuts import render, get_object_or_404, redirect
from django.views import View, generic
from .models import Post, Comment
from django.contrib import messages
from django.http import HttpResponse
from .forms import CommentForm


class PostList(generic.ListView):
    model = Post
    queryset = Post.objects.filter(status=1)
    template_name = 'index.html'


class RecipeDetails(View):

    def get(self, request, slug, *args, **kwargs):
        queryset = Post.objects.filter(status=1)
        post = get_object_or_404(queryset, slug=slug)
        comments = post.comments.filter(approved=True).order_by('created_on')
        comment_form = CommentForm()

        return render(
            request,
            "recipe_detail.html",
            {
                "post": post,
                "comments": comments,
                "comment_form": comment_form
            }
        )

    def post(self, request, slug, *args, **kwargs):
        queryset = Post.objects.filter(status=1)
        post = get_object_or_404(queryset, slug=slug)
        comments = post.comments.filter(approved=True).order_by('created_on')
        comment_form = CommentForm(data=request.POST)

        if comment_form.is_valid():
            comment_form.instance.email = request.user.email
            comment_form.instance.name = request.user.username
            comment = comment_form.save(commit=False)
            comment.post = post
            comment.author = request.user
            comment.save()
            commented = True
        else:
            commented = False

        return render(
            request,
            "recipe_detail.html",
            {
                "post": post,
                "comments": comments,
                "commented": commented,
                "comment_form": CommentForm()
            }
        )


def CommentEdit(request, slug, comment_id):
    post = get_object_or_404(Post, slug=slug)
    comment = get_object_or_404(Comment, pk=comment_id)

    if request.method == "POST":
        comment_form = CommentForm(data=request.POST, instance=comment)
        if comment_form.is_valid() and comment.author == request.user:
            comment = comment_form.save(commit=False)
            comment.post = post
            comment.approved = False
            comment.save()

            if not comment.approved:
                messages.add_message(
                    request, messages.INFO, 'Your edit is awaiting approval.')
            else:
                messages.add_message(
                   request, messages.SUCCESS, 'Comment was updated!')

            return redirect('recipe_detail', slug=post.slug)

        else:
            messages.add_message(
                request, messages.ERROR, 'Oops, something went wrong!')
    else:
        comment_form = CommentForm(instance=comment)

    return render(request, 'comment.edit.html', {
        'comment_form': comment_form,
        'comment': comment,
        'post': post,
    })


def CommentDelete(request, slug, comment_id):
    queryset = Post.objects.filter(status=1)
    post = get_object_or_404(queryset, slug=slug)
    comment = get_object_or_404(Comment, pk=comment_id)

    if comment.author == request.user:
        comment.delete()
        messages.add_message
        (request, messages.SUCCESS, 'Comment was successfully deleted!')

    else:
        messages.add_message
        (request, messages.ERROR, 'You can\'t delete others\' comments!')

    return redirect('recipe_detail', slug=post.slug)
