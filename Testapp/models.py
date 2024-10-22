from django.db import models
from django.contrib.auth.models import AbstractUser

class Company(models.Model):
    name = models.CharField(max_length=255)
    zip_code = models.CharField(max_length=10)
    email_address = models.EmailField()
    phone = models.CharField(max_length=15)
    web = models.URLField()

    def __str__(self):
        return self.name


class Location(models.Model):
    l_name = models.CharField(max_length=255)
    l_phone = models.CharField(max_length=20)
    l_address = models.CharField(max_length=255)
    l_com = models.CharField(max_length=100, default='default_value')

    def __str__(self):
        return self.l_name

class Employee(models.Model):
    e_name = models.CharField(max_length=255)
    e_phone = models.CharField(max_length=20)
    e_address = models.CharField(max_length=255)
    e_com = models.ForeignKey("Company", on_delete=models.CASCADE)
    e_loc = models.ForeignKey("Location", on_delete=models.CASCADE)
    e_img = models.ImageField( upload_to="", null=True )

    def __str__(self):
        return self.e_name