from django.contrib import admin

from bloodbank.models import DonorInfo, Stock

# Register your models here.
admin.site.register(Stock)
admin.site.register(DonorInfo)
