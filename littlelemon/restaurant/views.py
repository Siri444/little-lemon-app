from rest_framework.decorators import api_view
from .models import menu, booking
from .serializers import menuitemserializer,bookingserializer
from rest_framework import viewsets
from rest_framework import permissions
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateAPIView, DestroyAPIView

# Create your views here. 
class MenuItemsView(ListCreateAPIView):
    queryset = menu.objects.all()
    serializer_class = menuitemserializer

class SingleMenuItemView(RetrieveUpdateAPIView,DestroyAPIView):
    queryset = menu.objects.all()
    serializer_class = menuitemserializer
    
class bookingViewSet(viewsets.ModelViewSet):
   queryset = booking.objects.all()
   serializer_class = bookingserializer
   permission_classes = [permissions.IsAuthenticated] 