from django.conf.urls import patterns, include, url
from django.contrib import admin
import landing.urls

urlpatterns = patterns('',
    # Examples:
    url(r'^', include(landing.urls)),
    # url(r'^blog/', include('blog.urls')),
    url(r'^admin/', include(admin.site.urls)),
)
