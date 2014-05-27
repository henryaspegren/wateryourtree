from django.conf.urls import patterns, url

from core import views

urlpatterns = patterns('',
  url(r'^$', views.index, name='index'),
  url(r'^(?P<location_url>\S+)/$', views.detail, name='detail'),
)
