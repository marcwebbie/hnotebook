from django.conf.urls import patterns, include, url
from django.contrib import admin

from . import views as main_views

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'hnotebook.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', main_views.homepage),
)
