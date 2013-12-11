# Displays the blog posts

from django.template import loader, Context
from django.http import HttpResponse
from frenchgypsy.blog.models import BlogPost
from myforms import StatsForm, ItemForm
from django.template import RequestContext
from stockfunctions import stockCorrelate
from recettear import centered

def archive(request): #views get an HttpRequest obj
    posts = BlogPost.objects.all() #BlogPost is one of our models - This is ORM to get all the blog data from the db
    t = loader.get_template("archive.html") #we specify the name and django looks in our /templates folder
    c = Context({ 'posts' : posts }) #dictionary like obj w the data
    return HttpResponse(t.render(c)) #views return the HttpRequest
	
def stats(request):
	if request.method == 'POST':
		form = StatsForm(request.POST)
		t1 =  request.POST['ticker1']
		t2 =  request.POST['ticker2']
		corr = stockCorrelate(t1,t2)
		c = RequestContext(request,{ 'form' : form,'corr':corr,})
		t = loader.get_template("statresponse.html");
		return HttpResponse(t.render(c))
	else:
		form = StatsForm()
		t = loader.get_template("stat.html");
		c = RequestContext(request,{ 'form' : form,})
	return HttpResponse(t.render(c))

def atmosphere(request):
	if request.method == 'POST':
		form = ItemForm(request.POST)
		if form.is_valid:
			itemData = {'type' : request.POST['type'] , 'name' : request.POST['name'], 'bounds' : request.POST['bounds']}
			centeredItems, currentItem = centered(itemData)
		
		#take these variables and do something
		
			c = RequestContext(request, { 'form': form, 'items' : centeredItems, 'currentItem': currentItem})# template
			t = loader.get_template("recresponse.html");# context
			return HttpResponse(t.render(c))
		else:
			#relative = get_object_or_404(
			form = ItemForm(inital= {'bounds' : 0})
	else:
		form = ItemForm()
		t = loader.get_template("recettear.html");
		c = RequestContext(request,{ 'form' : form,})
	return HttpResponse(t.render(c))