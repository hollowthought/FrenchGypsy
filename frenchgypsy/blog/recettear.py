from models import Item, ItemType


def getDifferentItems(item):
	pass


def centered(itemData):

	#get the stats for the item we have
	currentItem = list(Item.objects.filter(id = int(itemData['name'])))
	if not currentItem: return None, itemData
	
	#get a list of types without the type we already have
	types = list(ItemType.objects.all())
	currentid = int(currentItem[0].type.id)
	remainingTypes = [i for i in types if i.id != currentid ]
	

	
	#choose a type out of the remaining types and iterate for all of them
	centeredItems = []
	bounds = 1
	bounds = int(itemData['bounds'])
	
	
	type1Items = Item.objects.filter(type = remainingTypes[0].id) #items of that type
	type2Items = Item.objects.filter(type = remainingTypes[1].id) #items of that type1Items
	type3Items = Item.objects.filter(type = remainingTypes[2].id) #items of that type
	for x in type1Items:
		for y in type2Items:
			for z in type3Items:
				totalGuady = currentItem[0].gaudy  + z.gaudy + y.gaudy + x.gaudy
				totalLight = currentItem[0].light + z.light + y.light + x.light

				if totalGuady >= -1 * bounds and totalGuady <= bounds and totalLight >=  -1 * bounds and totalLight <= bounds:					
					centeredItems.append({'item1' : x, 'item2' : y, 'item3' : z,'gaudy' : totalGuady, 'light' : totalLight})
										
				
	return centeredItems, currentItem[0]