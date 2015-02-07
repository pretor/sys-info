from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
     url(r'^$', 'sysinfo.views.home', name='home'),
     url(r'^get/', 'sysinfo.views.get', name='get'),
     url(r'^json/', 'sysinfo.views.servejson', name='json'),

    url(r'^admin/', include(admin.site.urls)),
)
