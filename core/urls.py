from django.conf.urls import patterns, url

from core import views

urlpatterns = patterns('',
  url(r'^$', views.index, name='index'),
  url(r'^create/$', views.create_location, name='create_location'),
  url(r'^list/$', views.list, name='list'),
  url(r'^(?P<location_url>\S+)/json$', views.detail_json, name='detail_json'),
)
