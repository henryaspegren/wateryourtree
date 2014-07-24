from django.conf.urls import patterns, include, url
from core import views

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', views.index),
    url(r'^core/', include('core.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^detail/(?P<location_url>\S+)/$', views.detail_json, name='detail_json'),
)
