
from django.contrib import admin
from django.urls import path, include
from bloodbank_api import urls as bloodbank_api_urls

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(bloodbank_api_urls))
]
