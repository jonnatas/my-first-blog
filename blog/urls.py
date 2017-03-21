from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.post_list, name='postlist'),
    url(r'^post/(?P<pk>[0-9]+)/$', views.post_detail, name='postdetail'),
    url(r'^post/(?P<pk>[0-9]+)/edit/$', views.post_edit, name='postedit'),
    url(r'^post/new/$', views.post_new, name='post_new'),
    url(r'^post/(?P<pk>\d+)/remove/$', views.post_remove, name='postremove'),
]
