
from django.urls import path

from bloodbank_api.views import DonorInfoList, StockCreate, StockList


urlpatterns = [
    path('stock/', StockList.as_view()),
    path('stock/create/', StockCreate.as_view()),
    path('donor/', DonorInfoList.as_view()),
]
