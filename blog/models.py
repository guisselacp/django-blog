from django.db import models
from django.contrib.auth.models import User

STATUS = ((0, "Draft"), (1, "Published"))

# Create your models here.
class Post(models.Model):
    # The title values should be unique to avoid having blog posts of the same name confusing your users.
    title = models.CharField(max_length=200, unique=True)
    # In Django, the slug is what you'll use to build a URL for each of your posts.
    slug = models.SlugField(max_length=200, unique=True)
    # One user can write many posts, so this is a one-to-many or Foreign Key. The cascade on delete means that on the deletion of the user entry, all their posts are also deleted.
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="blog_posts"
    )
    # This is the blog article content.
    content = models.TextField()
    # The auto_now_add=True means the default created time is the time of post entry.
    created_on = models.DateTimeField(auto_now_add=True)
    # An attribute status defined as an integer field with a default of 0.
    status = models.IntegerField(choices=STATUS, default=0)
    excerpt = models.TextField(blank=True)
    update_on = models.DateTimeField(auto_now=True)

    
    class Meta:
       ordering = ["-created_on"]
    def __str__(self):
        return f"{self.title} | written by {self.author}"


class Comment(models.Model):
    # many-to-one relationship with the Post model. If a blog post is deleted the comments on it should also be deleted.
    post = models.ForeignKey(
        Post, on_delete=models.CASCADE, related_name="comments")
    # many-to-one relationship with the built-in User model. If a user account is deleted the user's comments will be deleted also.
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="commenter")
    body = models.TextField()
    # Set the default attribute to False.
    approved = models.BooleanField(default=False)
    # Automatically populates when a comment is added but not when updated.
    created_on = models.DateTimeField(auto_now_add=True)
    

    class Meta:
       ordering = ["created_on"]
    def __str__(self):
        return f"Comment {self.body} by {self.author}"