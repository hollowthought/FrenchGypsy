from django.conf.urls.defaults import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'frenchgypsy.views.home', name='home'),
    # url(r'^frenchgypsy/', include('frenchgypsy.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    (r'^admin/', include(admin.site.urls)),
	url(r'', include('frenchgypsy.blog.urls')),
        url(r'', include('frenchgypsy.photogallery.urls')),
    #url(r'^admin/', include('django.contrib.admin.urls')),
    
)
