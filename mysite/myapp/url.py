from django.urls import path
from . import views

urlpatterns = [
    path('', views.myfunction, name='blank'),
    path('main/<int:raqam>', views.main, name='main'),

]