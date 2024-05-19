from django.contrib import admin
from .models import Post
from django_summernote.admin import SummernoteModelAdmin

@admin.register(Post)
# includes the summernote in the context field of posting a recipe
class PostAdmin(SummernoteModelAdmin):

    summernote_fields = ('content')


