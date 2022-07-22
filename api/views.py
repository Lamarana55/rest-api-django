from urllib import response
from django.shortcuts import render

# Create your views here.
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Item
from .serializers import ItemSerializer
from rest_framework import serializers
from rest_framework import status

@api_view(['GET'])
def ApiOverview(request):
	api_urls = {
		'all_items': '/',
		'Search by Category': '/?category=category_name',
		'Search by Subcategory': '/?subcategory=category_name',
		'Add': '/create',
		'Update': '/update/pk',
		'Delete': '/item/pk/delete'
	}

	return Response(api_urls)


@api_view(['POST'])
def add(request):
    item = ItemSerializer(data = request.data)
    if Item.objects.filter(**request.data).exists():
        raise serializers.ValidationError('this data already exist')

    if item.is_valid():
        item.save()
        return Response(item.data)
    else:
        return Response(status= status.HTTP_404_NOT_FOUND)


@api_view(['GET'])
def index(request):
    if request.query_params:
        items = Item.objects.filter(**request.query_params.dict())
    else:
        items = Item.objects.all()
    return Response(ItemSerializer(items, many=True).data) if items else Response(status=status.HTTP_404_NOT_FOUND)
    """ if items:
        data = ItemSerializer(items, many=True).data
        return Response(data)
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)

    """
@api_view(['PUT'])
def update(request, pk):
    item = Item.objects.get(pk=pk)
    data = ItemSerializer(instance=item, data=request.data)

    if data.is_valid():
        data.save()
        return Response(data.data)
    else:
        Response(status=status.HTTP_404_NOT_FOUND)

@api_view(['DELETE'])
def delete_items(request, pk):
	item = get_object_or_404(Item, pk=pk)
	item.delete()
	return Response(status=status.HTTP_202_ACCEPTED)
    
