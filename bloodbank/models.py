
from django.db import models


BLOOD_GROUP_CHOICES = (
    ("A+", "A+"),
    ("B+", "B+"),
    ("O+", "O+"),
    ("AB+", "AB+"),
    ("A-", "A-"),
    ("B-", "B-"),
    ("O-", "O-"),
    ("AB-", "AB-"),
)


class DonorInfo(models.Model):
    name = models.CharField(max_length=200)
    dob = models.DateField()
    address = models.CharField(max_length=300)
    pincode = models.CharField(max_length=6)
    blood_group = models.CharField(max_length=4, choices=BLOOD_GROUP_CHOICES)
    created_at = models.DateTimeField(auto_now_add=True)
    last_donated_date = models.DateField(null=True, blank=True)
    contact_no = models.CharField(max_length=10)

    def __str__(self):
        return self.name


class Stock(models.Model):
    donated_by = models.ForeignKey(DonorInfo, on_delete=models.CASCADE)
    blood_group = models.CharField(max_length=4, choices=BLOOD_GROUP_CHOICES)
    created_at = models.DateTimeField(auto_now_add=True)
    expiry_date = models.DateField()
    is_used = models.BooleanField(default=False)
    location = models.CharField(max_length=20)

    # genre= models.ForeignKey(Genre, on_delete=models.CASCADE)
    # date_created= models.DateTimeField(default=timezone.now)
