from django.shortcuts import render
from django.views import generic
from .models import Post
# Delete the following line
#from django.http import HttpResponse


# Create your views here.
class PostList(generic.ListView):
    queryset = Post.objects.filter(status=1)
    # Delete the followin code and replace for the next code
    # template_name = "post_list.html"
    template_name = "blog/index.html"
    paginate_by = 6
    
# Delete the following two lines
# def my_blog(request):
#    return HttpResponse("Hello, Blog!")

