from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import patterns, include, url
from django.contrib import admin
from musicapp.views import *

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', home, name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^music/',include('music.urls')),
    # url(r'^$',include('music.urls')),
    url(r'^admin/', include(admin.site.urls)),
)
