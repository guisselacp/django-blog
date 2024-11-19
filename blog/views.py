from django.shortcuts import render, get_object_or_404
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


def post_detail(request, slug):
    """
    Display an individual :model:`blog.Post`.

    **Context**

    ``post``
        An instance of :model:`blog.Post`.

    **Template:**

    :template:`blog/post_detail.html`
    """

    queryset = Post.objects.filter(status=1)
    post = get_object_or_404(queryset, slug=slug)

    return render(request, "blog/post_detail.html", {"post": post},)
