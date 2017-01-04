from django.contrib.auth.decorators import permission_required
from django.core.exceptions import PermissionDenied
from django.shortcuts import render

# Create your views here.
from django.http import Http404
from django.http import HttpResponse
from django.shortcuts import render

from tags.models import Tag
from .models import Blogs
from .forms import BlogForm

def blog_show(request):

    if request.method == "POST":
        form = BlogForm(request.POST)
        if form.is_valid():
            blog = form.save(commit=False)
            blog.owner = request.user
            blog.save()
            form.save_m2m()

    elif request.method == "GET":
        form = BlogForm()

    return render(request, "my_blog.html", {"blogs": Blogs.objects.filter(owner=request.user.id),
                                             "tags": Tag.objects.all(),
                                             "form": form})

def blog_get(request, blog_id):
    try:
        blog = Blogs.objects.get(id=blog_id)
        if request.user.id != blog.owner.id:
            raise PermissionDenied
        return render(request, "detailed_blog.html", {"blog": blog})
    except Blogs.DoesNotExist:
        raise Http404("We don't have any.")

@permission_required('is_superuser')
def show_all_blog(request):
    return render(request, "my_blog.html", {"blogs": Blogs.objects.all()})

@permission_required('is_superuser')
def show_all_blog_from_user(request, userId):
    return render(request, "my_blog.html", {"blogs": Blogs.objects.filter(owner=userId)})
