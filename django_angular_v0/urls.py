from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'django_angular_v0.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^$', 'myapp.views.home', name='home'),
    url(r'^admin/', include(admin.site.urls)),
)
