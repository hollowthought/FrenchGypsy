from django.conf.urls.defaults import * 
from frenchgypsy.blog.views import archive, stats, atmosphere

urlpatterns = patterns('',
    url(r'^$', archive), # sending the actual funcation, not just the name
	url(r'^blog/$', archive),
	url(r'^stat/$', stats),
	url(r'^rec/$', atmosphere),
	
)
