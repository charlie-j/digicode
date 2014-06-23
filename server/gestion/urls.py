from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'gestion.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^$', 'gestion.views.home', name='home'),
    url(r'^login/$', 'gestion.views.login_view', name='login'),
    url(r'^logout/$', 'gestion.views.logout_view', name='logout'),

    url(r'^admin/', include(admin.site.urls)),
    (r'^rpc/', include('rpc_server.urls')),

    url(r'^liste/', 'digicode.views.liste', name='liste'),
)

