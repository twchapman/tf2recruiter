from django.conf.urls.defaults import patterns, include, url
from main.views import index, edit

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', index),
    url(r'^edit/', edit),
    url(r'^frag/(?P<pid>\d+)', frag),
    url(r'^openid/', include('django_openid_consumer.urls')),
    url(r'^admin/', include(admin.site.urls)),
)