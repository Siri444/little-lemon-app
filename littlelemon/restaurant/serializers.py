from typing import __all__
from rest_framework import serializers
from .models import menu,booking

class menuitemserializer(serializers.ModelSerializer):
    class Meta:
        model = menu
        fields = ['item_id', 'title', 'price', 'inventory']
        
class bookingserializer(serializers.ModelSerializer):
    class Meta:
        model = booking
        fields = ['booking_id', 'Name', 'No_of_guests', 'Booking_date']