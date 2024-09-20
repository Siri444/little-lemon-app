from django.urls import path
from . import views

urlpatterns = [
    path('menu-items/', views.LCview.as_view()),
    path('menu-items/<int:pk>', views.SMItemview.as_view()),
    path('message/', views.msg),
]