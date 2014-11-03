from django.conf.urls import patterns, include, url
from django.contrib import admin

from . import views as main_views

urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', main_views.homepage, name='homepage'),
    url(r'^signup/', main_views.signup,name='signup'),
    url(r'^login/', 'django.contrib.auth.views.login',
        {'template_name': 'login.html'}, name='login'),
)
