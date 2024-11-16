from django.contrib import admin
from .models import Post, Comment
# The ready-made SummernoteModelAdmin class defines the text editor, enabling you to access its functionality in the admin panel for your posts.
from django_summernote.admin import SummernoteModelAdmin


# When we use a class, we register it with a decorator that is more Pythonic and allows us to customise how the models we are registering will appear on the admin site.
@admin.register(Post)
# This code will give your admin panel greater functionality and clarity. We'll discuss this in more detail soon.
class PostAdmin(SummernoteModelAdmin):

    # These are the header names for the table of posts.
    list_display = ('title', 'slug', 'status', 'created_on')
    # It speeds up the search by limiting which fields will be searched.
    search_fields = ['title', 'content']
    # Add a filter on status to the right-hand sidebar of the admin page. Now, the superuser can choose to filter posts by their draft or published status.
    list_filter = ('status', 'created_on',)
    # In the prepopulated_fields, the tuple containing the single value of title requires a trailing comma.
    # The prepopulated_fields attribute means you no longer need to write the slug yourself.
    prepopulated_fields = {'slug': ('title',)}
    # The summernote_fields attribute matches with the rich-text WYSIWYG editor for the content. 
    summernote_fields = ('content',)


# Register your models here. This will allow you to create, update and delete blog posts from the admin panel.
# Delete the following line:
# admin.site.register(Post)
admin.site.register(Comment)