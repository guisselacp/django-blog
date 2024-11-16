from django.contrib import admin
from .models import Post, Comment
from django_summernote.admin import SummernoteModelAdmin


@admin.register(Post)
class PostAdmin(SummernoteModelAdmin):

    list_display = ('title', 'slug', 'status')
    search_fields = ['title']
    list_filter = ('status',)
    # In the prepopulated_fields, the tuple containing the single value of title requires a trailing comma.
    prepopulated_fields = {'slug': ('title',)}
    summernote_fields = ('content',)


# Register your models here. This will allow you to create, update and delete blog posts from the admin panel.
# Delete the following line:
# admin.site.register(Post)
admin.site.register(Comment)