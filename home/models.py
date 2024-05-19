from django.db import models
from django.contrib.auth.modles import User
from cloudinary.models import CloudinaryField


# shows recipe post if drafted or published

STATUS = ((0, "Draft"), (1, "Published"))


# models for create recipe post
class Post(models.Model):
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="recipe_post")
    content = models.TextField()
    image = CloudinaryField('image', default='placeholder')
    excerpt = models.TextField(blank=True)
    status = models.IntegerField(choices=STATUS, default=0)
    likes = models.ManyToManyField(User, related_name="recipe_likes", blank=True)

  # presents wich order the recipes was creaed on
    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return self.title

    def likes(self):
        return self.likes.count()


