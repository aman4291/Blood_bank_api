
from django.urls import path

from bloodbank_api.views import donor_api, stock_api


urlpatterns = [
    path('stock/', stock_api),
    path('donor/', donor_api),
]
