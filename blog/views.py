from django.core.exceptions import PermissionDenied
from django.shortcuts import render

# Create your views here.
from django.http import Http404
from django.http import HttpResponse
from django.shortcuts import render

from tags.models import Tag
from .models import Blogs

def blog_show(request):

    if request.method == "POST":
        blog = Blogs.objects.create(name=request.POST.get("blog_name"),
                            description=request.POST.get("description_name"),
                            owner=request.user)

        blog.tags.add(*request.POST.getlist("tag_names"))


    return render(request, "my_blog.html", {"blogs": Blogs.objects.filter(owner=request.user.id),
                                             "tags":Tag.objects.all()})


def blog_get(request, blog_id):
    try:
        blog = Blogs.objects.get(id=blog_id)
        if request.user.id != blog.owner.id:
            raise PermissionDenied
        return render(request, "detailed_blog.html", {"blog": blog})
    except Blogs.DoesNotExist:
        raise Http404("We don't have any.")