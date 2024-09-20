from django.contrib import admin
from django.urls import path,include
from rest_framework.routers import DefaultRouter
from LittleLemonAPI import views

from restaurant import views
router=DefaultRouter()

router.register('tables', views.bookingViewSet,basename='tables')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('restaurant.urls')),
    path('restaurant/booking/', include(router.urls)),
    path('api/',include('LittleLemonAPI.urls'))
]
