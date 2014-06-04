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
    url(r'^fertilizer.html', views.index),
    url(r'^admin/', include(admin.site.urls)),
)
