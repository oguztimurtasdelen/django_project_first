from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='tracker-home'),
    path('tracker/', views.home, name='tracker-tracker'),

]