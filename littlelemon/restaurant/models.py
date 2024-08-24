from django.db import models
from django.db.models import Model
# Create your models here.

class booking(models.Model):
    booking_id=models.IntegerField()
    Name=models.CharField(max_length=225)
    No_of_guests=models.IntegerField()
    Booking_date=models.DateTimeField()

class menu(models.Model):
    item_id=models.IntegerField()
    title=models.CharField(max_length=225)
    price=models.DecimalField(max_digits=10,decimal_places=2)
    inventory=models.IntegerField()