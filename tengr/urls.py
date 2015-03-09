from django.conf.urls import patterns, include, url
from django.contrib import admin

from tgr.views import region, region_markers, community, community_modal, feedback

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'tengr.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^modal/community/(?P<region>[\w-]+)/(?P<slug>[\w-]+)/$', community_modal, name="community_modal"),
    url(r'^feedback/(?P<region>[\w-]+)/(?P<slug>[\w-]+)/$', feedback, name="feedback"),
    url(r'^(?P<slug>[\w-]+)/markers/(?P<attrs>[-\w]+)/$', region_markers, name="region_markers_filtered"),
    url(r'^(?P<slug>[\w-]+)/markers/$', region_markers, name="region_markers"),
    url(r'^(?P<region>[\w-]+)/(?P<slug>[\w-]+)/$', community, name="community"),
    url(r'^(?P<slug>[\w-]+)/$', region, name="region"),
)
