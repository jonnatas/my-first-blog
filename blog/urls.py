from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.post_list),
    url(r'^posts/(?P<pk>[0-9]+)/$', views.post_detail),
]

