from django.conf.urls import url, include
from django.contrib import admin
from django.conf.urls.static import static
from django.conf import settings

from django.contrib.auth import views

from wagtail.wagtailadmin import urls as wagtailadmin_urls
from wagtail.wagtaildocs import urls as wagtaildocs_urls
from wagtail.wagtailcore import urls as wagtail_urls

urlpatterns = [
    url(r'^admin/', include(wagtailadmin_urls)),
#    url(r'^admin/', admin.site.urls),
    url(r'', include(wagtail_urls)),
   # url(r'', include('blog.urls', namespace="blog")),
    url(r'^accounts/login/$', views.login, name='login'),
    url(r'^accounts/logout/$', views.logout, name='logout', kwargs={'next_page': '/'}),
    url(r'^documents/', include(wagtaildocs_urls)),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)



