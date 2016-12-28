from django.conf.urls import url

from .views import blog_show, blog_get

urlpatterns = [
    url(r'^$', blog_show),
    url(r'^(?P<blog_id>[0-9]+)/$',blog_get),
]
