from django.conf.urls.defaults import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', 'meetup.views.front'),
    url(r'^admin/', include(admin.site.urls)),
)
