from rest_framework import serializers
from .models import MenuItem

class menuitemserializer(serializers.ModelSerializer):
    class Meta:
        model=MenuItem
        fields=['title','price','inventory']