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


class Tag(models.Model):
    """Represent Tag object."""

    name = models.CharField(max_length=50)


class Image(models.Model):
    """Represent image object."""

    image_file = models.ImageField(upload_to="images/")
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    alter_text = models.CharField(max_length=100, null=True, blank=True)
    publication_date = models.DateTimeField(auto_now_add=True)


class Comment(models.Model):
    """Represent comment."""

    text = models.TextField()
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)


class Like(models.Model):
    """Represents user preferences for a specific post."""

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)


class Follow(models.Model):
    """Represent user's followers and user's followings."""

    follower = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="following"
    )
    following = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="followers"
    )


class Notification(models.Model):
    """ "Represent User notifications."""

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    notification_type = models.CharField(max_length=100)
    is_read = models.BooleanField(default=False)
    creation_date = models.DateTimeField(auto_now_add=True)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)


class PostTag(models.Model):
    """Mediator between Post and Tag."""

    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    tag = models.ForeignKey(Tag, on_delete=models.CASCADE)


class UserTag(models.Model):
    """Mediator between User and Tag."""

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    tag = models.ForeignKey(Tag, on_delete=models.CASCADE)
