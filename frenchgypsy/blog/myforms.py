from django import forms
from django.forms import ModelForm
from models import Item, ItemType

class StatsForm(forms.Form):
	ticker1 = forms.CharField(max_length = 10, required = True)
	ticker2 = forms.CharField(max_length = 10, required = True)
	
class ItemForm(ModelForm):
	'''myname = forms.ModelMultipleChoiceField(queryset=Item.fields['name'].objects.all())'''
	type = forms.ModelChoiceField(queryset=ItemType.objects.all())
	name = forms.ModelChoiceField(queryset=Item.objects.all())
	bounds = forms.IntegerField(max_value = 10, min_value = 0)
	class Meta:
		model = Item
		fields = []
		
		def __init__(self, *args, **kwargs):
			type = kwargs.pop('user','')
			super(ItemForm, self).__init__(*args, **kwargs)
			self.fields['type']=forms.ModelChoiceField(queryset=ItemType.objects.filter(owner=user))	
def clean(self):
    bounds = self.cleaned_data.get('bounds')
    validate_integer(bounds)
    return self.cleaned_data  	
'''	
class ItemForm(forms.Form):
    name = forms.CharField(max_length=100)
    authors = forms.ModelMultipleChoiceField(queryset=Author.objects.all())
'''
