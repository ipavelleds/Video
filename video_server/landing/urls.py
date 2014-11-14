from django.conf.urls import patterns, url
from views import landing_render, send_request

urlpatterns = patterns('',
    # Examples:
    url(r'^$', landing_render),
    url(r'^send-request$', send_request)
)