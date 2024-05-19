from django.contrib import admin
from .models import Post, Comment
from django_summernote.admin import SummernoteModelAdmin

@admin.register(Post)
# includes the summernote in the context field of posting a recipe
class PostAdmin(SummernoteModelAdmin):

    
    prepopulated_fields = {'slug': ('title',)}
    list_filter = ('status', 'created_on')
    summernote_fields = ('content')
    search_fields = ['title', 'content']
    list_display = ('title', 'status', 'created_on')


@admin.register(Comment)
class adminComments(admin.ModelAdmin):

    list_display = ('body', 'post', 'created_on', 'approved')
    search_fields = ('name', 'email')
    action = ['approve_comments']

    def approve_comments(self, request, queryseyt):
        queryseyt.update(approved=True)