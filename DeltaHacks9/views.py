
import time
from .models import BigBuisness
from .models import SmallBusiness
from .serializers import DeltaSerializerBig
from .serializers import DeltaSerializerSmall
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
import consume

@api_view(['GET', 'POST'])
def business_list_big(request, format=None):
    if request.method == 'GET':
        #Get names of all big businesses
        businesses = BigBuisness.objects.all()

        #Serialize them
        serializer = DeltaSerializerBig(businesses, many=True)
        return Response(serializer.data)

    if request.method == 'POST':
        serializer = DeltaSerializerBig(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

@api_view(['GET', 'PUT', 'DELETE'])
def business_details_big(request, id, format=None):

    try:
        business = BigBuisness.objects.get(pk=id)
    except BigBuisness.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = DeltaSerializerBig(business)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = DeltaSerializerBig(business, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        business.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

@api_view(['GET', 'POST'])
def business_list_small(request, format=None):
    if request.method == 'GET':
        #Get names of all big businesses
        businesses = SmallBusiness.objects.all()

        #Serialize them
        serializer = DeltaSerializerSmall(businesses, many=True)
        return Response(serializer.data)

    if request.method == 'POST':

        response = request.data
        response = consume.RemoveBigCompanies(response)
        upload = []
        for item in response:
            upload.append({'name': item['name'], 'photos': item['photos'], 'rating': item['rating']})

        print(upload)
        for item in range(len(upload)):
            serializer = DeltaSerializerSmall(data=upload[item])
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)

        serializer = DeltaSerializerSmall(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
@api_view(['GET', 'PUT', 'DELETE'])
def business_details_small(request, id, format=None):

    try:
        business = SmallBusiness.objects.get(pk=id)
    except SmallBusiness.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = DeltaSerializerSmall(business)
        return Response(serializer.data)

    elif request.method == 'POST':

        print(request)
        response = request.data
        print(response)

        serializer = DeltaSerializerSmall(business, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        business.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
