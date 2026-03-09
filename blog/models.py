from django.db import models


# Create your models here.


class User(models.Model):
    """Represent user."""

    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    birth_date = models.DateField()
    email = models.EmailField(unique=True)
    country = models.CharField(max_length=2)  # Country Code
    bio = models.CharField(max_length=255, null=True, blank=True)
    city = models.CharField(max_length=100, null=True, blank=True)


class Post(models.Model):
    """Represent a blog post."""

    title = models.CharField(max_length=255)
    text = models.TextField()
    creation_date = models.DateTimeField(auto_now_add=True)
    published = models.BooleanField(default=False)
    description = models.CharField(max_length=255, null=True, blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)


class Category(models.Model):
    """Represent a post category."""

    name = models.CharField(max_length=255)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
