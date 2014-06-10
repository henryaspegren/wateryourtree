from django.conf.urls import patterns, url

from core import views

urlpatterns = patterns('',
  url(r'^create/$', views.create_location, name='create_location'),
  url(r'^list/$', views.list, name='list'),
  url(r'^hit/(?P<location_url>\S+)/$', views.hit, name='hit'),
  url(r'^(?P<location_url>\S+)/$', views.detail_json, name='detail_json')
)
