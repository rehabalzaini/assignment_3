from django.conf.urls import url

from .views import *

urlpatterns = [
    url(r'^$', blog_show),
    url(r'^(?P<blog_id>[0-9]+)/$',blog_get),
    url(r'^all/$', show_all_blog),
    url(r'^all/user/(?P<userId>[0-9]+)$', show_all_blog_from_user),
]
