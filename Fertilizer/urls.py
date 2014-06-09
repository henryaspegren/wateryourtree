from django.conf.urls import patterns, include, url
from core import views

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'Fertilizer.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^$', views.index),
    url(r'^core/', include('core.urls')),
    url(r'^(?P<location_url>\S+)/$', views.produce_detail_page, name='detail_json'),
    url(r'^admin/', include(admin.site.urls)),
)
