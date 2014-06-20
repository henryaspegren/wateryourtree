from django.conf.urls import patterns, url

from core import views

urlpatterns = patterns('',
  url(r'^create/$', views.create_location, name='create_location'),
  url(r'^updatelatitude/$', views.update_latitude, name='updatelatitude'),
  url(r'^updatelongitude/$', views.update_longitude, name='updatelongitude'),
  url(r'^list/$', views.list, name='list'),
  url(r'^hit/(?P<location_url>\S+)/(?P<user_name>\S+[\w ]+)/$', views.hit, name='hit'),
  url(r'^name/(?P<location_name>\S+[\w ]+)/$', views.name_json, name='name_json'),
  url(r'^(?P<location_url>\S+)/$', views.detail_json, name='detail_json')
)

