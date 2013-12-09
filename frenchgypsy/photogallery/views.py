# Displays the blog posts

from django.template import loader, Context
from django.http import HttpResponse
from frenchgypsy.photogallery.models import Item

def archive(request): #views get an HttpRequest obj
    posts = Item.objects.all() #BlogPost is one of our models - This is ORM to get all the blog data from the db
    t = loader.get_template("photogallery_archive.html") #we specify the name and django looks in our /templates folder
    c = Context({ 'posts' : posts }) #dictionary like obj w the data
    return HttpResponse(t.render(c)) #views return the HttpRequest


