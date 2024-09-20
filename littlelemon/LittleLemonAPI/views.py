from django.shortcuts import render
from .serializers import menuitemserializer
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateAPIView,DestroyAPIView
from .models import MenuItem
from rest_framework.decorators import api_view,permission_classes
from rest_framework.permissions import IsAuthenticated
from django.http import HttpResponse
# Create your views here.
class LCview(ListCreateAPIView):
    queryset=MenuItem.objects.all()
    serializer_class=menuitemserializer
    
class SMItemview(RetrieveUpdateAPIView,DestroyAPIView):
    queryset=MenuItem.objects.all()
    serializer_class=menuitemserializer
    
@api_view()
@permission_classes([IsAuthenticated])
def msg(request):
    return HttpResponse({"message":"This view is protected"})