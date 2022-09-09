# from django.shortcuts import render
from django.http import HttpResponse

# from bloodbank.models import Stock, DonorInfo


# Create your views here.


def stock_api(request):
    return HttpResponse("stock api success")


def donor_api(request):
    return HttpResponse("donor api success")

   
