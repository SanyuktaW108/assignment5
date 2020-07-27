from django.db import models

# Create your models here.
from django.db import models
# Create your models here.
class Customer(models.Model):
    username=models.CharField(max_length=50)
    password=models.CharField(max_length=50)
    email=models.CharField(max_length=50)
    phone=models.CharField(max_length=50)


