from django.db import models
from django.contrib import admin

class BlogPost(models.Model):
	title = models.CharField(max_length = 150)
	body = models.TextField()
	timestamp = models.DateTimeField()
	
	class Meta:
	    ordering = ('-timestamp',) #comma makes this a single-item tuple ( otherwise its just a string )
	
class BlogPostAdmin(admin.ModelAdmin):
	list_display = ('title', 'timestamp')
	
class FunkyClass(models.Model):
    type = models.CharField(max_length = 55)
    amount = models.IntegerField()

class ItemType(models.Model):
	name = models.CharField(max_length = 55)
	def __unicode__(self):
	    return self.name
class Item(models.Model):
	name = models.CharField(max_length = 100)
	light = models.IntegerField()
	gaudy = models.IntegerField()
	type = models.ForeignKey('ItemType')
	def __unicode__(self):
	    return self.name
admin.site.register(BlogPost, BlogPostAdmin)