from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^register$', 'rpc_server.views.register', name='register'),
    url(r'^code$', 'rpc_server.views.code', name='code'),
)
