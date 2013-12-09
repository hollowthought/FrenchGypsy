from django.conf.urls.defaults import * 
from frenchgypsy.photogallery.views import archive

urlpatterns = patterns('',
    url(r'^photogallery/$', archive), # sending the actual funcation, not just the name
)
