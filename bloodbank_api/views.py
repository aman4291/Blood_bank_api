from django.http import HttpResponse
from rest_framework import generics
from bloodbank.models import DonorInfo, Stock
from .serializers import DonorInfoSerializer, StockCreateSerializer, StockSerializer


class StockList(generics.ListAPIView):
    queryset = Stock.objects.all()
    serializer_class = StockSerializer


class StockCreate(generics.CreateAPIView):
    queryset = Stock.objects.all()
    serializer_class = StockCreateSerializer


class DonorInfoList(generics.ListAPIView):
    queryset = DonorInfo.objects.all()
    serializer_class = DonorInfoSerializer


# class PostDetail(generics.RetrieveDestroyAPIView):
#     queryset = Post.objects.all()
#     serializer_class = PostSerializer


""" Concrete View Classes
#CreateAPIView
Used for create-only endpoints.
#ListAPIView
Used for read-only endpoints to represent a collection of model instances.
#RetrieveAPIView
Used for read-only endpoints to represent a single model instance.
#DestroyAPIView
Used for delete-only endpoints for a single model instance.
#UpdateAPIView
Used for update-only endpoints for a single model instance.
##ListCreateAPIView
Used for read-write endpoints to represent a collection of model instances.
RetrieveUpdateAPIView
Used for read or update endpoints to represent a single model instance.
#RetrieveDestroyAPIView
Used for read or delete endpoints to represent a single model instance.
#RetrieveUpdateDestroyAPIView
Used for read-write-delete endpoints to represent a single model instance.
"""


# from django.shortcuts import render

# from bloodbank.models import Stock, DonorInfo


# Create your views here.


def stock_api(request):
    return HttpResponse("stock api success")


def donor_api(request):
    return HttpResponse("donor api success")
