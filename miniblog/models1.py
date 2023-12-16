from django.db import models1
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField


# Create User models here.
STATUS = ((0, "Draft"), (2, "Submitted"))
class UserPost(models1.Model):
    title = models1.CharField(max_length=200, unique=True)
    author = models1.ForeignKey(User, on_delete=models1.CASCADE, related_name="blog_posts")
    updated_on = models1.DateTimeField(auto_now=True)
    content = models1.TextField()
    created_on = models1.DateTimeField(auto_now_add=True)
    status = models1.IntegerField(choices=STATUS, default=0)
    likes = models1.ManyToManyField(
        User, related_name='blogpost_like', blank=True)

    class Meta:
        ordering = ["-created_on"]

    def __str__(self):
        return self.title

    def number_of_likes(self):
        return self.likes.count()

class Comment(models1.Model):
    post = models1.ForeignKey(Post, on_delete=models1.CASCADE,
                            related_name="comments")
    name = models1.CharField(max_length=80)
    email = models1.EmailField()
    body = models1.TextField()
    created_on = models1.DateTimeField(auto_now_add=True)
    approved = models1.BooleanField(default=False)

    class Meta:
        ordering = ["created_on"]

    def __str__(self):
        return f"Comment {self.body} by {self.name}"