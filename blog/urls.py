from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.post_list, name='postlist'),
    url(r'^post/(?P<pk>[0-9]+)/$', views.post_detail, name='postdetail'),
    url(r'^post/(?P<pk>[0-9]+)/edit/$', views.post_edit, name='postedit'),
    url(r'^post/new/$', views.post_new, name='post_new'),
    url(r'^drafts/$', views.post_draft_list, name='postdraftlist'),
    url(r'^post/(?P<pk>\d+)/remove/$', views.post_remove, name='postremove'),
    url(r'^post/(?P<pk>\d+)/publish/$', views.post_publish, name='postpublish'),
    url(r'^post/(?P<pk>\d+)/comment/$', views.add_comment_to_post, name='addcomment'),
    url(r'^comment/(?P<pk>\d+)/approve/$', views.comment_approve, name='comment_approve'),
	url(r'^comment/(?P<pk>\d+)/remove/$', views.comment_remove, name='comment_remove'),
]
