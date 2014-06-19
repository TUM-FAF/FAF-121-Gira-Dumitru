from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    (r'^$', 'blog.views.index'),



    url(r'^admin/', include(admin.site.urls)),
)
