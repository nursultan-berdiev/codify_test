from items.models import Item
from items.serializers import ItemSerializer

queryset = Item.objects.all()
print(queryset)

serializer = ItemSerializer(instance=queryset, many=True)

print(serializer.data)

data = {
    'title': 'Mi',
    'price': 300,
    'description': 'mi phone',
    'category': 1,
    'image': '/media/8._%D0%91%D0%BE%D0%B6%D1%8C%D1%8F_%D0%BA%D0%BE%D1%80%D0%BE%D0%B2%D0%BA%D0%B0.jpg'
}

serializer = ItemSerializer(data=data)
serializer.is_valid()
serializer.save()

queryset = Item.objects.all()
print(queryset)

